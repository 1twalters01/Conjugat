// import Cookies from "js-cookie"
// import CSRFToken from "../../../functions/CSRFToken"
import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from '../../../functions/getTranslation'
import { EmailChangeFormTranslations } from '../../../content/settings/ChangeEmail'
import '../../../sass/Components/settings/Change email/EmailChangeForm.scss'

function EmailChangeForm({ language, onDoneChange }: { language:string, onDoneChange:Function}){
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/change-email/', {
        email: email,
        password: password,
      })
      .then(res=>{
        onDoneChange(true)
      })
      .catch(err=>{
        toast.error(err.response.data.error)
      })
    }
  
    return(
      <div className="Email-change-form-container">
        <form onSubmit={(e) => submit(e)}>
            {/* <CSRFToken /> */}
            <div className="email-spacer">
                <EmailField
                id="email"
                email={email}
                handleEmail={(e:ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
                labelText={getTranslation(EmailChangeFormTranslations, language, 'Email')}
                required={true}
                />
            </div>
            
            <div className="password-spacer">
                <PasswordField
                password = {password}
                handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
                id = "password"
                labelText={getTranslation(EmailChangeFormTranslations, language, 'Password')}
                />
            </div>
            
  
            <SubmitBtn
              value={getTranslation(EmailChangeFormTranslations, language, 'Submit')}
              style="strong-gold-btn"
            />
        </form>
      </div>
    )
}

export default EmailChangeForm