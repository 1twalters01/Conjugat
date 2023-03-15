import { useState } from "react"
import LoadTwoFactorAuth from "../../components/settings/Two factor auth/LoadTwoFactorAuth";
import Authorization from '../../functions/Authorization'

function TwoFactorAuth() {
  Authorization.AuthRequired()
  const [loading, setLoading] = useState(true);
  const [done, setDone] = useState(false)
  if (done == false) {
    return (
      <div>
        <h1>TwoFactorAuth</h1>

        <LoadTwoFactorAuth
          loading={loading}
          setDone={setDone}
          setLoading={setLoading}
        />
      </div>
    )
  }
  return (
    <p>Two factor authentication activation successful</p>
  )
}

export default TwoFactorAuth