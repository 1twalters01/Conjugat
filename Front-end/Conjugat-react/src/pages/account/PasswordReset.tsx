import Axios from 'axios'
import { Link } from 'react-router-dom'
import Authorization from '../../components/functions/Authorization'
import { ChangeEvent, FormEvent, useState} from "react"


function PasswordReset() {
  Authorization.NotAuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Password Reset</h1>
        
        <EmailForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else {
    <EmailDone />
  }
}

function EmailForm({onDoneChange}: {onDoneChange:Function}) {
  const url = "http://conjugat.io:8000/account/password-reset/"
  const domain = window.location.origin + "/account/"
  const [data, setData] = useState({
    email: ""
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      email: data.email,
      domain: domain
    })
    .then(res=>{
      onDoneChange(true)
    })
  }

  function handle(e:ChangeEvent<HTMLInputElement>) {
    const newdata = { ...data }
    newdata[e.target.id as keyof typeof data] = e.target.value
    setData(newdata)
  }

  return (
    <div>
      <form onSubmit={(e) => submit(e)}>
        <label htmlFor="email">Email</label>
        <input id="email" type="text" name="email" value={data.email} onChange={(e) => handle(e)} />
        <input type="submit" value="Submit" />
      </form>
    </div>
  )
}

function EmailDone() {
  return(
    <div>
      <h1>Password Confirmation</h1>

      <div>
          <p>We've emailed you instructions for setting your password.</p>
          <p>If you don't receive an email, please make sure you've entered the address you registered with.</p>
          <Link to="../login"><div>Login</div></Link>
      </div>
    </div>
  )
}

export default PasswordReset