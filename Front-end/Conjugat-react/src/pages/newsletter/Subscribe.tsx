import { ChangeEvent, FormEvent, useState} from "react"
import Axios from 'axios'

const url = "http://conjugat.io:8000/newsletter/subscribe/"
const token = localStorage.getItem("token")
const headers:any = {
  'Content-Type': 'application/json',
}
if (token) {
  headers['Authorization'] = 'Token '+token
}

var count: number

function Subscribe() {
  count = 0
  return (
    <div>
      <h1>Subscribe</h1>

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
        <SubscribeForm email={email}/>
      </div>
    )
  }
  return(
    <div></div>
  )
}

function SubscribeForm({email} : {email:string}){
  const url = 'http://conjugat.io:8000/newsletter/subscribe/'
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }

  const [data, setData] = useState({
    email: email,
    first_name: "",
    last_name: "",
  })
  const [languages, setLanguage] = useState<string[]>([]);

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      email: data.email,
      first_name: data.first_name,
      last_name: data.last_name,
      languages: languages,
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

  function changeLanguage(e:ChangeEvent<HTMLSelectElement>) {
    if (languages.includes(e.target.value)) {
      setLanguage(languages.filter(languages => languages !== e.target.value ))
    }
    else {
      setLanguage([...languages, e.target.value])
    }
  }

  return(
    <div>
      <form onSubmit={(e) => submit(e)}>
          <div>
            <label htmlFor="email">Email</label>
            <input id="email" type="text" name="email" value={data.email} onChange={(e) => handle(e)} required />
          </div>

          <div>
            <label htmlFor="first_name">First name</label>
            <input id="first_name" type="text" name="first_name" value={data.first_name} onChange={(e) => handle(e)} required />
          </div>
          
          <div>
            <label htmlFor="last_name">Last name</label>
            <input id="last_name" type="text" name="last_name" value={data.last_name} onChange={(e) => handle(e)} />
          </div>
          
          <div>
            <label htmlFor="languages">Languages</label>
            <select name="languages" id="languages" value={languages || []} onChange={(e) => changeLanguage(e)} multiple={true}>
              <option value="English">English</option>
              <option value="French">French</option>
              <option value="Italian">Italian</option>
              <option value="Portuguese">Portuguese</option>
              <option value="Spanish">Spanish</option>
            </select>
          </div>
          <button>Submit</button>
      </form>
    </div>
  )
}

export default Subscribe