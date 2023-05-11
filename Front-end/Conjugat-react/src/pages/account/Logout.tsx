import { useState } from 'react'
import Authorization from '../../functions/Authorization'
import SettingsNavbar from '../../components/settings/SettingsNavbar'
import Header from '../../components/account/Header'
import LogoutBtn from '../../components/account/Logout/LogoutBtn'
import LogoutResponse from '../../components/account/Logout/LogoutResponse'
import { useSelector } from 'react-redux'
import { RootState } from '../../redux/store'
import '../../sass/pages/account/Logout.scss'

function Logout() {
  Authorization.AuthRequired()
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)
  const [LoggedOut, SetLoggedOut] = useState(false)
  if (LoggedOut==false) {
    return (
        <>
            <div className="Settings-navbar-container container">
                <SettingsNavbar />
            </div>
            
            <div className="Logout-container container">
                <div className="header-spacer">
                    <Header language={language} />
                </div>
                
                <div className="text-spacer">
                    <p className='text'>Are you sure that you want to log out?</p>
                </div>
                
                <div className="logout-spacer">
                    <LogoutBtn onLoggedOutChange={SetLoggedOut} />
                </div>
            </div>
        </>
        
    )
  }
  else if (LoggedOut==true) {
    return (
      <div className="Logout-container container">
        <div className="header-spacer">
            <Header language={language} />
        </div>
        
        <div className="logout-response-spacer">
            <LogoutResponse />
        </div>
      </div>
    )
  }
  return <div></div>
}

export default Logout