import { useState} from "react"
import Authorization from '../../functions/Authorization'
import AccountDeleted from "../../components/settings/Close account/AccountDeleted"
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
      <div>
        <h1>Close account</h1>

        <AccountDeleted />
      </div>
    )
  }
  return <div></div>
}

export default CloseAccount