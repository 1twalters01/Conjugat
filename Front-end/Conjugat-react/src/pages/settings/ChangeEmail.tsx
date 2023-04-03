import { useState } from "react"
import Authorization from '../../functions/Authorization'
import EmailChanged from "../../components/settings/Change email/EmailChanged"
import EmailChangeForm from "../../components/settings/Change email/EmailChangeForm"
import SettingsLinks from "../../components/settings/SettingsLinks"
import '../../sass/pages/settings/ChangeEmail.scss'

function ChangeEmail() {
    Authorization.AuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <div className="Change-email-container">
                <div className="lhs container">
                    <SettingsLinks />
                </div>
                
                <div className="rhs container">
                    <div className="Header-spacer">
                        <h1 className="text">Change email</h1>
                    </div>
                    
                    <div className="form-spacer">
                        <EmailChangeForm
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
                <h1>Change email done</h1>

                <EmailChanged />
            </div>
        )
    }
}

export default ChangeEmail