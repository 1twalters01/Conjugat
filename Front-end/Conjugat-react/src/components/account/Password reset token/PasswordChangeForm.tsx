import { ChangeEvent, FormEvent, useState } from "react"
import { useParams } from 'react-router-dom'
import AxiosInstance from "../../../functions/AxiosInstance";
import PasswordField from "../../Input fields/PasswordField";
import SubmitBtn from "../../Input fields/SubmitBtn";
import '../../../sass/Components/account/Password reset token/PasswordChangeForm.scss'
import handleText from "../../../functions/handlers/handleText";

function PasswordChangeForm({ onDoneChange }: {onDoneChange:Function}) {
    const { uidb64, token } = useParams();
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
            console.log(err.response.data.error)
        })
    }
  
    return(
      <div className="passwordChange-form">
        <form onSubmit={(e) => submit(e)}>
          <PasswordField
            password = {password}
            handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword)}
            id = "password"
            labelText="Password"
          />
          <div className="password-spacer"></div>

          <PasswordField
            password = {password2}
            handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword2)}
            id = "password2"
            labelText="Repeat password"
          />
          <div className="password-spacer2"></div>
          
          <SubmitBtn
            value="Change Password"
          />
        </form>
      </div>
    )
}

export default PasswordChangeForm