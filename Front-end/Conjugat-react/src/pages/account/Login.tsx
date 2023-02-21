import {useState} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'

function Login() {
  Authorization.NotAuthRequired()
  return (
    <div>
      <h1>Login</h1>
      {localStorage.getItem("id") == null ?
        <UsernameForm />
      :
        <div><ResetUsername /><PasswordForm /></div>
      }
      
      
    </div>
  )
}

function UsernameForm() {
  const url = "http://conjugat.io:8000/account/login/username/"
  const [data, setData] = useState({
    username: ""
  })

  function submit(e) {
    e.preventDefault();
    Axios.post(url, {
      username: data.username
    })
    .then(res=>{
      localStorage.setItem("username", res.data.username);
      localStorage.setItem("id", res.data.id);
      localStorage.setItem("confirmed", res.data.confirmed);
      window.location.reload();
    })
  }

  function handle(e) {
    const newdata = { ...data }
    newdata[e.target.id] = e.target.value
    setData(newdata)
  }

  return(
    <div>
      <form onSubmit={(e) => submit(e)}>
          <label htmlFor="username">Email or Username</label>
          <input id="username" type="text" name="username" value={data.username} onChange={(e) => handle(e)} />
          <button>Submit</button>
        </form>
    </div>
  )
}

function PasswordForm() {
  const url = "http://conjugat.io:8000/account/login/password/"
  const [data, setData] = useState({
    password: "",
    totp: "",
    rememberMe:false
  })

  function submit(e) {
    e.preventDefault();
    Axios.post(url, {
      username: localStorage.getItem("username"),
      id: localStorage.getItem("id"),
      password: data.password,
      totp: data.totp,
      confirmed: localStorage.getItem("confirmed"),
      rememberMe: data.rememberMe
    })
    .then(res=>{
      localStorage.setItem("token", res.data.token);
      localStorage.removeItem('username');
      localStorage.removeItem('id');
      localStorage.removeItem('confirmed');
      window.location.reload();
    })
  }

  function handle(e) {
    const newdata = { ...data }
    newdata[e.target.id] = e.target.value
    setData(newdata)
  }

  return(
    <div>
      <form onSubmit={(e) => submit(e)}>
          <div>
            <label htmlFor="password">Password</label>
            <input id="password" type="password" name="password" value={data.password} onChange={(e) => handle(e)} />
          </div>
          {localStorage.getItem("confirmed") == 'false' ?
            null
          :
            <div>
              <label htmlFor="totp">Totp</label>
              <input id="totp" type="text" name="totp" value={data.totp} onChange={(e) => handle(e)} />
            </div>
          }
          <label htmlFor="rememberMe">remember me</label>
          <input type="checkbox" name="rememberMe" id="rememberMe" checked={data.rememberMe} onChange={(e) => handle(e)} />
          <button>Submit</button>
      </form>
    </div>
  )
}

function ResetUsername() {
  const username = localStorage.getItem("username")
  const id = localStorage.getItem("id")
  const confirmed = localStorage.getItem("confirmed")

  function submit(e) {
    e.preventDefault();
    localStorage.removeItem('username');
    localStorage.removeItem('id');
    localStorage.removeItem('confirmed');
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

export default Login