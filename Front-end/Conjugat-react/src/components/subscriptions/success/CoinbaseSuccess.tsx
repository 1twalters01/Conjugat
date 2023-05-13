import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import { getTranslation } from "../../../functions/getTranslation"
import { CoinbaseSuccessTranslations } from "../../../content/settings/Premium"


function CoinbaseSuccess({charge} : {charge:string}) {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
      <div>
        <p>{getTranslation(CoinbaseSuccessTranslations, language, 'Text1')}</p>
        <a href={charge}><button>{getTranslation(CoinbaseSuccessTranslations, language, 'Text2')}</button></a>
      </div>
      
    )
}

export default CoinbaseSuccess