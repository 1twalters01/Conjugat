import { Link } from "react-router-dom"
import '../../../sass/Components/account/DualLinks.scss'


function UsernameLinks() {
    return (
      <div className="links">
          <Link to="../../Newsletter/subscribe"><div className="link weak-gold-btn">Newsletter</div></Link>
          <Link to="../Register"><div className="link weak-green-btn">Register</div></Link>
      </div>
    )
}

export default UsernameLinks