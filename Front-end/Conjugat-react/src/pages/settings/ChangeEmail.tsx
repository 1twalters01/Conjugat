import { useState } from "react"
import Authorization from '../../functions/Authorization'
import EmailChangeForm from "../../components/settings/Change email/EmailChangeForm"

function ChangeEmail() {
    Authorization.AuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
        return (        
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
        )
    }
    else {
        return (
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">Change email done</h1>
                </div>                

                <div className="para">
                    <p className="text">Email has been updated.</p>
                </div>
                
            </div>
        )
    }
}

export default ChangeEmail