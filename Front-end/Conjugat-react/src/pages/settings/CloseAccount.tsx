import { useState} from "react"
import Authorization from '../../functions/Authorization'
import AccountDeleteForm from "../../components/settings/Close account/AccountDeleteForm"

function CloseAccount() {
    Authorization.AuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
      return (
        <div className="rhs container">
            <div className="Header-spacer">
                <h1 className="text">Close account</h1>
            </div>
            
            <div className="form-spacer">
                <AccountDeleteForm
                  onDoneChange={setDone}
                />
            </div>
        </div>
      )
    }
    else if (done == true) {
        return (
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">Close account</h1>
                </div>                

                <div className="para">
                    <p className="text">Account has been successfully deleted</p>
                </div>
            </div>
        )
    }
    return <div></div>
}

export default CloseAccount