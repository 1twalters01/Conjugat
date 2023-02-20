import {useState} from "react"
import Axios from 'axios'
import { Route, useNavigate } from "react-router-dom"
import Authorization from '../../Authorization'

function Register() {
  Authorization.NotAuthRequired()
  return (
    <div>
      <h1>Register</h1>
      
      <RegisterForm />
    </div>
  )
}

function RegisterForm() {
  const url = "http://conjugat.io:8000/account/register/"
  const [data, setData] = useState({
    username:"",
    email: "",
    password: "",
    password2: ""
  })

  function submit(e) {
    e.preventDefault();
    Axios.post(url, {
      username: data.username,
      email: data.email,
      password: data.password,
      password2: data.password2
    })
    .then(res=>{
      const navigate = useNavigate();
      return navigate('/register/done');
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
        <div>
          <label htmlFor="username">Username</label>
          <input id="username" type="text" name="username" value={data.username} onChange={(e) => handle(e)} />
        </div>
        
        <div>
          <label htmlFor="email">Email</label>
          <input id="email" type="text" name="email" value={data.email} onChange={(e) => handle(e)} />

        </div>
        
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
    </div>
  )
}

export default Register