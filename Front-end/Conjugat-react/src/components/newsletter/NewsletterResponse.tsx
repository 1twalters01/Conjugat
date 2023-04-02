import { Link } from "react-router-dom"
import '../../sass/Components/newsletter/NewsletterResponseUnauth.scss'

function NewsletterResponse({text}: {text:string}) {
    return (
        <div className="Newsletter-response">
            <p className="para text">{text}</p>
            <Link to="../../../"><div className="home-btn strong-gold-btn">Home</div></Link>
        </div>
    )
}

export default NewsletterResponse