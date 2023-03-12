import { FormEvent } from "react"
import Axios from 'axios'
import Authorization from '../../components/functions/Authorization'

function Themes() {
  Authorization.AuthRequired()
  return (
    <div>
      <h1>Theme</h1>
    
      <Test />
    </div>
  )
}

function Test() {
  const url = "http://conjugat.io:8000/settings/themes/"
  const token = localStorage.getItem("token")
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+ token
  }

  function submitDark(e:FormEvent<HTMLDivElement>) {
    e.preventDefault();
    Axios.post(url, {
      choice: 'Dark'
    },
    {
      headers: headers
    })
    .then(res=>{
      location.reload()
    })
  }
  
  function submitLight(e:FormEvent<HTMLDivElement>) {
    e.preventDefault();
    Axios.post(url, {
      choice: 'Dark'
    },
    {
      headers: headers
    })
    .then(res=>{
      location.reload()
    })
  }

  return(
    <div>
      <div onClick={(e) => submitDark(e)} style={{height: '200px', width: '200px', background: 'black'}}>
      
      </div>



      <div onClick={(e) => submitLight(e)} style={{height: '200px', width: '200px', background: 'yellow'}}>

      </div>
    </div>
  )
}
export default Themes