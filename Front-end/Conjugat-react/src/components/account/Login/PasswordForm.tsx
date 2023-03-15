import { useNavigate } from "react-router-dom"
import { ChangeEvent, FormEvent, useState, } from "react"

import AxiosInstance from '../../../functions/AxiosInstance'
import PasswordField from '../../Input fields/PasswordField'
import TotpField from '../../Input fields/TotpField'
import RememberMeField from '../../Input fields/RememberMeField'
import PasswordReset from './PasswordReset'
import SubmitBtn from "../../Input fields/SubmitBtn"

import '../../../sass/Components/account/Login/PasswordForm.scss'
import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"

function PasswordForm() {
    const{ username } = useSelector((state: RootState) => state.login)
    const{ id } = useSelector((state: RootState) => state.login)
    const{ confirmed } = useSelector((state: RootState) => state.login)
    
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')
    const [rememberMe, setRememberMe] = useState(false)
    const navigate = useNavigate()
    
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handleTotp(e:ChangeEvent<HTMLInputElement>) {
        if (isNaN(+e.target.value) == false){
          setTotp(e.target.value)
        }
    }
    function handleRememberMe(e:ChangeEvent<HTMLInputElement>) {
        setRememberMe(e.target.checked)
    }
  
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        
        AxiosInstance.Unauthorised
        .post('account/login/password/', {
            username: username,
            id: id,
            confirmed: confirmed,
            password: password,
            totp: totp,
            remember_me: rememberMe
        })
        .then(res=>{
            localStorage.setItem("token", res.data.key);
            navigate('/home')
        })
        .catch(err=>{
          console.log(err.response.data.error)
        })
    }

    return (
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
            <PasswordField
              password = {password}
              handlePassword = {handlePassword}
              id = "password"
              labelText="Password"
            />
            <div className="password-spacer"></div>

            {confirmed == false ?
              null
            :
              <>
              <div className="totp-top-spacer"></div>
                <TotpField
                  totp = {totp}
                  handleTotp = {handleTotp}
                />
                <div className="totp-bottom-spacer"></div>
              </>
            }

            <RememberMeField
              rememberMe = {rememberMe}
              handleRememberMe = {handleRememberMe}
            />
            <div className="rememberMe-spacer"></div>

            <PasswordReset />
            <div className="passwordReset-spacer"></div>

            <SubmitBtn
              value="Submit"
            />
        </form>
      </div>
    )
}


export default PasswordForm