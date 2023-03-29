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
                <div className="Header-spacer">
                    <Header />
                </div>

                <div className="UsernameLinks-spacer">
                    <UsernameLinks />
                </div>

                <div className="form-width">
                    <UsernameForm onPageChange={setPage} />
                </div>
                
                <div className="UsernameForm-spacer"></div>

                
                <div className="AlternameLogins-spacer">
                    <AlternateLogins />
                </div>
            </div>          
        )
    }

    if (page == 'password') {
        return (
            <div className="Login-password-container container">
                <div className="Header-spacer">
                    <Header />
                </div>
                

                <div className="ResetUsername-spacer form-width">
                    <ResetUsername onPageChange={setPage} />
                </div>

                <div className="form-width">
                    <PasswordForm/>
                </div>
            </div>
        )
    }
    return <div></div>
}

export default Login