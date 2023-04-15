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
      const base = import.meta.env.VITE_CLIENT_URL as string
      AxiosInstance.Authorised
      .post('subscriptions/retrieve-status/', {
        success_url: base+'subscriptions/success',
        cancel_url: base+'subscriptions/cancelled',
      })
      .then(res =>{
        setSubscribed(res.data.subscribed)
        setTrial(res.data.trial)
        setStripeCustomerID(res.data.stripe_customer_id)
        setStripeURL(res.data.stripe_url)
        setCoinbaseURL(res.data.coinbase_url)
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