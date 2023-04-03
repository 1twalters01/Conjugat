import { ChangeEvent, FormEvent, useState} from "react"
import { useSelector } from "react-redux";
import { toast } from "react-toastify";
import AxiosInstance from "../../../functions/AxiosInstance";
import { RootState } from "../../../redux/store";
import PasswordField from "../../Input fields/PasswordField"
import SubmitBtn from "../../Buttons/SubmitBtn";
import TotpField from "../../Input fields/TotpField";
import '../../../sass/Components/settings/Close account/AccountDeleteForm.scss'

function AccountDeleteForm({ onDoneChange }: {onDoneChange:Function}){
    const { confirmed } = useSelector((state: RootState) => state.persistedReducer.login)
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')

    function handleTotp(e:ChangeEvent<HTMLInputElement>) {
      if (isNaN(+e.target.value) == false){
        setTotp(e.target.value)
      }
    }

    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/close-account/', {
        password: password,
        totp: totp
      })
      .then(res=>{
        localStorage.removeItem('token');
        onDoneChange(true)
      })
      .catch(err=>{
        toast.error(err.response.data.error)
      })
    }
  
    return(
      <div className="Close-account-form-container">
          <form onSubmit={(e) => submit(e)}>
              <div className="password-spacer">
                  <PasswordField
                    password = {password}
                    handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
                    id = "password"
                    labelText="Password"
                  />
              </div>

              {confirmed == false ?
                null
              :
                  <div className="totp-spacer">
                      <TotpField
                      totp = {totp}
                      handleTotp = {(e:ChangeEvent<HTMLInputElement>) => handleTotp(e)}
                      labelText="Totp"
                      />
                  </div>
              }

              <SubmitBtn
                value="Delete account"
                style="strong-red-btn"
              />
          </form>
      </div>
    )
}

export default AccountDeleteForm