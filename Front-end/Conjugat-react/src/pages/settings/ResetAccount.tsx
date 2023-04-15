import { useState } from "react"
import Authorization from "../../functions/Authorization"
import SettingsLinks from "../../components/settings/SettingsLinks"
import '../../sass/pages/settings/ResetAccount.scss'
import AccountResetForm from "../../components/settings/reset account/AccountResetForm"

function ResetAccount() {
    Authorization.AuthRequired()
    const [done, setDone] = useState(false)
    if (done == false) {
        return (
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">Reset account</h1>
                </div>
                
                <div className="form-spacer">
                    <AccountResetForm
                    onDoneChange={setDone}
                    />
                </div>
            </div>
        )
    }
    return (
        <div className="rhs container">
            <div className="Header-spacer">
                <h1 className="text">Reset account</h1>
            </div>                
    
            <div className="para">
                <p className="text">Your account has been reset successfully</p>
            </div>
            
        </div>
    )
}

export default ResetAccount