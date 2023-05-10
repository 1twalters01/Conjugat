import { Link } from "react-router-dom"
import '../../sass/Components/home/MiscNavbar.scss'
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/home/MiscNavbar"

function MiscNavbar({language}: {language:string}){
    return(
        <div className="Misc-navbar">
            <Link to='/Contact' ><p className="nav-link text-blue-link">{getTranslation(translations, language, 'Contact')}</p></Link>
            <Link to='/Faq' ><p className="nav-link text-blue-link">{getTranslation(translations, language, 'Faq')}</p></Link>
            <Link to='/Privacy' ><p className="nav-link text-blue-link">{getTranslation(translations, language, 'Privacy')}</p></Link>
            <Link to='/Terms' ><p className="nav-link text-blue-link">{getTranslation(translations, language, 'Terms')}</p></Link>
            <Link to='/Premium' ><p className="nav-link text-blue-link">{getTranslation(translations, language, 'Premium')}</p></Link>
        </div>
    )
}

export default MiscNavbar