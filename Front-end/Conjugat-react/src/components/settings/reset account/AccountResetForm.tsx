import { ChangeEvent, FormEvent, useEffect, useState } from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import { toast } from "react-toastify"
import AxiosInstance from "../../../functions/AxiosInstance"
import PasswordField from "../../Input fields/PasswordField"
import TotpField from "../../Input fields/TotpField"
import SubmitBtn from "../../Buttons/SubmitBtn"
import SelectField from "../../Input fields/SelectField"
import { getTranslation } from '../../../functions/getTranslation'
import { AccountResetFormTranslations } from '../../../content/settings/ResetAccount'

function AccountResetForm({ language, onDoneChange }: { language:string, onDoneChange:Function }){
    const { confirmed } = useSelector((state: RootState) => state.persistedReducer.login)
    const [FieldList, setFieldList] = useState<string[]>([])
    const [languages, setLanguage] = useState<string[]>([])
    const [password, setPassword] = useState('')
    const [totp, setTotp] = useState('')

    const fetchdata = async () => {
        const res = await (
            AxiosInstance.Authorised
            .get('settings/reset-account/')
        )
        console.log(res.data.languages)
        setFieldList(res.data.languages)
    }

    useEffect(() => {
        fetchdata()
    }, [])

    function changeLanguage(e:ChangeEvent<HTMLSelectElement>) {
        if (languages.includes(e.target.value)) {
          setLanguage(languages.filter(languages => languages !== e.target.value))
        }
        else {
          setLanguage([...languages, e.target.value])
        }
    }

    function handleTotp(e:ChangeEvent<HTMLInputElement>) {
      if (isNaN(+e.target.value) == false){
        setTotp(e.target.value)
      }
    }

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Authorised
        .post('settings/reset-account/', {
          password: password,
          totp: totp,
          languages: languages,
        })
        .then(res=>{
          onDoneChange(true)
        })
        .catch(err=>{
          toast.error(err.response.data.error)
        })
    }

    return (
        <div className="Close-account-form-container">
            <form onSubmit={(e) => submit(e)}>
                <div className="password-spacer">
                    <SelectField
                    labelText={getTranslation(AccountResetFormTranslations, language, 'Select')}
                    languages={languages}
                    changeLanguage={changeLanguage}
                    FieldList = {FieldList}
                    FieldListValues = {FieldList}
                    />
                </div>

                <div className="password-spacer">
                    <PasswordField
                        password = {password}
                        handlePassword = {(e:ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
                        id = "password"
                        labelText={getTranslation(AccountResetFormTranslations, language, 'Password')}
                    />
                </div>

                {confirmed == false ?
                    null
                :
                    <div className="totp-spacer">
                        <TotpField
                        totp = {totp}
                        handleTotp = {(e:ChangeEvent<HTMLInputElement>) => handleTotp(e)}
                        labelText={getTranslation(AccountResetFormTranslations, language, 'Totp')}
                        />
                    </div>
                }

                <SubmitBtn
                    value={getTranslation(AccountResetFormTranslations, language, 'Submit')}
                    style="strong-red-btn"
                />
            </form>
        </div>
        )
}

export default AccountResetForm