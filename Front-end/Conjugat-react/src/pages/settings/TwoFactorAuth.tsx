import { useState } from "react"
import LoadTwoFactorAuth from "../../components/settings/Two factor auth/LoadTwoFactorAuth";
import Authorization from '../../functions/Authorization'
import SettingsLinks from "../../components/settings/SettingsLinks";
import '../../sass/pages/settings/TwoFactorAuth.scss'

function TwoFactorAuth() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)
  if (done == false) {
    return (
        <div className="Two-factor-container">
            <div className="lhs container">
                <SettingsLinks />
            </div>
            
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
        </div>
    )
  }
  return (
    <p>Two factor authentication activation successful</p>
  )
}

export default TwoFactorAuth