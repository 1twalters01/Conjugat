import { Link } from "react-router-dom"

function LogoutAllResponse() {
    return(
      <div className="log-out">
        <h1>Logged out</h1>
        <p>You have been successfully logged out from all devices.</p>
        <Link to="../login"><div className="register weak-btn">Login</div></Link>
      </div>
    )
}

export default LogoutAllResponse