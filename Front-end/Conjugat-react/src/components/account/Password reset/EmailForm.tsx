import { ChangeEvent, FormEvent, useState} from "react"

import AxiosInstance from "../../functions/AxiosInstance"
import EmailField from "../../Input fields/EmailField"

function EmailForm({onDoneChange}: {onDoneChange:Function}) {
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
      <div>
        <form onSubmit={(e) => submit(e)}>
          <EmailField
            email={email}
            handleEmail={handleEmail}
          />
          
          <div className="submit">
            <input type="submit" className="strong-btn" value="Submit" />
          </div>
        </form>
      </div>
    )
  }

export default EmailForm