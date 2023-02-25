import { ChangeEvent, FormEvent, useState, useEffect} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'
import QRCode from "react-qr-code"
import { useNavigate } from 'react-router'

const url = "http://conjugat.io:8000/settings/two-factor-auth/"
const token = localStorage.getItem("token")
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token '+ token
}
var load: boolean

function TwoFactorAuth() {
  Authorization.AuthRequired()
  load = false
  return (
    <div>
      <h1>TwoFactorAuth</h1>

      <Qrcode />
      <QrForm />
    </div>
  )
}



function Qrcode() {
  const [qrString, setQrString] = useState("")

  useEffect(() => {
    if (load == false) {
      Axios.get(url, {headers: headers})
      .then(
        res => setQrString(res.data.qr_string)
      )
      load = true
    }
  })

  return(
    <div style={{ background: 'white', padding: '10px' }}>
      { qrString == "" ?
      <div style={{ height: '260px'}}></div>
      :
      <QRCode value={qrString} />
      }
      
    </div>
  )
}

function QrForm() {
  const [data, setData] = useState({
    password: "",
    totp: "",
  })

  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    Axios.post(url, {
      password: data.password,
      totp: data.totp,
    },
    {
      headers: headers
    })
    .then(res=>{
      location.reload()
    })
  }

  function handle(e:ChangeEvent<HTMLInputElement>) {
    const newdata = { ...data }
    newdata[e.target.id as keyof typeof data] = e.target.value
    setData(newdata)
  }

  return(
    <form onSubmit={(e) => submit(e)}>
        <div>
          <label htmlFor="password">Password</label>
          <input id="password" type="password" name="password" value={data.password} onChange={(e) => handle(e)} />
        </div>

        <div>
          <label htmlFor="totp">totp</label>
          <input id="totp" type="text" name="totp" value={data.totp} onChange={(e) => handle(e)} />
        </div>

        <button>Submit</button>
    </form>
  )
}

export default TwoFactorAuth