import GetFacebookURL from './FacebookBtn'
import GetGoogleURL from './GoogleBtn'
import GetTwitterURL from './TwitterBtn'
import { getTranslation } from "../../../functions/getTranslation"
import { AlternateLoginTranslation } from "../../../content/account/Login"
import '../../../sass/Components/account/Login/AlternateLogins.scss'

function AlternateLogins({ language }: { language:string }) {
    return (
        <div className="alternatives">
            <p className="options text">{getTranslation(AlternateLoginTranslation, language, 'Label')}</p>
            <div className="alt-login">
                <GetFacebookURL />
                <GetGoogleURL />
                <GetTwitterURL />
            </div>
        </div>
    )
  }

export default AlternateLogins