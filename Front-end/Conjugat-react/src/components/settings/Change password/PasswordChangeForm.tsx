import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"

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
        toast.error(err.response.data.error)
      })
    }

    return(
      <div>
        <form onSubmit={(e) => submit(e)}>
            <PasswordField
              password = {password}
              handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
              id = "password"
              labelText="Password"
            />
  
            <PasswordField
              password = {newPassword1}
              handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setNewPassword1(e.target.value)}
              id = "newPassword1"
              labelText="New password"
            />
  
            <PasswordField
              password = {newPassword2}
              handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setNewPassword2(e.target.value)}
              id = "newPassword2"
              labelText="Re-enter new password"
            />
  
            <SubmitBtn
              value="Submit"
            />
        </form>
      </div>
    )
}

export default PasswordChangeForm