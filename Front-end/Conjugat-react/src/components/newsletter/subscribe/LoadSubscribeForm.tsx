import { useState } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import SubscribeForm from "./SubscribeForm"

function LoadSubscribeForm({language, setDone, loading, setLoading}: {language:string, setDone:Function, loading:boolean, setLoading:Function}) {
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
        language={language}
        email={email}
        setDone={setDone}
        setEmail={setEmail}
        />
      )
    }
    return (
      <SubscribeForm
        language={language}
        email={email}
        setDone={setDone}
        setEmail={setEmail}
      />
    )
}

export default LoadSubscribeForm