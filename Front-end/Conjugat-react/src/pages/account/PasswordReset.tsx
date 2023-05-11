import { useState } from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import PasswordResetDone from "../../components/account/Password reset/PasswordResetDone"
import PasswordResetForm from "../../components/account/Password reset/PasswordResetForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import '../../sass/pages/account/PasswordReset.scss'

function PasswordReset() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <div className="PasswordReset-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>
                
                
                <div className="RegisterLinks-spacer">
                    <RegisterLinks />
                </div>
                
                <div className="form-width">
                    <PasswordResetForm onDoneChange={setDone} />
                </div>
            </div>
        )
    }
    else {
        return(
            <div className="PasswordReset-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>
                
                <PasswordResetDone />
            </div>
        )
    }
}

export default PasswordReset