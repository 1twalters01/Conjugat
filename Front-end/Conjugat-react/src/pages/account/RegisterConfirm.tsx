import { Link } from "react-router-dom"
import Authorization from '../../Authorization'

function RegisterConfirmation() {
  
  Authorization.NotAuthRequired()
  return (
    <div>
      <h1>Registration Confirmation</h1>

      <div>
          <p>We've emailed you instructions for setting your password.</p>
          <p>If you don't receive an email, please make sure you've entered the address you registered with.</p>
          <Link to="../login"><div>Login</div></Link>
      </div>
    </div>
  )
}

  export default RegisterConfirmation