import { FormEvent } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"

function PaypalSuccess({status, setStatus} : {status:string, setStatus:Function}) {
    function submit (e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      const target = e.target as HTMLFormElement
      AxiosInstance.Authorised
      .post('subscriptions/success/', {
        action:target.name
      })
      .then(res=>{
        setStatus(res.data.status)
        // window.location.reload();
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

export default PaypalSuccess