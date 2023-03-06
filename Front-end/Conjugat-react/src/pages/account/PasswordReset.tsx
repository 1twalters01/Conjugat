import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'
import { Link } from "react-router-dom"


function PasswordReset() {
  Authorization.NotAuthRequired()
  return (
    <div>
      <h1>Password Reset</h1>
      
      <EmailForm />
    </div>
  )
}

function EmailForm() {
  const url = "http://conjugat.io:8000/account/password-reset/"
  const domain = window.location.origin + "/account/"
  const [done, setDone] = useState(false)
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
      setDone(true)
    })
  }

  function handle(e:ChangeEvent<HTMLInputElement>) {
    const newdata = { ...data }
    newdata[e.target.id as keyof typeof data] = e.target.value
    setData(newdata)
  }

  if (done == true) {
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
  else{
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
}

export default PasswordReset