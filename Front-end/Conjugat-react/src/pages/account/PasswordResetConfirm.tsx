import { Outlet, NavLink } from "react-router-dom"
import Authorization from '../../Authorization'

function PasswordResetConfirm() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Password Confirmations</h1>
        
      </div>
    )
  }

  export default PasswordResetConfirm