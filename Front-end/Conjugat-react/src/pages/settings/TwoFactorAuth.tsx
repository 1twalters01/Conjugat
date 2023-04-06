import { useState } from "react"
import LoadTwoFactorAuth from "../../components/settings/Two factor auth/LoadTwoFactorAuth";
import Authorization from '../../functions/Authorization'


function TwoFactorAuth() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)
  if (done == false) {
    return (
        <div className="rhs container">
            <div className="Header-spacer">
                <h1 className="text">Two Factor Authentication</h1>
            </div>
            
            <div className="form-spacer">
                  <LoadTwoFactorAuth
                  setDone={setDone}
                  />
              </div>
        </div>
    )
  }
  return (
    <div className="rhs container">
        <div className="Header-spacer">
            <h1 className="text">Two Factor Authentication</h1>
        </div>                

        <div className="para">
            <p className="text">Two factor authentication activation successful.</p>
        </div>
        
    </div>
  )
}

export default TwoFactorAuth