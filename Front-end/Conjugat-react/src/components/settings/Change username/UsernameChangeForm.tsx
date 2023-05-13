import { ChangeEvent, FormEvent, useState} from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import TextField from "../../Input fields/TextField"
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import { getTranslation } from '../../../functions/getTranslation'
import { UsernameChangeFormTranslations } from '../../../content/settings/ChangeUsername'
import '../../../sass/Components/settings/Change username/UsernameChangeForm.scss'

function UsernameChangeForm({ language, onDoneChange }: { language:string, onDoneChange:Function }){
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/change-username/', {
        username: username,
        password: password,
      })
      .then(res=>{
        onDoneChange(true)
      })
      .catch(err=>{
        toast.error(err.response.data.error)
      })
    }
  
    return(
      <div className="Username-change-form-container">
        <form onSubmit={(e) => submit(e)}>
            <div className="username-spacer">
                <TextField
                id = "username"
                labelText={getTranslation(UsernameChangeFormTranslations, language, 'Username')}
                value = { username }
                handleText = {(e:ChangeEvent<HTMLInputElement>) => setUsername(e.target.value)}
                required = {true}
                />
            </div>
            
  
            <div className="password-spacer">
                <PasswordField
                password = {password}
                handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
                id = "password"
                labelText={getTranslation(UsernameChangeFormTranslations, language, 'Password')}
                />
            </div>
  
            <SubmitBtn
              value={getTranslation(UsernameChangeFormTranslations, language, 'Submit')}
              style="strong-gold-btn"
            />
        </form>
      </div>
    )
}

export default UsernameChangeForm