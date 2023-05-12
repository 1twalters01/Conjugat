import { Link } from "react-router-dom"
import { getTranslation } from "../../../functions/getTranslation"
import { LogoutResponseTranslations } from "../../../content/account/Logout"
import '../../../sass/Components/account/Logout/LogoutResponse.scss'

function LogoutResponse({language}: {language:string}) {
    return(
        <div className="Logout-response">
            <p className="para text">{getTranslation(LogoutResponseTranslations, language, 'Text1')}</p>
            <Link to="../../../"><div className="home-btn strong-gold-btn">{getTranslation(LogoutResponseTranslations, language, 'Text2')}</div></Link>
        </div>
    )
}

export default LogoutResponse