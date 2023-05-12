import { Link } from "react-router-dom"
import { getTranslation } from "../../../functions/getTranslation";
import { RegisterLinksTranslations } from "../../../content/account/PasswordReset";
import '../../../sass/Components/account/DualLinks.scss'

function RegisterLinks({language}: {language:string}) {
    return (
        <div className="dual-links">
            <Link to="../Login"><div className="link weak-btn weak-blue-btn">{getTranslation(RegisterLinksTranslations, language, 'Login')}</div></Link>
            <Link to="../../Newsletter/subscribe"><div className="link weak-btn weak-gold-btn">{getTranslation(RegisterLinksTranslations, language, 'Newsletter')}</div></Link>
        </div>
    )
}

export default RegisterLinks