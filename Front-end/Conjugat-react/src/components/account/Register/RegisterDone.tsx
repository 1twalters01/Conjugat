import { Link } from "react-router-dom"

function RegisterDone() {
    return(
      <div>  
          <div>
              <p>We've emailed you instructions for setting your password.</p>
              <p>If you don't receive an email, please make sure you've entered the address you registered with.</p>
              <Link to="../login"><div>Login</div></Link>
          </div>
      </div>
    )
}

export default RegisterDone