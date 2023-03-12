import { ChangeEvent, FormEvent, useState} from "react"
import AxiosInstance from "../../functions/AxiosInstance"
import PasswordField from "../../Input fields/PasswordField"


function PasswordChangeForm({ onDoneChange }: {onDoneChange:Function}){
    const [password, setPassword] = useState('')
    const [newPassword1, setNewPassword1] = useState('')
    const [newPassword2, setNewPassword2] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/change-password/', {
        password: password,
        newPassword1: newPassword1,
        newPassword2: newPassword2,
      })
      .then(res=>{
        onDoneChange(true)
      })
      .catch(err=>{
        console.log(err.response.data)
      })
    }
  
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handleNewPassword1(e:ChangeEvent<HTMLInputElement>) {
      setNewPassword1(e.target.value)
    }
    function handleNewPassword2(e:ChangeEvent<HTMLInputElement>) {
      setNewPassword2(e.target.value)
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
  
            <PasswordField
              password = {newPassword1}
              handlePassword = {handleNewPassword1}
              id = "newPassword1"
              labelText="New password"
            />
  
            <PasswordField
              password = {newPassword2}
              handlePassword = {handleNewPassword2}
              id = "newPassword2"
              labelText="Re-enter new password"
            />
  
            <button>Submit</button>
        </form>
      </div>
    )
}

export default PasswordChangeForm