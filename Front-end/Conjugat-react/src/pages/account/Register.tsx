import { useState } from "react"
import { Helmet } from "react-helmet"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import RegisterDoneFalse from "../../components/account/Register/RegisterDoneFalse"
import RegisterDoneTrue from "../../components/account/Register/RegisterDoneTrue"
import RegisterForm from "../../components/account/Register/RegisterForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import '../../sass/pages/account/Register.scss'
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/account/Register"

function Register() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)

    const [done, setDone] = useState(false)
    const [returnedEmail, setReturnedEmail] = useState(null)

    if (done == false) {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title1')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent1')}
                    />
                </Helmet>

                <div className="Register-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>

                    
                    <div className="RegisterLinks-spacer">
                        <RegisterLinks language={language} />
                    </div>
                    
                    <div className="form-width">
                        <RegisterForm
                            language={language}
                            onDoneChange={setDone}
                            setReturnedEmail={setReturnedEmail}
                        />
                    </div>
                    
                    <div className="RegisterForm-spacer"></div>
                </div>
            </>
        )
    }
    else {
        if (returnedEmail == true){
            return (
                <>
                    <Helmet>
                        <title>{getTranslation(translations, language, 'Title2')}</title>
                        <meta name="description"
                            content={getTranslation(translations, language, 'metaContent2')}
                        />
                    </Helmet>

                    <div className="Register-container container">
                        <div className="Header-spacer">
                            <Header language={language} />
                        </div>

                        <div className="Register-done-spacer">
                            <RegisterDoneTrue language={language} />
                        </div>
                    </div>
                </>
            )
        }
        else {
            return (
                <>
                    <Helmet>
                        <title>{getTranslation(translations, language, 'Title3')}</title>
                        <meta name="description"
                            content={getTranslation(translations, language, 'metaContent3')}
                        />
                    </Helmet>
                
                    <div className="Register-container container">
                        <div className="Header-spacer">
                            <Header language={language} />
                        </div>
                        
                        <div className="Register-done-spacer">
                            <RegisterDoneFalse language={language} />
                        </div>
                    
                    </div>
                </>
            )
        }
    }
}

export default Register