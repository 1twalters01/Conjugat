import { useState } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import StripeSuccess from "../../subscriptions/success/StripeSuccess"
import PaypalSuccess from "../../subscriptions/success/PaypalSuccess"
import CoinbaseSuccess from "../../subscriptions/success/CoinbaseSuccess"
import StripeProcess from "../../subscriptions/Process/StripeProcess"
import PaypalProcess from "../../subscriptions/Process/PaypalProcess"
import CoinbaseProcess from "../../subscriptions/Process/CoinbaseProcess"

function RetrievePremiumStatus() {
    const [loading, setLoading] = useState(true)

    const [method, setMethod] = useState(null)
    const [subscribed, setSubscribed] = useState(null)
    const [url, setURL] = useState('')
    const [status, setStatus] = useState('')
    
    const [trial, setTrial] = useState(null)
    const [stripeURL, setStripeURL] = useState('')
    const [stripeCustomerID, setStripeCustomerID] = useState('')
    const [coinbaseURL, setCoinbaseURL] = useState('')

    if(loading == true) {
      setLoading(false)

      AxiosInstance.Authorised
      .post('settings/premium/',{
        return_url: window.location.href,
        success_url: 'http://localhost:5000/subscriptions/success',
        cancel_url: 'http://localhost:5000/settings/premium',
        lookup_key: 'Conjugat Premium',
        method: null
      })
      .then(res =>{
        if (res.data.subscribed == true) {
            setMethod(res.data.method)
            setSubscribed(res.data.subscribed)
            setURL(res.data.url)
            setStatus(res.data.status)
        }
        else{
            setTrial(res.data.trial)
            setSubscribed(res.data.subscribed)
            setStripeURL(res.data.stripe_url)
            setStripeCustomerID(res.data.stripe_customer_id)
            setCoinbaseURL(res.data.coinbase_url)
        }
      })
    }

    if(subscribed == false) {
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

    if(method === 1 && subscribed == true) {
        return (
            <div>
                <StripeSuccess url={url}/>
            </div>
        )
    }
    else if(method === 2 && subscribed == true) {
        return (
            <div>
                <PaypalSuccess status={status}/>
            </div>
        )
    }
    else if(method === 3 && subscribed == true) {
        return (
            <div>
                <CoinbaseSuccess charge={url} />
            </div>
        )
    }
    return <></>
}

export default RetrievePremiumStatus