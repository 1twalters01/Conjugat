import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../components/functions/Authorization'

function ChangeUsername() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Change username</h1>

        <UsernameForm
          onDoneChange={setDone}
        />
      </div>
    )
  }

  else {
    return (
      <div>
        <h1>Change Password done</h1>

        <UsernameDone />
      </div>
    )
  }
}

function UsernameForm({ onDoneChange }: {onDoneChange:Function}){
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
    .then(
      onDoneChange(true)
    )
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

function UsernameDone() {
  return(
    <div>Email has been updated</div>
  )
}

export default ChangeUsername