import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../components/functions/Authorization'

function ChangePassword() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Change password</h1>

        <PasswordForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else {
    return (
      <div>
        <h1>Change Password done</h1>

        <PasswordDone />
      </div>
    )
  }
}

function PasswordForm({ onDoneChange }: {onDoneChange:Function}){
  const url = "http://conjugat.io:8000/settings/change-password/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token,
  }
  const [data, setData] = useState({
    password: "",
    newPassword1: "",
    newPassword2: "",
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      password: data.password,
      newPassword1: data.newPassword1,
      newPassword2: data.newPassword2,
    },
    {
      headers: headers
    })
    .then(res=>{
      console.log(res.data)
      onDoneChange(true)
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
            <label htmlFor="password">Password</label>
            <input id="password" type="password" name="password" value={data.password} onChange={(e) => handle(e)} />
          </div>

          <div>
            <label htmlFor="newPassword1"> New password</label>
            <input id="newPassword1" type="text" name="newPassword1" value={data.newPassword1} onChange={(e) => handle(e)} />
          </div>

          <div>
            <label htmlFor="newPassword2">Re-enter new password</label>
            <input id="newPassword2" type="text" name="newPassword2" value={data.newPassword2} onChange={(e) => handle(e)} />
          </div>

          <button>Submit</button>
      </form>
    </div>
  )
}

function PasswordDone() {
  return(
    <div>Password has been updated</div>
  )
}

export default ChangePassword