import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import handleText from "../../../functions/handlers/handleText"
import EmailField from "../../Input fields/EmailField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import '../../../sass/Components/account/Password reset/PasswordResetForm.scss'

function PasswordResetForm({onDoneChange}: {onDoneChange:Function}) {
    const domain = window.location.origin + "/account/"
    const [email, setEmail] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/password-reset/', {
            email: email,
            domain: domain
        })
        .then(
            onDoneChange(true)
        )
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }
  
    return (
      <div className="passwordReset-form">
        <form onSubmit={(e) => submit(e)}>
          <EmailField
            id='email'
            email={email}
            labelText='Email'
            handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setEmail)}
          />
          <div className="email-spacer"></div>

          <SubmitBtn
            value="Reset Password"
          />
        </form>
      </div>
    )
}

export default PasswordResetForm