import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js"
import { ChangeEvent, FormEvent, useState, useEffect} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'

const url = "http://conjugat.io:8000/subscriptions/process/"
const token = localStorage.getItem("token")
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token '+ token
}

var count: number

function Process() {
  Authorization.AuthRequired()
  count = 0
  return (
    <div>
      <h1>Process</h1>

      <RetrieveStatus />
    </div>
  )
}

function RetrieveStatus() {
  const [subscribed, setSubscribed] = useState(null)
  const [trial, setTrial] = useState(null)
  
  if(count < 2){
    Axios.get(url, {headers: headers})
    .then(res =>{
      setTrial(res.data.trial)
      setSubscribed(res.data.subscribed)
    })
    count += 1
  }
  else{
    if(subscribed == true) {
      window.location.href = "/subscriptions/success"
    }

    return (
      <div>
        <StripeProcess />
        <PaypalProcess trial={trial}/>
        <CoinbaseProcess />
      </div>
    )
  }
   
    return (
      <div>
        <p>Loading...</p>
      </div>
    )
}

function StripeProcess() {
  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      success_url: 'http://localhost:5000/subscriptions/success',
      cancel_url: 'http://localhost:5000/subscriptions/cancelled',
      method: 'Stripe',
      lookup_key: 'Conjugat Premium'
    },
    {
      headers: headers
    })
    .then(res=>{
      console.log(res.data.url)
      window.location.href = res.data.url
    })
  }

  return(
    <div>
      <p>Stripe</p>
      <div>
        <div>
          <h3>Premium plan</h3>
          <h5>$3.00 / month</h5>
        </div>

        <form onSubmit={(e) => submit(e)}>
            <input type="hidden" name="lookup_key" value="Conjugat Premium" />
            <button id="checkout-and-portal-button" type="submit">Checkout</button>
        </form>
      </div>
    </div>
  )
}

function PaypalProcess({trial} : {trial:boolean|null}) {
  const paypalSubscribe = (data:any, actions:any) => {
    if (trial==false) {
      return actions.subscription.create({
        'plan_id': 'P-1L603410HK8214405MP6L5NQ',
      });
    }
    else if (trial==true) {
      return actions.subscription.create({
        'plan_id': 'P-9MS66805EA398571SMP6LZ4Y',
      });
    }
  };

  const paypalOnError = (err:any) => {
    console.log("Error", err)
  }

  const paypalOnCancel = (err:any) => {
    console.log("cancelled", err)
  }

  const paypalOnApprove = (data:any, detail:any) => {
    Axios.post(url, {
      subscriptionID: data.subscriptionID,
      method: 'Paypal',
    },
    {
      headers: headers
    })
    .then(res=>{
      window.location.href = "/subscriptions/success"
    })
  };
  
  if (trial==true || trial==false) {
    return(
      <div>
        <p>Paypal</p>
        <PayPalScriptProvider
          options={{"client-id":`${import.meta.env.VITE_paypal_client_id}`, vault:true}}
        >
          <PayPalButtons
            createSubscription={paypalSubscribe}
            onApprove={paypalOnApprove}
            onError={paypalOnError}
            onCancel={paypalOnCancel}
          />
        </PayPalScriptProvider>
      </div>
    )
  }
  return (
    <div></div>
  )
}

function CoinbaseProcess() {
  const [chargeURL, setChargeURL] = useState('')
  if(count < 2) {
    Axios.post(url, {
      success_url: 'http://localhost:5000/subscriptions/success',
      cancel_url: 'http://localhost:5000/subscriptions/cancelled',
      method: 'Coinbase',
    },
    {
      headers: headers
    })
    .then(res => {
      setChargeURL(res.data.url)
    })
    count += 1
  }
  else{
    return(
      <div>
        <p>Coinbase</p>
        <a href={chargeURL}><button>Purchase</button></a>
      </div>
    )
  }
  return(<div></div>)
}

export default Process