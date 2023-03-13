import { ChangeEvent, FormEvent, useState} from "react"
import AxiosInstance from "../../../functions/AxiosInstance"
import UsernameField from "../../Input fields/UsernameField"
import PasswordField from "../../Input fields/PasswordField"


function UsernameChangeForm({ onDoneChange }: {onDoneChange:Function}){
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/change-username/', {
        username: username,
        password: password,
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
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
  
    return(
      <div>
        <form onSubmit={(e) => submit(e)}>
            <UsernameField
              username = {username}
              handleUsername = {handleUsername}
              labelText = "Username"
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

export default UsernameChangeForm