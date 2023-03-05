import { FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'
import PropTypes from 'prop-types'

const url = "http://conjugat.io:8000/subscriptions/success/"
const token = localStorage.getItem("token")
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token '+ token
}

var count: number
count = 0

function Success() {
  Authorization.AuthRequired()
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
  const [charge, setCharge] = useState('')
  const [status, setStatus] = useState('')
  
  if(count < 2){
    Axios.get(url, {headers: headers})
    .then(res =>{
      setMethod(res.data.method)
      setSubscribed(res.data.subscribed)
      setCharge(res.data.charge)
      setStatus(res.data.status)
      console.log(res.data)
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
      console.log(status, 'paypal')
      return (
        <div>
          <PaypalSuccess status={status}/>
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

function PaypalSuccess({status} : {status:string}) {
  function submit (e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const target = e.target as HTMLFormElement
    Axios.post(url, {
      action:target.name
    },
    {
    headers:headers
    })
    .then(res=>{
      window.location.reload();
    })
  }  

  if (status === 'ACTIVE') {
    return (
      <form method="post" onSubmit={(e) => submit(e)} name="Stop">
        <input type="submit" value="Stop subscription" />
      </form>
    )
  }
  else if (status === 'SUSPENDED') {
    return (
      <form onSubmit={(e) => submit(e)} name="Re-start">
        <input type="submit" value="Restart subscription" />
      </form>
    )
  }
  else if (status === 'CANCELLED') {
    return (
      <p>Subscription has been cancelled.</p>
    )
  }
  return (
    <div>Paypal {status}</div>
  )
}

function CoinbaseSuccess({charge} : {charge:string}) {
  return (
    <div>
      <p>Coinbase</p>
      <a href={charge}><button>View Purchase</button></a>
    </div>
    
  )
}
CoinbaseSuccess.propTypes = {
  charge: PropTypes.string
}


export default Success