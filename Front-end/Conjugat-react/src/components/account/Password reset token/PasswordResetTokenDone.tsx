import { Link } from 'react-router-dom'
import '../../../sass/Components/account/Password reset token/PasswordResetTokenDone.scss'

function PasswordResetTokenDone(){
    return(
        <div className="PasswordResetTokenDone-response">
            <p className="para text">Your password has successfully been reset.</p>
            <Link to="../login"><div className="login-btn strong-gold-btn">Login</div></Link>
        </div>
    )
}

export default PasswordResetTokenDone