import { FormEvent} from "react"
import Axios from 'axios'
import Authorization from '../../Authorization'

function Logout() {
  Authorization.AuthRequired()
  return (
    <div>
        <h1>Logout</h1>

        <LogoutBtn />
    </div>
  )
}

function LogoutBtn() {
  function submit(e:FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const url = "http://conjugat.io:8000/account/logout/"
    const token = localStorage.getItem("token")
    
    const headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Token '+ token
    }

    Axios.post(url, {},
    {
      headers: headers
    })
    .then(res=>{
      console.log(res.data)
      localStorage.removeItem('token');
      window.location.reload();
    })
  }

  return (
    <form onSubmit={(e) => submit(e)}>
      <button>Log out</button>
    </form>
  )
}

export default Logout