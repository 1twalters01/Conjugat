import { useState } from "react"
import Authorization from '../../functions/Authorization'
import PasswordChanged from "../../components/settings/Change password/PasswordChanged"
import PasswordChangeForm from "../../components/settings/Change password/PasswordChangeForm"
import SettingsLinks from "../../components/settings/SettingsLinks"
import '../../sass/pages/settings/ChangePassword.scss'

function ChangePassword() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
        <div className="Change-password-container">
            <div className="lhs container">
                <SettingsLinks />
            </div>
            
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">Change Password</h1>
                </div>
                
                <div className="form-spacer">
                    <PasswordChangeForm
                      onDoneChange={setDone}
                    />
                </div>
            </div>
        </div>
    )
  }
  else {
    return (
      <div>
        <h1>Change Password done</h1>

        <PasswordChanged />
      </div>
    )
  }
}

export default ChangePassword