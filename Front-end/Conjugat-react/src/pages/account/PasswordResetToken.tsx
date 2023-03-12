import { useState } from "react"
import Header from "../../components/account/Header"
import Authorization from '../../components/functions/Authorization'
import EmailDone from "../../components/account/Password reset/EmailDone"
import PasswordChange from "../../components/account/Password reset token/PasswordChange"

function PasswordResetToken() {
  Authorization.NotAuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <Header />
        <h1>Password Change</h1>

        <PasswordChange
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else {
    return (
      <div>
        <Header />
        <h1>Change email done</h1>

        <EmailDone />
      </div>
    )
  }
}



export default PasswordResetToken