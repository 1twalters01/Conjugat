import { useState } from "react"
import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Header from "../../components/account/Header"
import Authorization from '../../functions/Authorization'
import PasswordResetTokenDone from "../../components/account/Password reset token/PasswordResetTokenDone"
import PasswordChangeForm from "../../components/account/Password reset token/PasswordChangeForm"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/account/PasswordResetToken"
import '../../sass/pages/account/PasswordResetToken.scss'

function PasswordResetToken() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title1')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent1')}
                    />
                </Helmet>

                <div className="Password-change-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>
                    
                    <div className="Title-spacer">
                        <h1 className="blue-text">{getTranslation(translations, language, 'Text')}</h1>
                    </div>

                    <div className="form-width">
                        <PasswordChangeForm
                        language={language}
                        onDoneChange={setDone}
                        />
                    </div>
                </div>
            </>
        )
    }
    else {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title2')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent2')}
                    />
                </Helmet>

                <div className="Password-change-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>

                    <div className="password-reset-token-spacer">
                        <PasswordResetTokenDone language={language} />
                    </div>
                </div>
            </>
        )
      }
}



export default PasswordResetToken