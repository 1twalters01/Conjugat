import { useState } from "react"
import Authorization from '../../functions/Authorization'
import PasswordChanged from "../../components/settings/Change password/PasswordChanged"
import PasswordChangeForm from "../../components/settings/Change password/PasswordChangeForm"

function ChangePassword() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Change password</h1>

        <PasswordChangeForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else {
    return (
      <div>
        <h1>Change Password done</h1>

        <PasswordChanged />
      </div>
    )
  }
}

export default ChangePassword