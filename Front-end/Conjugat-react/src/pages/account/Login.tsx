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
  const [username, setUsername] = useState('')
  const [id, setId] = useState('')
  const [confirmed, setConfirmed] = useState(null)

  if (page == 'username') {
    return (
      <div className="Login-container">
        <div className="Header-spacer-top"></div>
        <Header />
        <div className="Header-spacer-bottom"></div>

        <UsernameLinks />
        <div className="UsernameLinks-spacer"></div>

        <UsernameForm
          onPageChange={setPage}
          username={username}
          onUsernameChange={setUsername}
          onIdChange={setId}
          onConfirmedChange={setConfirmed}
        />
        <div className="UsernameForm-spacer"></div>

        <AlternateLogins />
      </div>
    )
  }

  if (page == 'password' && username != '') {
    return(
      <div className="Login-container">
        <div className="Header-spacer-top"></div>
        <Header />
        <div className="Header-spacer-bottom"></div>

        <ResetUsername
          onPageChange={setPage}
          onUsernameChange={setUsername}
          onIdChange={setId}
          onConfirmedChange={setConfirmed}
        />
        <div className="ResetUsername-spacer"></div>

        <PasswordForm
          username={username}
          id={id}
          confirmed={confirmed}
        />
        
      </div>
    )
  }
  return <div></div>
}

export default Login