import { FormEvent} from "react"
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import AxiosInstance from '../../../functions/AxiosInstance'
import { onThemeChange } from "../../../redux/slices/themeSlice";

function LogoutBtn({onLoggedOutChange} : {onLoggedOutChange:Function}) {
    const dispatch = useDispatch();
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();

      AxiosInstance.Authorised
      .post('/account/logout/')
      .then(res=>{
          localStorage.removeItem('token');
          dispatch(onThemeChange('Dark'))
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