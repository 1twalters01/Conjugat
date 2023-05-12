import { ChangeEvent, FormEvent, useState } from "react"
import { useParams } from 'react-router-dom'
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import handleText from "../../../functions/handlers/handleText"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from "../../../functions/getTranslation"
import { PasswordChangeTokenFormTranslations } from "../../../content/account/PasswordResetToken"
import '../../../sass/Components/account/Password reset token/PasswordChangeForm.scss'

function PasswordChangeForm({ language, onDoneChange }: { language:string, onDoneChange:Function}) {
    const { uidb64, token } = useParams()
    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/password-reset/confirm', {
            uidb64: uidb64,
            token: token,
            password: password,
            password2: password2,
        })
        .then(res =>{
            onDoneChange(true)
        })
        .catch(err => {
            toast.error(err.response.data.error)
        })
    }
  
    return(
      <div className="passwordChange-form">
        <form onSubmit={(e) => submit(e)}>
          <div className="password-spacer">
            <PasswordField
              password = {password}
              handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword)}
              id = "password"
              labelText={getTranslation(PasswordChangeTokenFormTranslations, language, 'Password')}
            />
          </div>

          <div className="password-spacer2">
            <PasswordField
              password = {password2}
              handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword2)}
              id = "password2"
              labelText={getTranslation(PasswordChangeTokenFormTranslations, language, 'password2')}
            />
          </div>
          
          <SubmitBtn
            value={getTranslation(PasswordChangeTokenFormTranslations, language, 'Change Password')}
            style="strong-gold-btn"
          />
        </form>
      </div>
    )
}

export default PasswordChangeForm