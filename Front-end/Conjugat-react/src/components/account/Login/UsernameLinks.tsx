import { Link } from "react-router-dom"
import { getTranslation } from "../../../functions/getTranslation"
import { UsernameLinksTranslation } from "../../../content/account/Login"
import '../../../sass/Components/account/DualLinks.scss'


function UsernameLinks({language}: {language:string}) {
    return (
      
      <div className="dual-links">
          <Link to="../../Newsletter/subscribe"><div className="link weak-gold-btn">{getTranslation(UsernameLinksTranslation, language, 'Newsletter')}</div></Link>
          <Link to="../Register"><div className="link weak-green-btn">{getTranslation(UsernameLinksTranslation, language, 'Register')}</div></Link>
      </div>
    )
}

export default UsernameLinks