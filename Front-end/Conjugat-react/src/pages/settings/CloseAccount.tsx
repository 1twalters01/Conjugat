import { useState} from "react"
import Authorization from '../../components/functions/Authorization'
import AccountDeleted from "../../components/settings/Close account/AccountDeleted"
import AccountDeleteForm from "../../components/settings/Close account/AccountDeleteForm"

function CloseAccount() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Close account</h1>

        <AccountDeleteForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else if (done == true) {
    return (
      <div>
        <h1>Close account</h1>

        <AccountDeleted />
      </div>
    )
  }
}

export default CloseAccount