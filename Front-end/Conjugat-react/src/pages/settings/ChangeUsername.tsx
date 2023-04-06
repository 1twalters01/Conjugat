import { useState } from "react"
import Authorization from '../../functions/Authorization'
import UsernameChangeForm from "../../components/settings/Change username/UsernameChangeForm"

function ChangeUsername() {
  Authorization.AuthRequired()
  const [done, setDone] = useState(false)

    if (done == false) {
        return (
          <div className="rhs container">
              <div className="Header-spacer">
                  <h1 className="text">Change Username</h1>
              </div>
              
              <div className="form-spacer">
                  <UsernameChangeForm
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
                    <h1 className="text">Change Username done</h1>
                </div>                

                <div className="para">
                    <p className="text">Username has been updated</p>
                </div>
            </div>
        )
    }
    return <div></div>
}

export default ChangeUsername