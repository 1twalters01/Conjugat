import {useState} from "react"
import { useParams } from 'react-router-dom'
import Axios from 'axios'
import Authorization from '../../Authorization'

function PasswordResetToken() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Password Change</h1>

        <PasswordChange />
      </div>
    )
  }

function PasswordChange() {
  const { uidb64, token } = useParams();
  const url = "http://conjugat.io:8000/account/password-reset/confirm"
  const [data, setData] = useState({
    uidb64: uidb64,
    token: token,
    password: "",
    password2: ""
  })

  function submit(e) {
    e.preventDefault();
    Axios.post(url, {
      uidb64: uidb64,
      token: token,
      password: data.password,
      password2: data.password2,
    })
    .then(
      window.location = '/account/password-reset/done'
    )
  }

  function handle(e) {
    const newdata = { ...data }
    newdata[e.target.id] = e.target.value
    setData(newdata)
  }

  return(
    <form onSubmit={(e) => submit(e)}>
      <div>
        <label htmlFor="password">password</label>
        <input id="password" type="password" name="password" value={data.password} onChange={(e) => handle(e)} />
      </div>
      
      <div>
        <label htmlFor="password2">Repeat your password</label>
        <input id="password2" type="password" name="password2" value={data.password2} onChange={(e) => handle(e)} />
      </div>
      <input type="submit" value="Submit" />
    </form>
  )
}

export default PasswordResetToken