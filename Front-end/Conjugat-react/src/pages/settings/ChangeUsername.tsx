import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'

function ChangeUsername() {
  return (
    <div>
      <h1>Change username</h1>

      <UsernameForm />
    </div>
  )
}

function UsernameForm(){
  const url = "http://conjugat.io:8000/settings/change-username/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }

  const [data, setData] = useState({
    username: "",
    password: "",
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      username: data.username,
      password: data.password,
    },
    {
      headers: headers
    })
    .then(res=>{
      console.log(res.data)
    })
  }

  function handle(e:ChangeEvent<HTMLInputElement>) {
    const newdata = { ...data }
    newdata[e.target.id as keyof typeof data] = e.target.value
    setData(newdata)
  }

  return(
    <div>
      <form onSubmit={(e) => submit(e)}>
          <div>
            <label htmlFor="username">Username</label>
            <input id="username" type="text" name="username" value={data.username} onChange={(e) => handle(e)} />
          </div>

          <div>
            <label htmlFor="password">Password</label>
            <input id="password" type="password" name="password" value={data.password} onChange={(e) => handle(e)} />
          </div>

          <button>Submit</button>
      </form>
    </div>
  )
}

export default ChangeUsername