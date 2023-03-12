import { Link } from "react-router-dom"

function Header() {
    return (
        <div className="headings">
            <Link to="../../"><h1>Conjugat</h1></Link>
            <h2>Helping you to perfect your verb conjugations</h2>
        </div>
    )
}

export default Header