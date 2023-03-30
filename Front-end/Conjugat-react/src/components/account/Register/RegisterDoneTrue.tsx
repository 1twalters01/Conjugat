import { Link } from "react-router-dom"

function RegisterDoneTrue() {
    return(
        <div className="Register-done">  
            <div className="para">
                <p className="text">We've emailed you instructions for setting your password.</p>
                <p className="text">If you don't receive an email, please make sure you've entered the address you registered with.</p>
            </div>  
            <Link to="../../"><div className="btn strong-gold-btn">Home</div></Link>
        </div>
    )
}

export default RegisterDoneTrue