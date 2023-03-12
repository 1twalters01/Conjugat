import { FormEvent} from "react"
import AxiosInstance from '../../functions/AxiosInstance'

function LogoutBtn({onLoggedOutChange} : {onLoggedOutChange:Function}) {
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();

      AxiosInstance.Authorised
      .post('/account/logout/')
      .then(res=>{
          localStorage.removeItem('token');
          onLoggedOutChange(true)
      })
      .catch(err=>{
          console.log(err.response.data.error)
      })
    }

    return (
      <form onSubmit={(e) => submit(e)}>
        <button>Log out</button>
      </form>
    )
  }

export default LogoutBtn