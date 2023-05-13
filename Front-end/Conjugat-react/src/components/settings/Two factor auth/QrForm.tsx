import { ChangeEvent, FormEvent, useState} from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import { useDispatch } from "react-redux"
import { toast } from "react-toastify"
import { onConfirmedChange } from "../../../redux/slices/loginSlice"
import PasswordField from "../../Input fields/PasswordField"
import TotpField from "../../Input fields/TotpField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import AxiosInstance from "../../../functions/AxiosInstance"
import { getTranslation } from '../../../functions/getTranslation'
import { QrFormTranslations } from '../../../content/settings/TwoFactorAuth'
import '../../../sass/Components/settings/Two factor auth/QrForm.scss'

function QrForm({setDone}: {setDone:Function}) {
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const dispatch = useDispatch()
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')
  
    function submit(e:FormEvent<HTMLFormElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/two-factor-auth/', {
        password: password,
        totp: totp,
      })
      .then(res=>{
        setDone(true)
        console.log(res.data.confirmed, res.data.success)
        dispatch(onConfirmedChange(res.data.confirmed))
      })
      .catch(err => {
        toast.error(err.response.data.error)
      })
    }
  
    function handlePassword(e:ChangeEvent<HTMLInputElement>) {
      setPassword(e.target.value)
    }
    function handleTotp(e:ChangeEvent<HTMLInputElement>) {
        if (isNaN(+e.target.value) == false){
          setTotp(e.target.value)
        }
    }
  
    return(
        <form className="QrForm-container" onSubmit={(e) => submit(e)}>
            <div className="password-spacer">
                <PasswordField
                  id="password"
                  password={password}
                  handlePassword={(e:ChangeEvent<HTMLInputElement>) => handlePassword(e)}
                  labelText={getTranslation(QrFormTranslations, language, 'Password')}
                />
            </div>

            <div className="totp-spacer">
                <TotpField
                totp={totp}
                handleTotp={(e:ChangeEvent<HTMLInputElement>) => handleTotp(e)}
                labelText={getTranslation(QrFormTranslations, language, 'Totp')}
                />
            </div>
    
            <SubmitBtn
              value={getTranslation(QrFormTranslations, language, 'Submit')}
              style="strong-gold-btn"
            />
        </form>
    )
}

export default QrForm