import { ChangeEvent, FormEvent, useState} from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"

function EmailChangeForm({ onDoneChange }: {onDoneChange:Function}){
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
        console.log(err.response.data)
      })
    }
  
    function handleEmail(e:ChangeEvent<HTMLInputElement>) {
      setEmail(e.target.value)
    }
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
  
    return(
      <div>
        <form onSubmit={(e) => submit(e)}>
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
  
            <button>Submit</button>
        </form>
      </div>
    )
}

export default EmailChangeForm