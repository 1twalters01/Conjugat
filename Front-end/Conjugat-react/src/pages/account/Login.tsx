import { useState } from "react"
import {Helmet} from "react-helmet-async";
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import AlternateLogins from '../../components/account/Login/AlternateLogins'
import Header from '../../components/account/Header'
import PasswordForm from '../../components/account/Login/PasswordForm'
import ResetUsername from '../../components/account/Login/ResetUsername'
import UsernameForm from '../../components/account/Login/UsernameForm'
import UsernameLinks from '../../components/account/Login/UsernameLinks'
import { getTranslation } from "../../functions/getTranslation";
import { translations } from "../../content/account/Login";
import '../../sass/pages/account/Login-username.scss'
import '../../sass/pages/account/Login-password.scss'

function Login() {
    Authorization.NotAuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [page, setPage] = useState('username')

    if (page == 'username') {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title1')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent1')}
                    />
                    <link rel="canonical" href="/account/login" />
                </Helmet>

                <div className="Login-username-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>

                    <div className="UsernameLinks-spacer">
                        <UsernameLinks language={language} />
                    </div>

                    <div className="form-width">
                        <UsernameForm language={language} onPageChange={setPage} />
                    </div>
                    
                    <div className="UsernameForm-spacer"></div>

                    
                    <div className="AlternameLogins-spacer">
                        <AlternateLogins language={language} />
                    </div>
                </div>
            </>
        )
    }

    if (page == 'password') {
        return (
            <>
                <Helmet>
                    <title>{getTranslation(translations, language, 'Title2')}</title>
                    <meta name="description"
                        content={getTranslation(translations, language, 'metaContent2')}
                    />
                </Helmet>

                <div className="Login-password-container container">
                    <div className="Header-spacer">
                        <Header language={language} />
                    </div>
                    

                    <div className="ResetUsername-spacer form-width">
                        <ResetUsername language={language} onPageChange={setPage} />
                    </div>

                    <div className="form-width">
                        <PasswordForm language={language} />
                    </div>
                </div>
            </>
        )
    }
    return <div></div>
}

export default Login