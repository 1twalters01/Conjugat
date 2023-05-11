import { ChangeEvent, FormEvent, useState, } from "react"
import { useDispatch, useSelector } from "react-redux"
import { toast } from "react-toastify"
import { RootState } from "../../../redux/store"
import { onThemeChange } from "../../../redux/slices/themeSlice"
import { onLanguageChange } from "../../../redux/slices/languageSlice"
import axios from "axios"
import AxiosInstance from '../../../functions/AxiosInstance'
import handleText from "../../../functions/handlers/handleText"
import PasswordField from '../../Input fields/PasswordField'
import handleTotp from "../../../functions/handlers/handleTotp"
import TotpField from '../../Input fields/TotpField'
import handleCheckbox from "../../../functions/handlers/handleCheckbox"
import RememberMeField from '../../Input fields/RememberMeField'
import PasswordReset from './PasswordReset'
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from "../../../functions/getTranslation"
import { PasswordFormTranslation } from "../../../content/account/Login"
import '../../../sass/Components/account/Login/PasswordForm.scss'

function PasswordForm({language}:{language:string}) {
    const dispatch = useDispatch()
    const { confirmed } = useSelector((state: RootState) => state.persistedReducer.login)
    const { username } = useSelector((state: RootState) => state.persistedReducer.login)
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')
    const [rememberMe, setRememberMe] = useState(false)

    async function get_theme(token:string){
        const result = await(
            AxiosInstance.Authorised
            .get ('settings/themes/', {
                headers: {
                    'Authorization': 'Token '+ localStorage.getItem("token"),
                    'Content-Type': 'application/json',
                    accept: 'application/json',
                }
            })
        )
        dispatch(onThemeChange(result.data.theme))
    }

    async function get_language(token:string){
      const result = await(
          AxiosInstance.Authorised
          .get ('settings/languages/', {
              headers: {
                  'Authorization': 'Token '+ localStorage.getItem("token"),
                  'Content-Type': 'application/json',
                  accept: 'application/json',
              }
          })
      )
      dispatch(onLanguageChange(result.data.language))
  }

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
            localStorage.setItem("token", res.data.token)
            Promise.all([get_theme(res.data.token), get_language(res.data.token)]).then((values) => {
                window.location.href = '/home'
            });
        })
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }

    return (
      <div className="login-form">
        <form onSubmit={(e) => submit(e)}>
            <div className="password-spacer">
                <PasswordField
                  password = {password}
                  handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword)}
                  id = "password"
                  labelText={getTranslation(PasswordFormTranslation, language, 'Password')}
                />
            </div>

          {confirmed == false ?
            null
          :
            <>
            <div className="totp-spacer">
                <TotpField
                  totp = {totp}
                  handleTotp = {(e:ChangeEvent<HTMLInputElement>) => handleTotp(e, setTotp)}
                  labelText={getTranslation(PasswordFormTranslation, language, 'Totp')}
                />
            </div>
            </>
          }

          <div className="rememberMe-spacer">
              <RememberMeField
                labelText={getTranslation(PasswordFormTranslation, language, 'RememberMe')}
                rememberMe = {rememberMe}
                handleRememberMe = {(e:ChangeEvent<HTMLInputElement>) => handleCheckbox(e, setRememberMe)}
              />
          </div>

          <div className="passwordReset-spacer">
              <PasswordReset linkText={getTranslation(PasswordFormTranslation, language, 'LinkText')} />
          </div>

          <SubmitBtn
            value="Log in"
            style='strong-gold-btn'
          />
      </form>
    </div>
  )
}

export default PasswordForm