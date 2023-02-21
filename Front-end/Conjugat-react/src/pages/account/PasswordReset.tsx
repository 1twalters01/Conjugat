import {useState} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'


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
  const [data, setData] = useState({
    email: ""
  })

  function submit(e) {
    e.preventDefault();
    Axios.post(url, {
      email: data.email,
      domain: domain
    })
    .then(res=>{
      window.location = '/account/password-reset/confirm'
    })
  }

  function handle(e) {
    const newdata = { ...data }
    newdata[e.target.id] = e.target.value
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

export default PasswordReset