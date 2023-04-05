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
          <div className="rhs container">
              <div className="Header-spacer">
                  <h1 className="text">Logout all</h1>
              </div>
              
              <div className="para">
                  <p className='text'>Are you sure that you want to log out of all accounts?</p>
              </div>

              <div className="form-spacer">
                  <LogoutAllBtn
                  onLoggedOutChange={SetLoggedOut}
                  />
              </div>
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