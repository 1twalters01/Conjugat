import { useState } from 'react'

import Authorization from '../../functions/Authorization'

import Header from '../../components/account/Header'
import LogoutBtn from '../../components/account/Logout/LogoutBtn'
import LogoutResponse from '../../components/account/Logout/LogoutResponse'


function Logout() {
  Authorization.AuthRequired()
  const [LoggedOut, SetLoggedOut] = useState(false)
  if (LoggedOut==false) {
    return (
      <div>
        <Header />

        <LogoutBtn
          onLoggedOutChange={SetLoggedOut}
        />
      </div>
    )
  }
  else if (LoggedOut==true) {
    return (
      <div>
        <Header />

        <LogoutResponse />
      </div>
    )
  }
  return <div></div>
}



export default Logout