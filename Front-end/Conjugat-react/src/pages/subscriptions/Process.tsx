import { ChangeEvent, FormEvent, useState, useEffect} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'
import { useNavigate } from 'react-router'

const url = "http://conjugat.io:8000/subscriptions/process/"
const token = localStorage.getItem("token")
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token '+ token
}
var count = 0

function Process() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Process</h1>

      <StripeProcess />
      <PaypalProcess />
      <CoinbaseProcess />
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

function PaypalProcess() {
  return(
    <div>
      <p>Paypal</p>
    </div>
  )
}

function CoinbaseProcess() {
  const [chargeURL, setChargeURL] = useState(null)
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
  
}

export default Process