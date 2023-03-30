import { Link } from "react-router-dom"
import '../../../sass/Components/account/DualLinks.scss'

function RegisterLinks() {
    return (
        <div className="dual-links">
            <Link to="../Login"><div className="link weak-btn weak-blue-btn">Login</div></Link>
            <Link to="../../Newsletter/subscribe"><div className="link weak-btn weak-gold-btn">Newsletter</div></Link>
        </div>
    )
}

export default RegisterLinks