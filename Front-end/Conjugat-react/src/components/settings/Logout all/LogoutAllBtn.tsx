import { FormEvent } from "react"
import { useDispatch } from "react-redux";
import AxiosInstance from '../../../functions/AxiosInstance'
import { onThemeChange } from "../../../redux/slices/themeSlice";

function LogoutAllBtn({onLoggedOutChange} : {onLoggedOutChange:Function}) {
    const dispatch = useDispatch();
    
    function submit(e:FormEvent<HTMLButtonElement>) {
      e.preventDefault();
      console.log(localStorage.getItem('token'), 'hiii')
      AxiosInstance.Authorised
      .post('/settings/logout-all/')
      .then(res=>{
          localStorage.removeItem('token');
          dispatch(onThemeChange('Dark'))
          onLoggedOutChange(true)
      })
      .catch(err=>{
          console.log(err)
      })
    }

    return (
      <button onClick={(e) => submit(e)}>Log out</button>
    )
  }

export default LogoutAllBtn