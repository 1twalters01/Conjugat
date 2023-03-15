import { ChangeEvent, FormEvent, useState } from "react"
import AxiosInstance from "../../../functions/AxiosInstance"

import TextField from "../../Input fields/TextField"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Input fields/SubmitBtn"

import '../../../sass/Components/account/Register/RegisterForm.scss'

function RegisterForm({ onDoneChange }: {onDoneChange:Function}) {
    const domain = window.location.origin + "/account/"
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('')
  
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
        console.log(err.response.data)
      })
    }
  
    function handleUsername(e:ChangeEvent<HTMLInputElement>) {
      setUsername(e.target.value)
    }
    function handleEmail(e:ChangeEvent<HTMLInputElement>) {
      setEmail(e.target.value)
    }
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handlePassword2(e:ChangeEvent<HTMLInputElement>) {
      setPassword2(e.target.value)
    }
  
    return (
      <div className="register-form">
        <form onSubmit={(e) => submit(e)}>
          <TextField
            id='username'
            value = {username}
            handleText = {handleUsername}
            labelText = "Username"
            required={false}
          />
          <div className="username-spacer"></div>
          
          <EmailField
            id='email'
            email={email}
            labelText="Email"
            handleEmail={handleEmail}
          />
          <div className="email-spacer"></div>
          
          <PasswordField
            password = {password}
            handlePassword = {handlePassword}
            id = "password"
            labelText="Password"
          />
          <div className="password-spacer"></div>
          
          <PasswordField
            password = {password2}
            handlePassword = {handlePassword2}
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