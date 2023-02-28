import { Link } from "react-router-dom"
import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'
import './Login.scss'

function Login() {
  Authorization.NotAuthRequired()
  return (
    <div className="main-container">
      <div className="headings">
        <Link to="../../"><h1>Conjugat</h1></Link>
        <h2>Helping you to perfect your verb conjugations</h2>
      </div>

      {sessionStorage.getItem("id") == null ?
        <div>
          <UsernameLinks />
          <UsernameForm />
          <UsernameSocials />
        </div>
      :
        <div>
          <ResetUsername />
          <PasswordForm />
        </div>
      }
    </div>
  )
}

function UsernameLinks() {
  return (
    <div className="links">
      <Link to="../Register"><div className="link weak-btn">Register</div></Link>
      <Link to="../../Newsletter/subscribe"><div className="link weak-btn">Newsletter</div></Link>
    </div>
  )
}

function UsernameForm() {
  const url = "http://conjugat.io:8000/account/login/username/"
  const [data, setData] = useState({
    username: ""
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      username: data.username
    })
    .then(res=>{
      sessionStorage.setItem("username", res.data.username);
      sessionStorage.setItem("id", res.data.id);
      sessionStorage.setItem("confirmed", res.data.confirmed);
      window.location.reload();
    })
  }

  function handle(e:ChangeEvent<HTMLInputElement>) {
    const newdata = { ...data }
    newdata[e.target.id as keyof typeof data] = e.target.value
    setData(newdata)
  }

  return(
    <div className="login-form">
      <form onSubmit={(e) => submit(e)}>
        <div>
          <p className="field-text"><label htmlFor="username">Email or Username</label></p>
          <input id="username" type="text" name="username" value={data.username} onChange={(e) => handle(e)} />
        </div>

        <div className="submit">
          <button>Submit</button>
        </div>
      </form>
    </div>
  )
}

function UsernameSocials() {
  return (
    <div className="alternatives">
      <p className="options">Or log-in via:</p>
      <div className="alt-login">
        <a href="{% url 'social:begin' 'facebook' %}"><div className="facebook Facebook-btn"><p>Facebook</p></div></a>
        <a href="{% url 'social:begin' 'google-oauth2' %}"><div className="google Google-btn"><p>Google</p></div></a>
        <a href="{% url 'social:begin' 'twitter' %}"><div className="twitter Twitter-btn"><p>Twitter</p></div></a>
      </div>
    </div>
  )
}




function ResetUsername() {
  const username = sessionStorage.getItem("username")
  const id = sessionStorage.getItem("id")
  const confirmed = sessionStorage.getItem("confirmed")

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    sessionStorage.removeItem('username');
    sessionStorage.removeItem('id');
    sessionStorage.removeItem('confirmed');
    window.location.reload();
  }
  return(
    <div>
      <form onSubmit={(e) => submit(e)}>
        <button>Choose a different username</button>
      </form>
    </div>
  )
}

function PasswordForm() {
  const url = "http://conjugat.io:8000/account/login/password/"
  const [data, setData] = useState({
    password: "",
    totp: "",
  })
  const [rememberMe, setRememberMe] = useState(false)

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      username: sessionStorage.getItem("username"),
      id: sessionStorage.getItem("id"),
      password: data.password,
      totp: data.totp,
      confirmed: sessionStorage.getItem("confirmed"),
      remember_me: rememberMe
    })
    .then(res=>{
      localStorage.setItem("token", res.data.token);
      sessionStorage.removeItem('username');
      sessionStorage.removeItem('id');
      sessionStorage.removeItem('confirmed');
      window.location.reload();
    })
  }

  function handle(e:ChangeEvent<HTMLInputElement>) {
    const newdata = { ...data }
    newdata[e.target.id as keyof typeof data] = e.target.value
    setData(newdata)
  }
  function handleChecked(e:ChangeEvent<HTMLInputElement>) {
    setRememberMe(e.target.checked)
    console.log(rememberMe, e.target.checked)
  }

  return(
    <div>
      <form onSubmit={(e) => submit(e)}>
          <div>
            <label htmlFor="password">Password</label>
            <input id="password" type="password" name="password" value={data.password} onChange={(e) => handle(e)} />
          </div>
          {sessionStorage.getItem("confirmed") == 'false' ?
            null
          :
            <div>
              <label htmlFor="totp">Totp</label>
              <input id="totp" type="text" name="totp" value={data.totp} onChange={(e) => handle(e)} />
            </div>
          }
          <label htmlFor="rememberMe">remember me</label>
          <input type="checkbox" name="rememberMe" id="rememberMe" checked={rememberMe} onChange={(e) => handleChecked(e)} />
          
          <div className="password-reset">
            <Link to="../password-reset">
              Forgotten your password?
            </Link>
          </div>

          <button>Submit</button>
      </form>
    </div>
  )
}

export default Login