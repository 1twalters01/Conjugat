import { Link } from "react-router-dom"
import { getTranslation } from "../../../functions/getTranslation"
import { RegisterDoneTrueTranslations } from "../../../content/account/Register"

function RegisterDoneTrue({language}: {language:string}) {
    return(
        <div className="Register-done">  
            <div className="para">
                <p className="text">{getTranslation(RegisterDoneTrueTranslations, language, 'Text1')}</p>
                <p className="text">{getTranslation(RegisterDoneTrueTranslations, language, 'Text2')}</p>
            </div>  
            <Link to="../../"><div className="btn strong-gold-btn">Home</div></Link>
        </div>
    )
}

export default RegisterDoneTrue