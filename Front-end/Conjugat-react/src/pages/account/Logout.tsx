import { useState } from 'react'
import { Helmet } from 'react-helmet'
import { useSelector } from 'react-redux'
import { RootState } from '../../redux/store'
import Authorization from '../../functions/Authorization'
import SettingsNavbar from '../../components/settings/SettingsNavbar'
import Header from '../../components/account/Header'
import LogoutBtn from '../../components/account/Logout/LogoutBtn'
import LogoutResponse from '../../components/account/Logout/LogoutResponse'
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/account/Logout"
import '../../sass/pages/account/Logout.scss'

function Logout() {
  Authorization.AuthRequired()
  const { language } = useSelector((state: RootState) => state.persistedReducer.language)
  const [LoggedOut, SetLoggedOut] = useState(false)
  if (LoggedOut==false) {
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
            </Helmet>

            <div className="Settings-navbar-container container">
                <SettingsNavbar language={language} />
            </div>
            
            <div className="Logout-container container">
                <div className="header-spacer">
                    <Header language={language} />
                </div>
                
                <div className="text-spacer">
                    <p className='text'>{getTranslation(translations, language, 'Text')}</p>
                </div>
                
                <div className="logout-spacer">
                    <LogoutBtn language={language} onLoggedOutChange={SetLoggedOut} />
                </div>
            </div>
        </>
        
    )
  }
  
  else if (LoggedOut==true) {
    return (
      <>
          <Helmet>
              <title>{getTranslation(translations, language, 'Title2')}</title>
              <meta name="description"
                  content={getTranslation(translations, language, 'metaContent2')}
              />
          </Helmet>

          <div className="Logout-container container">
              <div className="header-spacer">
                  <Header language={language} />
              </div>
              
              <div className="logout-response-spacer">
                  <LogoutResponse language={language} />
              </div>
          </div>
      </>
    )
  }
  return <div></div>
}

export default Logout