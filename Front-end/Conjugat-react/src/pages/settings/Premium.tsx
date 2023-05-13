import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import Authorization from '../../functions/Authorization'
import RetrievePremiumStatus from "../../components/settings/premium/RetrievePremiumStatus"
import { getTranslation } from '../../functions/getTranslation'
import { translations } from '../../content/settings/Premium'

function Premium() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <div className="rhs container">
            <div className="Header-spacer">
                <h1 className="text">{getTranslation(translations, language, 'Text1')}</h1>
            </div>

            <div className="form-spacer">
                <RetrievePremiumStatus />
            </div>
        </div>
    )
}



export default Premium