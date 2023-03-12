import { ChangeEvent, FormEvent, useState } from "react"
import AxiosInstance from "../../functions/AxiosInstance"

import UsernameField from "../../Input fields/UsernameField"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"


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
      <div>
        <form onSubmit={(e) => submit(e)}>
          <UsernameField
            username = {username}
            handleUsername = {handleUsername}
            labelText = "Username"
          />
          
          <EmailField
            email={email}
            handleEmail={handleEmail}
          />
          
          <PasswordField
            password = {password}
            handlePassword = {handlePassword}
            id = "password"
            labelText="Password"
          />
          <PasswordField
            password = {password2}
            handlePassword = {handlePassword2}
            id = "password2"
            labelText="Repeat password"
          />
  
          <div className="submit">
            <input type="submit" className="strong-btn" value="Submit" />
          </div>
        </form>
      </div>
    )
}

export default RegisterForm