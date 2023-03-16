import { useState } from "react"
import { useNavigate } from "react-router-dom"
import AxiosInstance from "../../../functions/AxiosInstance"
import StripeSuccess from "./StripeSuccess"
import PaypalSuccess from "./PaypalSuccess"
import CoinbaseSuccess from "./CoinbaseSuccess"

function RetrieveSuccessStatus() {
    const navigate = useNavigate()
    const [method, setMethod] = useState(null)
    const [subscribed, setSubscribed] = useState(null)
    const [url, setURL] = useState('')
    const [status, setStatus] = useState('')
    const [loading, setLoading] = useState(true)
    
    if(loading == true) {
      setLoading(false)

      AxiosInstance.Authorised
      .post('subscriptions/success/',{
        return_url: window.location.href,
        method: null
      })
      .then(res =>{
        console.log(res.data)
        setMethod(res.data.method)
        setSubscribed(res.data.subscribed)
        setURL(res.data.url)
        setStatus(res.data.status)
      })
    }

    if(subscribed == false) {
        navigate('/subscriptions/process')
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
  
  
  
  
  
  

export default RetrieveSuccessStatus