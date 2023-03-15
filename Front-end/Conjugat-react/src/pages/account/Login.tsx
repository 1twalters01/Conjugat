import { useState } from "react"

import Authorization from '../../functions/Authorization'

import Header from '../../components/account/Header'
import AlternateLogins from '../../components/account/Login/AlternateLogins'
import PasswordForm from '../../components/account/Login/PasswordForm'
import ResetUsername from '../../components/account/Login/ResetUsername'
import UsernameForm from '../../components/account/Login/UsernameForm'
import UsernameLinks from '../../components/account/Login/UsernameLinks'

import '../../sass/pages/account/Login.scss'

function Login() {
  Authorization.NotAuthRequired()
  const [page, setPage] = useState('username')
  const [confirmed, setConfirmed] = useState(null)

  if (page == 'username') {
    return (
      <div className="Login-username-container">
        <div className="Header-spacer-top"></div>
        <Header />
        <div className="Header-spacer-bottom"></div>

        <UsernameLinks />
        <div className="UsernameLinks-spacer"></div>

        <UsernameForm
          onPageChange={setPage}
        />
        <div className="UsernameForm-spacer"></div>

        <AlternateLogins />
      </div>
    )
  }

  if (page == 'password') {
    return(
      <div className="Login-password-container">
        <div className="Header-spacer-top"></div>
        <Header />
        <div className="Header-spacer-bottom"></div>

        <ResetUsername
          onPageChange={setPage}
        />
        <div className="ResetUsername-spacer"></div>

        <PasswordForm/>
        <div className="PasswordForm-spacer"></div>
      </div>
    )
  }
  return <div></div>
}

export default Login