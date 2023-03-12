import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'
import Authorization from '../../components/functions/Authorization'

function CloseAccount() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Close account</h1>

      <AccountForm />
    </div>
  )
}

function AccountForm(){
  const url = "http://conjugat.io:8000/settings/close-account/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }

  const [data, setData] = useState({
    password: "",
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      password: data.password,
    },
    {
      headers: headers
    })
    .then(res=>{
      localStorage.removeItem('token');
      window.location.reload();
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

          <button>Submit</button>
      </form>
    </div>
  )
}

export default CloseAccount