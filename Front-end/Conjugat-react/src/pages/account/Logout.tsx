import { useState } from 'react'
import Authorization from '../../functions/Authorization'
import Header from '../../components/account/Header'
import LogoutBtn from '../../components/account/Logout/LogoutBtn'
import LogoutResponse from '../../components/account/Logout/LogoutResponse'
import '../../sass/pages/account/Logout.scss'

function Logout() {
  Authorization.AuthRequired()
  const [LoggedOut, SetLoggedOut] = useState(false)
  if (LoggedOut==false) {
    return (
        <div className="Logout-container container">
            <div className="header-spacer">
                <Header />
            </div>
            
            <div className="text-spacer">
                <p className='text'>Are you sure that you want to log out?</p>
            </div>
            
            <div className="logout-spacer">
                <LogoutBtn onLoggedOutChange={SetLoggedOut} />
            </div>
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