import { useState } from "react"
import { useNavigate } from "react-router-dom"
import AxiosInstance from "../../../functions/AxiosInstance"
import CoinbaseProcess from "./CoinbaseProcess"
import PaypalProcess from "./PaypalProcess"
import StripeProcess from "./StripeProcess"

function RetrieveStatus() {
    const navigate = useNavigate()
    const [subscribed, setSubscribed] = useState(null)
    const [trial, setTrial] = useState(null)
    const [loading, setLoading] = useState(true)
    const [stripeURL, setStripeURL] = useState('')
    const [stripeCustomerID, setStripeCustomerID] = useState('')
    const [coinbaseURL, setCoinbaseURL] = useState('')
    
    if (loading == true) {
      setLoading(false)

      AxiosInstance.Authorised
      .post('subscriptions/process/', {
        success_url: 'http://localhost:5000/subscriptions/success',
        cancel_url: 'http://localhost:5000/subscriptions/cancelled',
        lookup_key: 'Conjugat Premium',
        method: null,
      })
      .then(res =>{
        setTrial(res.data.trial)
        setSubscribed(res.data.subscribed)
        setStripeURL(res.data.stripe_url)
        setStripeCustomerID(res.data.stripe_customer_id)
        setCoinbaseURL(res.data.coinbase_url)
        console.log(res.data)
      })
      return <></>
    }

    if (subscribed == true) {
      navigate('/subscriptions/success')
    }
    return (
      <>
        <StripeProcess
          url={stripeURL}
          stripeCustomerID={stripeCustomerID}
        />
        <PaypalProcess
          trial={trial}
        />
        <CoinbaseProcess
          url={coinbaseURL}
        />
      </>
    )
}

export default RetrieveStatus