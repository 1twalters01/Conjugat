import { useState } from 'react'
import Authorization from '../../functions/Authorization'
import LogoutAllBtn from '../../components/settings/Logout all/LogoutAllBtn'
import { Link } from 'react-router-dom'

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
                  <p className='text'>Are you sure that you want to log out of all accounts, including this one?</p>
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
          <div className="rhs container">
              <div className="Header-spacer">
                  <h1 className="text">Logout all</h1>
              </div>                

              <div className="para">
                  <p className="text">You have been successfully logged out from all devices.</p>
                  <Link to="../login"><div className="register weak-btn">Login</div></Link>
              </div>
          </div>
      )
  }
  return <div></div>
}

export default LogoutAll