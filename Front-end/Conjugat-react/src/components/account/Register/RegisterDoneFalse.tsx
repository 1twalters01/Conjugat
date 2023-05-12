import { Link } from "react-router-dom"
import { getTranslation } from "../../../functions/getTranslation"
import { RegisterDoneFalseTranslations } from "../../../content/account/Register"
import '../../../sass/Components/account/Register/RegisterDone.scss'

function RegisterDoneFalse({language}: {language:string}) {
    return(
        <div className="Register-done">  
            <div className="para">
                <p className="text">{getTranslation(RegisterDoneFalseTranslations, language, 'Text1')}</p>
                <p className="text">{getTranslation(RegisterDoneFalseTranslations, language, 'Text2')}</p>
            </div>  
            <Link to="../login"><div className="btn strong-gold-btn">Login</div></Link>
        </div>
    )
}

export default RegisterDoneFalse