import { ChangeEvent, FormEvent, useState} from "react"
import AxiosInstance from "../../../functions/AxiosInstance";
import PasswordField from "../../Input fields/PasswordField"

function AccountDeleteForm({ onDoneChange }: {onDoneChange:Function}){
    const [password, setPassword] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/close-account/', {
        password: password,
      })
      .then(res=>{
        localStorage.removeItem('token');
        onDoneChange(true)
      })
      .catch(err=>{
        console.log(err.response.data)
      })
    }
  
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
        setPassword(e.target.value)
    }
  
    return(
      <div>
        <form onSubmit={(e) => submit(e)}>
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

export default AccountDeleteForm