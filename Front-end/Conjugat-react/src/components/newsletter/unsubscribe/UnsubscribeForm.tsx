import { ChangeEvent, FormEvent } from "react"
import { toast } from "react-toastify"
import EmailField from "../../Input fields/EmailField"
import AxiosInstance from "../../../functions/AxiosInstance"
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from "../../../functions/getTranslation";
import { unsubscribeFormTranslations } from "../../../content/newsletter/Unsubscribe";
import '../../../sass/Components/newsletter/unsubscribe/UnsubscribeForm.scss'

function UnsubscribeForm({language, setDone, email, setEmail}: {language:string, setDone:Function, email:string, setEmail:Function}) {
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Unauthorised
      .post('/newsletter/unsubscribe/', {
        email: email,
      })
      .then(res=>{
        setDone(true)
        console.log(res.data)
      })
      .catch(err=>{
        toast.error(err.response.data.error)
      })
    }
    
    function handleEmail(e:ChangeEvent<HTMLInputElement>) {
      setEmail(e.target.value)
    }
  
    return (
      <div className="Unsubscribe-form">
        <form onSubmit={(e) => submit(e)}>
            <div className="email-spacer">
                <EmailField
                id='email'
                email={email}
                labelText={getTranslation(unsubscribeFormTranslations, language, 'Email')}
                handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleEmail(e)}
                required={true}
                />
            </div>

            <SubmitBtn
              value="Unsubscribe"
              style="strong-gold-btn"
            />
        </form>
      </div>
    )
}

export default UnsubscribeForm