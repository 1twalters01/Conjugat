import { useNavigate } from "react-router-dom"
import { ChangeEvent, FormEvent, useState, } from "react"

import AxiosInstance from '../../../functions/AxiosInstance'
import PasswordField from '../../Input fields/PasswordField'
import TotpField from '../../Input fields/TotpField'
import RememberMeField from '../../Input fields/RememberMeField'
import PasswordReset from '../../Input fields/PasswordReset'

function PasswordForm({username, id, confirmed}: {username:string, id:string, confirmed:boolean|null}) {
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')
    const [rememberMe, setRememberMe] = useState(false)
    const navigate = useNavigate()
    
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handleTotp(e:ChangeEvent<HTMLInputElement>) {
        setTotp(e.target.value)
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
            
            {confirmed == false ?
              null
            :
              <TotpField
                totp = {totp}
                handleTotp = {handleTotp}
              />
            }

            <RememberMeField
              rememberMe = {rememberMe}
              handleRememberMe = {handleRememberMe}
            />

            <PasswordReset />

            <div className="submit">
                <input type="submit" className="strong-btn" value="Submit" />
            </div>
        </form>
      </div>
    )
}


export default PasswordForm