import { Link } from "react-router-dom"
import '../../../sass/Components/account/Logout/LogoutResponse.scss'

function LogoutResponse() {
    return(
        <div className="Logout-response">
            <p className="para text">You have been successfully logged out.</p>
            <Link to="../../../"><div className="home-btn strong-gold-btn">Home</div></Link>
        </div>
    )
}

export default LogoutResponse