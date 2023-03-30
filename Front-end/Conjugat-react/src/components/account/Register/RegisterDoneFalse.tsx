import { Link } from "react-router-dom"
import '../../../sass/Components/account/Register/RegisterDone.scss'

function RegisterDoneFalse() {
    return(
        <div className="Register-done">  
            <div className="para">
                <p className="text">Your account has been successfully made.</p>
                <p className="text">Please follow the link below to log in.</p>
            </div>  
            <Link to="../login"><div className="btn strong-gold-btn">Login</div></Link>
        </div>
    )
}

export default RegisterDoneFalse