import { useState } from "react"
import Authorization from '../../functions/Authorization'
import EmailChangeForm from "../../components/settings/Change email/EmailChangeForm"
import EmailChanged from "../../components/settings/Change email/EmailChanged"

function ChangeEmail() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Change email</h1>

        <EmailChangeForm
          onDoneChange={setDone}
        />
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