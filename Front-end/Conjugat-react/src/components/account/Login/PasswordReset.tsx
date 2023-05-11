import { Link } from "react-router-dom"

import '../../../sass/Components/account/Login/PasswordReset.scss'

function PasswordReset( {linkText}: {linkText:string} ) {
    return (
      <div className="password-reset">
        <Link to="../password-reset" className="text-blue-link">
          {linkText}
        </Link>
      </div>
    )
  }

export default PasswordReset