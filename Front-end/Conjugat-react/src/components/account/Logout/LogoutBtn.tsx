import { FormEvent } from "react"
import { useDispatch } from "react-redux";
import AxiosInstance from '../../../functions/AxiosInstance'
import { onThemeChange } from "../../../redux/slices/themeSlice";
import { getTranslation } from "../../../functions/getTranslation"
import { LogoutBtnTranslations } from "../../../content/account/Logout"
import '../../../sass/Components/account/Logout/LogoutBtn.scss'

function LogoutBtn({language, onLoggedOutChange} : {language:string, onLoggedOutChange:Function}) {
    const dispatch = useDispatch();
    
    function submit(e:FormEvent<HTMLButtonElement>) {
      e.preventDefault();
      console.log(localStorage.getItem('token'), 'hiii')
      AxiosInstance.Authorised
      .post('/account/logout/')
      .then(res=>{
          localStorage.removeItem('token');
          dispatch(onThemeChange('Dark'))
          onLoggedOutChange(true)
      })
      .catch(err=>{
          localStorage.removeItem('token');
          console.log(err)
          onLoggedOutChange(true)
      })
    }

    return (
      <button onClick={(e) => submit(e)} className='logout-btn strong-gold-btn'>{getTranslation(LogoutBtnTranslations, language, 'Text')}</button>
    )
  }

export default LogoutBtn