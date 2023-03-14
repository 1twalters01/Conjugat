import '../../../sass/Components/account/Login/UsernameLinks.scss'

import { Link } from "react-router-dom"

function UsernameLinks() {
    return (
        <div className="links">
            <Link to="../Register"><div className="link weak-btn">Register</div></Link>
            <Link to="../../Newsletter/subscribe"><div className="link weak-btn">Newsletter</div></Link>
        </div>
    )
}

export default UsernameLinks