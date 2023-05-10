import { Link } from "react-router-dom"
import '../../sass/Components/account/Header.scss'
import { getTranslation } from "../../functions/getTranslation"
import { translations as translationsHeader } from '../../content/Header'

function Header({language}: {language:string}) {
    return (
        <div className="headings">
            <Link to="../../"><h1 className="title header">{getTranslation(translationsHeader, language, 'Header')}</h1></Link>
            <h2 className="subheader">{getTranslation(translationsHeader, language, 'Subheader')}</h2>
        </div>
    )
}

export default Header