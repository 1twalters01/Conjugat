import { Link } from "react-router-dom"
import { getTranslation } from "../../functions/getTranslation"
import { NewsletterResponseTranslation } from '../../content/newsletter/Subscribe'
import '../../sass/Components/newsletter/NewsletterResponseUnauth.scss'

function NewsletterResponse({language, text}: {language:string, text:string}) {
    return (
        <div className="Newsletter-response">
            <p className="para text">{text}</p>
            <Link to="../../../"><div className="home-btn strong-gold-btn">{getTranslation(NewsletterResponseTranslation, language, 'Home')}</div></Link>
        </div>
    )
}

export default NewsletterResponse