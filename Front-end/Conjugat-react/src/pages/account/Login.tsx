import { useState } from "react"
import Authorization from '../../functions/Authorization'
import AlternateLogins from '../../components/account/Login/AlternateLogins'
import Header from '../../components/account/Header'
import PasswordForm from '../../components/account/Login/PasswordForm'
import ResetUsername from '../../components/account/Login/ResetUsername'
import UsernameForm from '../../components/account/Login/UsernameForm'
import UsernameLinks from '../../components/account/Login/UsernameLinks'
import '../../sass/pages/account/Login-username.scss'
import '../../sass/pages/account/Login-password.scss'

function Login() {
    Authorization.NotAuthRequired()
    const [page, setPage] = useState('username')

    if (page == 'username') {
        return (
            <div className="Login-username-container container">
                <div className="Header-spacer-top"></div>
                <Header />
                <div className="Header-spacer-bottom"></div>

                <UsernameLinks />
                <div className="UsernameLinks-spacer"></div>

                <div className="form-width">
                    <UsernameForm onPageChange={setPage} />
                </div>
                
                <div className="UsernameForm-spacer"></div>

                <AlternateLogins />
                <div className="UsernameForm-spacer"></div>
            </div>          
        )
    }

    if (page == 'password') {
        return (
            <div className="Login-password-container container">
                <div className="Header-spacer-top"></div>
                <Header />
                <div className="Header-spacer-bottom"></div>

                <div className="form-width">
                    <ResetUsername onPageChange={setPage} />
                </div>
                <div className="ResetUsername-spacer"></div>

                <div className="form-width">
                    <PasswordForm/>
                </div>
                <div className="PasswordForm-spacer"></div>
            </div>
        )
    }
    return <div></div>
}

export default Login