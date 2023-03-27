import { useState } from "react"
import Header from "../../components/account/Header"
import Authorization from '../../functions/Authorization'
import EmailDone from "../../components/account/Password reset/PasswordResetDone"
import PasswordChangeForm from "../../components/account/Password reset token/PasswordChangeForm"
import '../../sass/pages/account/PasswordResetToken.scss'

function PasswordResetToken() {
    Authorization.NotAuthRequired()
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <div className="Password-change-container container">
                <div className="Header-spacer-top"></div>
                <Header />
                <div className="Header-spacer-bottom"></div>

                <h1 className="blue-text">Change Password</h1>
                <div className="Title-spacer"></div>

                <div className="form-width">
                    <PasswordChangeForm
                    onDoneChange={setDone}
                    />
                </div>
                <div className="PasswordChangeForm-spacer"></div>
            </div>
        )
    }
    else {
        return (
          <div>
            <div className="Header-spacer-top"></div>
            <Header />
            <div className="Header-spacer-bottom"></div>

            <h1>Change email done</h1>

            <EmailDone />
          </div>
        )
      }
}



export default PasswordResetToken