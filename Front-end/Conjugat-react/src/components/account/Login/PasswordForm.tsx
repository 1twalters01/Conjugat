import { ChangeEvent, FormEvent, useState, } from "react"
import { useDispatch, useSelector } from "react-redux"
import { toast } from "react-toastify"
import { RootState } from "../../../redux/store"
import { onThemeChange } from "../../../redux/slices/themeSlice"
import AxiosInstance from '../../../functions/AxiosInstance'
import handleText from "../../../functions/handlers/handleText"
import PasswordField from '../../Input fields/PasswordField'
import handleTotp from "../../../functions/handlers/handleTotp"
import TotpField from '../../Input fields/TotpField'
import handleCheckbox from "../../../functions/handlers/handleCheckbox"
import RememberMeField from '../../Input fields/RememberMeField'
import PasswordReset from './PasswordReset'
import SubmitBtn from "../../Input fields/SubmitBtn"
import '../../../sass/Components/account/Login/PasswordForm.scss'


function PasswordForm() {
    const dispatch = useDispatch()
    // const navigate = useNavigate()
    const { confirmed } = useSelector((state: RootState) => state.persistedReducer.login)
    const { username } = useSelector((state: RootState) => state.persistedReducer.login)
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')
    const [rememberMe, setRememberMe] = useState(false)

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Unauthorised
        .post('account/login/password/', {
            username: username,
            password: password,
            totp: totp,
            remember_me: rememberMe
        })
        .then(res=>{
            console.log(res.data.token)
            localStorage.setItem("token", res.data.token)
            dispatch(onThemeChange(res.data.theme))
            window.location.href = ('/home')
        })
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }

    return (
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
          <PasswordField
            password = {password}
            handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword)}
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
                handleTotp = {(e:ChangeEvent<HTMLInputElement>) => handleTotp(e, setTotp)}
                labelText="Totp"
              />
              <div className="totp-bottom-spacer"></div>
            </>
          }

          <RememberMeField
            rememberMe = {rememberMe}
            handleRememberMe = {(e:ChangeEvent<HTMLInputElement>) => handleCheckbox(e, setRememberMe)}
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