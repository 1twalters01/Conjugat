import { useState } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import UnsubscribeForm from "./UnsubscribeForm"

function LoadUnsubscribeForm({setDone, loading, setLoading}: {setDone:Function, loading:boolean, setLoading:Function}) {
    const [email, setEmail] = useState('')
  
    if (loading) {
      var Axios
      if (localStorage.getItem("token")) {Axios = AxiosInstance.Authorised}
      else {Axios = AxiosInstance.Unauthorised}
      Axios
      .get('newsletter/subscribe/')
      .then(res =>{
        setEmail(res.data.email)
        setLoading(false)
      })
      return <></>
    }
    return (
      <UnsubscribeForm
        email={email}
        setDone={setDone}
        setEmail={setEmail}
      />
    )
}

export default LoadUnsubscribeForm