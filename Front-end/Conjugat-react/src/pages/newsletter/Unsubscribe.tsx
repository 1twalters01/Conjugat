import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'

function Unsubscribe() {
  return (
    <div>
      <h1>Change email</h1>

      <UnsubscribeForm />
    </div>
  )
}

function UnsubscribeForm(){
  const url = "http://conjugat.io:8000/newsletter/unsubscribe/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }

  const [data, setData] = useState({
    email: "",
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      email: data.email,
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
            <label htmlFor="email">Email</label>
            <input id="email" type="text" name="email" value={data.email} onChange={(e) => handle(e)} />
          </div>
          <button>Submit</button>
      </form>
    </div>
  )
}

export default Unsubscribe