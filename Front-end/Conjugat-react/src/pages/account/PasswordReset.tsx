import { useState } from "react"

import Header from "../../components/account/Header"
import Authorization from '../../functions/Authorization'
import EmailDone from "../../components/account/Password reset/EmailDone"
import EmailForm from "../../components/account/Password reset/EmailForm"

function PasswordReset() {
  Authorization.NotAuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <Header />
        <h1>Password Reset</h1>
        
        <EmailForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else {
    return(
      <div>
        <Header />

        <EmailDone />
      </div>
    )
  }
}

export default PasswordReset