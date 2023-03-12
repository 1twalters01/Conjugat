import { Link } from "react-router-dom"

function LogoutResponse() {
    return(
      <div className="log-out">
        <h1>Logged out</h1>
        <p>You have been successfully logged out.</p>
        <Link to="../login"><div className="register weak-btn">Login</div></Link>
      </div>
    )
}

export default LogoutResponse