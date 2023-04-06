import { useState } from "react"
import Authorization from '../../functions/Authorization'
import PasswordChangeForm from "../../components/settings/Change password/PasswordChangeForm"

function ChangePassword() {
    Authorization.AuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
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
        )
    }
    else {
        return (
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">Change Password done</h1>
                </div>                

                <div className="para">
                    <p className="text">Password has been updated</p>
                </div>
                
            </div>
        )
    }
}

export default ChangePassword