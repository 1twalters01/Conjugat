// import Cookies from "js-cookie"
// import CSRFToken from "../../../functions/CSRFToken"
import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"

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
        toast.error(err.response.data.error)
      })
    }
  
    return(
      <div>
        <form onSubmit={(e) => submit(e)}>
            {/* <CSRFToken /> */}
            <EmailField
              id="email"
              email={email}
              handleEmail={(e:ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
              labelText="Email"
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

export default EmailChangeForm