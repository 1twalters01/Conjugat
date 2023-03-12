import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../components/functions/Authorization'

function ChangeEmail() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Change email</h1>

        <EmailForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else {
    return (
      <div>
        <h1>Change email done</h1>

        <EmailDone />
      </div>
    )
  }
}

function EmailForm({ onDoneChange }: {onDoneChange:Function}){
  const url = "http://conjugat.io:8000/settings/change-email/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }
  
  const [data, setData] = useState({
    email: "",
    password: "",
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      email: data.email,
      password: data.password,
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
            <label htmlFor="email">Email</label>
            <input id="email" type="text" name="email" value={data.email} onChange={(e) => handle(e)} />
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

function EmailDone() {
  return(
    <div>Email has been updated</div>
  )
}

export default ChangeEmail