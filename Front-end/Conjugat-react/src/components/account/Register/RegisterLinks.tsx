import { Link } from "react-router-dom"
import '../../../sass/Components/account/DualLinks.scss'

function RegisterLinks() {
    return (
      <div className="links">
        <Link to="../Login"><div className="link weak-btn">Login</div></Link>
        <Link to="../../Newsletter/subscribe"><div className="link weak-btn">Newsletter</div></Link>
      </div>
    )
}

export default RegisterLinks