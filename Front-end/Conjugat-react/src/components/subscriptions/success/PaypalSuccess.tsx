import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import { FormEvent } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import { getTranslation } from "../../../functions/getTranslation"
import { PaypalSuccessTranslations } from "../../../content/settings/Premium"

function PaypalSuccess({status, setStatus} : {status:string, setStatus:Function}) {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)

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
          <input type="submit" value={getTranslation(PaypalSuccessTranslations, language, 'Text1')} />
        </form>
      )
    }
    else if (status === 'SUSPENDED') {
      return (
        <form onSubmit={(e) => submit(e)} name="Re-start">
          <input type="submit" value={getTranslation(PaypalSuccessTranslations, language, 'Text2')} />
        </form>
      )
    }
    else if (status === 'CANCELLED') {
      return (
        <p>{getTranslation(PaypalSuccessTranslations, language, 'Text3')}</p>
      )
    }
    return (
      <div>Paypal {status}</div>
    )
}

export default PaypalSuccess