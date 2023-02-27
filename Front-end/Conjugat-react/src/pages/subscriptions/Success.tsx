import { ChangeEvent, FormEvent, useState, useEffect} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'
import { useNavigate } from 'react-router'

const url = "http://conjugat.io:8000/subscriptions/success/"
const token = localStorage.getItem("token")
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token '+ token
}
var count: number

function Success() {
  Authorization.AuthRequired()
  count = 0
  return (
    <div>
      <h1>Success</h1>

      <RetrieveStatus />
    </div>
  )
}

function RetrieveStatus() {
  const [method, setMethod] = useState(null)
  const [subscribed, setSubscribed] = useState(null)
  const [charge, setCharge] = useState(null)
  
  if(count < 2){
    Axios.get(url, {headers: headers})
    .then(res =>{
      setMethod(res.data.method)
      setSubscribed(res.data.subscribed)
      setCharge(res.data.charge)
    })
    count += 1
  }
  else{
    if(method == null || subscribed == false) {
      return (
        <div>
          <NotSubscribed />
        </div>
      )
    }
    if(method == 'Stripe' && subscribed == true) {
      return (
        <div>
          <StripeSuccess />
        </div>
      )
    }
    else if(method == 'Paypal' && subscribed == true) {
      return (
        <div>
          <PaypalSuccess />
        </div>
      )
    }
    else if(method == 'Coinbase' && subscribed == true) {
      console.log(charge)
      return (
        <div>
          <CoinbaseSuccess charge={charge} />
        </div>
      )
    }
    return (
      <div>
        <p>Error</p>
      </div>
    )
  }
  return(
    <div></div>
  )
}

function NotSubscribed() {
  return (
    <div>None</div>
  )
}

function StripeSuccess() {
  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      return_url: window.location.href
    },
    {
      headers: headers
    })
    .then(res=>{
      console.log(res.data.url)
      window.location.href = res.data.url
    })
  }

  return (
    <div>
      <p>Stripe</p>
      <p>Your payment has been processed successfully</p>

      <form action="" onSubmit={(e) => submit(e)}>
        <input type="hidden" id="session-id" name="session_id" value="" />
        <button id="checkout-and-portal-button" type="submit">Manage your billing information</button>
      </form>
    </div>
    
  )
}

function PaypalSuccess() {
  return (
    <div>Paypal</div>
  )
}

function CoinbaseSuccess({charge}) {
  console.log(charge)
  return (
    <div>
      <p>Coinbase</p>
      <a href={charge}><button>View Purchase</button></a>
    </div>
    
  )
}

export default Success