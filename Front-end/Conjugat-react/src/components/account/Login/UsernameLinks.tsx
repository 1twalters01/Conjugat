import { Link } from "react-router-dom"
import '../../../sass/Components/account/DualLinks.scss'


function UsernameLinks() {
    return (
      <div className="links">
        <Link to="../Register"><div className="link weak-btn">Register</div></Link>
        <Link to="../../Newsletter/subscribe"><div className="link weak-btn">Newsletter</div></Link>
      </div>
    )
}

export default UsernameLinks