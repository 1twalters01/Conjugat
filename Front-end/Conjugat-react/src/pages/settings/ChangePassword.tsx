import { useState } from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import { getTranslation } from '../../functions/getTranslation'
import { translations } from '../../content/settings/ChangePassword'
import PasswordChangeForm from "../../components/settings/Change password/PasswordChangeForm"

function ChangePassword() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [done, setDone] = useState(false)

    if (done == false) {
        return (
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">{getTranslation(translations, language, 'Text1')}</h1>
                </div>
                
                <div className="form-spacer">
                    <PasswordChangeForm
                      onDoneChange={setDone}
                    />
                </div>
            </div>
        )
    }
    else {
        return (
            <div className="rhs container">
                <div className="Header-spacer">
                    <h1 className="text">{getTranslation(translations, language, 'Text2')}</h1>
                </div>                

                <div className="para">
                    <p className="text">{getTranslation(translations, language, 'Text3')}</p>
                </div>
                
            </div>
        )
    }
}

export default ChangePassword