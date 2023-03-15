import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'

const url = "http://conjugat.io:8000/newsletter/unsubscribe/"
const token = localStorage.getItem("token")
const headers:any = {
  'Content-Type': 'application/json',
}
if (token) {
  headers['Authorization'] = 'Token '+token
}

var count: number

function Unsubscribe() {
  count = 0
  return (
    <div>
      <h1>Unsubscribe</h1>

      <RetrieveStatus />
    </div>
  )
}

function RetrieveStatus() {
  const [email, setEmail] = useState('')
  
  if(count < 2){
    Axios.get(url, {headers: headers})
    .then(res =>{
      if (res.data.email != null) {
        setEmail(res.data.email)
      }
    })
    count += 1
  }
  else{
    return (
      <div>
        <UnsubscribeForm email={email}/>
      </div>
    )
  }
  return(
    <div></div>
  )
}

function UnsubscribeForm({email} : {email:string}){
  const url = "http://conjugat.io:8000/newsletter/unsubscribe/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }
  const [done, setDone] = useState(false)
  const [data, setData] = useState({
    email: email,
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
          <p>You successfully unsubscribed</p>
      </div>
    )
  }
  else{
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
}

export default Unsubscribe