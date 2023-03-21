import { useState } from 'react'
import Authorization from '../../functions/Authorization'
import Header from '../../components/account/Header'
import LogoutAllBtn from '../../components/settings/Logout all/LogoutAllBtn'
import LogoutAllResponse from '../../components/settings/Logout all/LogoutAllResponse'


function LogoutAll() {
  Authorization.AuthRequired()
  const [LoggedOut, SetLoggedOut] = useState(false)
  if (LoggedOut==false) {
    return (
      <div>
        <Header />

        <LogoutAllBtn
          onLoggedOutChange={SetLoggedOut}
        />
      </div>
    )
  }
  else if (LoggedOut==true) {
    return (
      <div>
        <Header />

        <LogoutAllResponse />
      </div>
    )
  }
  return <div></div>
}

export default LogoutAll