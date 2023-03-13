import { useState } from "react"

import Authorization from '../../functions/Authorization'

import Header from '../../components/account/Header'
import AlternateLogins from '../../components/account/Login/AlternateLogins'
import PasswordForm from '../../components/account/Login/PasswordForm'
import ResetUsername from '../../components/account/Login/ResetUsername'
import UsernameForm from '../../components/account/Login/UsernameForm'
import UsernameLinks from '../../components/account/Login/UsernameLinks'


function Login() {
  Authorization.NotAuthRequired()
  const [page, setPage] = useState('username')
  const [username, setUsername] = useState('')
  const [id, setId] = useState('')
  const [confirmed, setConfirmed] = useState(null)

  if (page == 'username') {
    return (
      <div className="main-container">
        <Header />
        <UsernameLinks />
        <UsernameForm
          onPageChange={setPage}
          username={username}
          onUsernameChange={setUsername}
          onIdChange={setId}
          onConfirmedChange={setConfirmed}
        />
        <AlternateLogins />
      </div>
    )
  }

  if (page == 'password' && username != '') {
    return(
      <div className="main-container">
        <Header />
        <ResetUsername
          onPageChange={setPage}
          onUsernameChange={setUsername}
          onIdChange={setId}
          onConfirmedChange={setConfirmed}
        />
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