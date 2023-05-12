import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import handleText from "../../../functions/handlers/handleText"
import EmailField from "../../Input fields/EmailField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from "../../../functions/getTranslation"
import { PasswordResetFormTranslations } from '../../../content/account/PasswordReset'
import '../../../sass/Components/account/Password reset/PasswordResetForm.scss'

function PasswordResetForm({language, onDoneChange}: {language:string, onDoneChange:Function}) {
    const domain = window.location.origin + "/account/"
    const [email, setEmail] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/password-reset/', {
            email: email,
            domain: domain
        })
        .then(
            onDoneChange(true)
        )
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }
  
    return (
      <div className="passwordReset-form">
          <form onSubmit={(e) => submit(e)}>
              <div className="email-spacer">
                  <EmailField
                  id='email'
                  email={email}
                  labelText={getTranslation(PasswordResetFormTranslations, language, 'Email')}
                  handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setEmail)}
                  required={true}
                  />
              </div>

              <SubmitBtn
              value={getTranslation(PasswordResetFormTranslations, language, 'Reset Password')}
              style="strong-gold-btn"
              />
          </form>
      </div>
    )
}

export default PasswordResetForm