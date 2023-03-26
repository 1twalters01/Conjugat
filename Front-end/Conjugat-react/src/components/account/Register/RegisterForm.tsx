import { ChangeEvent, FormEvent, useState } from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import handleText from "../../../functions/handlers/handleText"
import TextField from "../../Input fields/TextField"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import '../../../sass/Components/account/Register/RegisterForm.scss'

function RegisterForm({ onDoneChange }: {onDoneChange:Function}) {
    const domain = window.location.origin + "/account/"
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('')
    const [username, setUsername] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/register/', {
            username: username,
            email: email,
            password: password,
            password2: password2,
            domain: domain
        })
        .then(res=>{
            onDoneChange(true)
        })
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }

    return (
      <div className="register-form">
        <form onSubmit={(e) => submit(e)}>
          <TextField
            id='username'
            value = {username}
            handleText={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setUsername)}
            labelText = "Username"
            required={false}
          />
          <div className="username-spacer"></div>
          
          <EmailField
            id='email'
            email={email}
            labelText="Email"
            handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setEmail)}
          />
          <div className="email-spacer"></div>
          
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
            value="Sign up"
          />
        </form>
      </div>
    )
}

export default RegisterForm