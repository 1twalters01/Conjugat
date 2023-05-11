import { Link } from "react-router-dom"
import { getTranslation } from "../../functions/getTranslation"
import { newsletterLinksTranslations } from '../../content/newsletter/Subscribe'
import '../../sass/Components/newsletter/NewsletterLinks.scss'

function NewsletterLinks({language}: {language:string}) {
    return (
        <div className="newsletter-links">
            <Link to="../../account/Login" className="link weak-blue-btn">{getTranslation(newsletterLinksTranslations, language, 'Login')}</Link>
            <Link to="../../account/Register" className="link weak-green-btn">{getTranslation(newsletterLinksTranslations, language, 'Register')}</Link>
        </div>
    )
}

export default NewsletterLinks