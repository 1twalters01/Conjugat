import { ChangeEvent, FormEvent, useState } from "react"
import { useParams, Link } from 'react-router-dom'
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
  const [done, setDone] = useState(false)
  const [data, setData] = useState({
    uidb64: uidb64,
    token: token,
    password: "",
    password2: ""
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      uidb64: uidb64,
      token: token,
      password: data.password,
      password2: data.password2,
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
        <h1>Registration Done</h1>

        <div>
          <p>Your password has successfully been reset.</p>
          <Link to="../login"><div>Login</div></Link>
        </div>
      </div>
    )
  }
  else{
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
}

export default PasswordResetToken