import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import TextField from "../../Input fields/TextField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"

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
        toast.error(err.response.data.error)
      })
    }
  
    return(
      <div>
        <form onSubmit={(e) => submit(e)}>
            <TextField
              id = "username"
              labelText = "Username"
              value = { username }
              handleText = {(e:ChangeEvent<HTMLInputElement>) => setUsername(e.target.value)}
              required = {true}
            />
  
            <PasswordField
              password = {password}
              handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
              id = "password"
              labelText="Password"
            />
  
            <SubmitBtn
              value="Submit"
            />
        </form>
      </div>
    )
}

export default UsernameChangeForm