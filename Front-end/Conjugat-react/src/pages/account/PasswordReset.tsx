import { useState } from "react"
import Authorization from '../../functions/Authorization'
import Header from "../../components/account/Header"
import PasswordResetDone from "../../components/account/Password reset/PasswordResetDone"
import PasswordResetForm from "../../components/account/Password reset/PasswordResetForm"
import RegisterLinks from "../../components/account/Register/RegisterLinks"
import '../../sass/pages/account/PasswordReset.scss'

function PasswordReset() {
    Authorization.NotAuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
          <div className="PasswordReset-container">
            <div className="Header-spacer-top"></div>
            <Header />
            <div className="Header-spacer-bottom"></div>

            <RegisterLinks />
            <div className="RegisterLinks-spacer"></div>
            
            <PasswordResetForm
            onDoneChange={setDone}
            />
            <div className="PasswordResetForm-spacer"></div>
          </div>
        )
    }
    else {
        return(
          <div>
            <div className="Header-spacer-top"></div>
            <Header />
            <div className="Header-spacer-bottom"></div>

            <PasswordResetDone />
          </div>
        )
    }
}

export default PasswordReset