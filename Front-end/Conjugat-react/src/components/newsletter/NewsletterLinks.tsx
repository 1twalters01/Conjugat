import { Link } from "react-router-dom"
import '../../sass/Components/newsletter/NewsletterLinks.scss'

function NewsletterLinks() {
    return (
        <div className="newsletter-links">
            <Link to="../../account/Login" className="link weak-blue-btn">Login</Link>
            <Link to="../../account/Register" className="link weak-green-btn">Register</Link>
        </div>
    )
}

export default NewsletterLinks