import { useState } from "react"
import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import PasswordResetDone from "../../components/account/Password reset/PasswordResetDone"
import PasswordResetForm from "../../components/account/Password reset/PasswordResetForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/account/PasswordReset"
import '../../sass/pages/account/PasswordReset.scss'

function PasswordReset() {
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

                <div className="PasswordReset-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>
                    
                    
                    <div className="RegisterLinks-spacer">
                        <RegisterLinks language={language} />
                    </div>
                    
                    <div className="form-width">
                        <PasswordResetForm language={language} onDoneChange={setDone} />
                    </div>
                </div>
            </>
        )
    }
    else {
        return(
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title2')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent2')}
                    />
                </Helmet>

                <div className="PasswordReset-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>
                    
                    <PasswordResetDone language={language} />
                </div>
            </>
        )
    }
}

export default PasswordReset