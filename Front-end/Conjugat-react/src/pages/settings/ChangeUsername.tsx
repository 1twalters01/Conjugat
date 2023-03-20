import { useState } from "react"
import Authorization from '../../functions/Authorization'
import UsernameChanged from "../../components/settings/Change username/UsernameChanged"
import UsernameChangeForm from "../../components/settings/Change username/UsernameChangeForm"

function ChangeUsername() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

  if (done == false) {
    return (
      <div>
        <h1>Change username</h1>

        <UsernameChangeForm
          onDoneChange={setDone}
        />
      </div>
    )
  }
  else if (done == true) {
    return (
      <div>
        <h1>Change Username done</h1>

        <UsernameChanged />
      </div>
    )
  }
  return <div></div>
}

export default ChangeUsername