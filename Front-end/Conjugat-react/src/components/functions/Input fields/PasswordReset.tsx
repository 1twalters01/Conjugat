import { Link } from "react-router-dom"

function PasswordReset() {
    return (
      <div className="password-reset">
        <Link to="../password-reset">
          Forgotten your password?
        </Link>
      </div>
    )
  }

export default PasswordReset