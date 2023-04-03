import { useState } from "react"
import Authorization from '../../functions/Authorization'
import UsernameChanged from "../../components/settings/Change username/UsernameChanged"
import UsernameChangeForm from "../../components/settings/Change username/UsernameChangeForm"
import SettingsLinks from "../../components/settings/SettingsLinks"
import '../../sass/pages/settings/ChangeUsername.scss'

function ChangeUsername() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <div className="Change-username-container">
                <div className="lhs container">
                    <SettingsLinks />
                </div>
                
                <div className="rhs container">
                    <div className="Header-spacer">
                        <h1 className="text">Change Username</h1>
                    </div>
                    
                    <div className="form-spacer">
                        <UsernameChangeForm
                        onDoneChange={setDone}
                        />
                    </div>
                </div>
            </div>
        )
    }
    else if (done == true) {
      return (
        <div>
          <h1>Change Username done</h1>

          <UsernameChanged />
        </div>
      )
    }
    return <div></div>
}

export default ChangeUsername