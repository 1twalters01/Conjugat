import { ChangeEvent, FormEvent, useState} from "react"

import AxiosInstance from "../../../functions/AxiosInstance"
import EmailField from "../../Input fields/EmailField"
import SubmitBtn from "../../Input fields/SubmitBtn"

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
        console.log(err.response.data.error)
      })
    }
  
    function handleEmail(e:ChangeEvent<HTMLInputElement>) {
      setEmail(e.target.value)
    }
  
    return (
      <div className="passwordReset-form">
        <form onSubmit={(e) => submit(e)}>
          <EmailField
            id='email'
            email={email}
            labelText='Email'
            handleEmail={handleEmail}
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