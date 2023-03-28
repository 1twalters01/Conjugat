import { Link } from "react-router-dom"

import '../../../sass/Components/account/Login/PasswordReset.scss'

function PasswordReset() {
    return (
      <div className="password-reset">
        <Link to="../password-reset" className="text-blue-link">
          Forgotten your password?
        </Link>
      </div>
    )
  }

export default PasswordReset