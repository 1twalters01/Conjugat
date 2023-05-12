import { ChangeEvent, FormEvent, useState } from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import handleText from "../../../functions/handlers/handleText"
import TextField from "../../Input fields/TextField"
import EmailField from "../../Input fields/EmailField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from "../../../functions/getTranslation"
import { RegisterFormTranslations } from "../../../content/account/Register"
import '../../../sass/Components/account/Register/RegisterForm.scss'

function RegisterForm({ language, onDoneChange, setReturnedEmail }: {language:string, onDoneChange:Function, setReturnedEmail:Function}) {
    const domain = window.location.origin + "/account/"
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('')
    const [username, setUsername] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        if (password == password2) {
            AxiosInstance.Unauthorised
            .post('account/register/', {
                username: username,
                email: email,
                password: password,
                password2: password2,
                domain: domain
            })
            .then(res=>{
                setReturnedEmail(res.data.email)
                console.log(res.data.email)
                onDoneChange(true)
            })
            .catch(err=>{
                console.log(err.response)
                toast.error(err.response.data.error)
            })
        }
        else {
          toast.error('Passwords do not match')
        }
    }

    return (
      <div className="register-form">
          <form onSubmit={(e) => submit(e)}>
              <div className="username-spacer">
                  <TextField
                  id='username'
                  value = {username}
                  handleText={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setUsername)}
                  labelText = {getTranslation(RegisterFormTranslations, language, 'Username')}
                  required={false}
                  />
              </div>
              
              <div className="email-spacer">
                  <EmailField
                  id='email'
                  email={email}
                  labelText={getTranslation(RegisterFormTranslations, language, 'Email')}
                  handleEmail={(e:ChangeEvent<HTMLInputElement>) => handleText(e, setEmail)}
                  required={false}
                  />
              </div>
              
              <div className="password-spacer">
                  <PasswordField
                    password = {password}
                    handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword)}
                    id = "password"
                    labelText={getTranslation(RegisterFormTranslations, language, 'Password')}
                  />
              </div>
              
              <div className="password-spacer2">
                  <PasswordField
                    password = {password2}
                    handlePassword = {(e:ChangeEvent<HTMLInputElement>) => handleText(e, setPassword2)}
                    id = "password2"
                    labelText={getTranslation(RegisterFormTranslations, language, 'Password2')}
                  />
              </div>
      
              <SubmitBtn
                value={getTranslation(RegisterFormTranslations, language, 'Sign up')}
                style="strong-gold-btn"
              />
          </form>
      </div>
    )
}

export default RegisterForm