import { useState } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import SubscribeForm from "./SubscribeForm"

function LoadSubscribeForm({setDone, loading, setLoading}: {setDone:Function, loading:boolean, setLoading:Function}) {
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
      return (
        <SubscribeForm
        email={email}
        setDone={setDone}
        setEmail={setEmail}
        />
      )
    }
    return (
      <SubscribeForm
        email={email}
        setDone={setDone}
        setEmail={setEmail}
      />
    )
}

export default LoadSubscribeForm