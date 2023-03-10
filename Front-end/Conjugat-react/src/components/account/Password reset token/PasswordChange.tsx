import { ChangeEvent, FormEvent, useState } from "react"
import { useParams } from 'react-router-dom'
import AxiosInstance from "../../../functions/AxiosInstance";
import PasswordField from "../../Input fields/PasswordField";

function PasswordChange({ onDoneChange }: {onDoneChange:Function}) {
    const { uidb64, token } = useParams();
    const url = "http://conjugat.io:8000/account/password-reset/confirm"
    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
  
      AxiosInstance.Unauthorised
      .post(url, {
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
  
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handlePassword2(e:ChangeEvent<HTMLInputElement>) {
      setPassword2(e.target.value)
    }
  
    return(
      <form onSubmit={(e) => submit(e)}>
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
        
        <input type="submit" value="Submit" />
      </form>
    )
}

export default PasswordChange