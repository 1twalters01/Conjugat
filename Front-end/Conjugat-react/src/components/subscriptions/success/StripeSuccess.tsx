import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import { getTranslation } from "../../../functions/getTranslation"
import { StripeSuccessTranslations } from "../../../content/settings/Premium"

function StripeSuccess({url} : {url:string}) {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    
    return (
        <div>
            <p>{getTranslation(StripeSuccessTranslations, language, 'Text1')}</p>
            <p>{getTranslation(StripeSuccessTranslations, language, 'Text2')}</p>

            <a href={url}><button>{getTranslation(StripeSuccessTranslations, language, 'Text3')}</button></a>
        </div>
    )
}

export default StripeSuccess