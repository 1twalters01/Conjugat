import { useState } from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Header from "../../components/account/Header"
import Authorization from '../../functions/Authorization'
import PasswordResetTokenDone from "../../components/account/Password reset token/PasswordResetTokenDone"
import PasswordChangeForm from "../../components/account/Password reset token/PasswordChangeForm"
import { getTranslation } from "../../functions/getTranslation"
import { Translations } from "../../content/account/PasswordResetToken"
import '../../sass/pages/account/PasswordResetToken.scss'

function PasswordResetToken() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <div className="Password-change-container container">
                <div className="Header-spacer">
                    <Header language={language} />
                </div>
                
                <div className="Title-spacer">
                    <h1 className="blue-text">{getTranslation(Translations, language, 'Text')}</h1>
                </div>

                <div className="form-width">
                    <PasswordChangeForm
                    language={language}
                    onDoneChange={setDone}
                    />
                </div>
            </div>
        )
    }
    else {
        return (
          <div className="Password-change-container container">
              <div className="Header-spacer">
                  <Header language={language} />
              </div>

              <div className="password-reset-token-spacer">
                  <PasswordResetTokenDone language={language} />
              </div>
          </div>
        )
      }
}



export default PasswordResetToken