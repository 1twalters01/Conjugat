import AxiosInstance from "../../../functions/AxiosInstance"
import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import { getTranslation } from "../../../functions/getTranslation"
import { StripeSuccessTranslations } from "../../../content/settings/Premium"

function CoinbaseProcess({url}: {url:string}) {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    
    function submit() {
        console.log(url, 'Coinbase')

        AxiosInstance.Authorised
        .post('subscriptions/new-coinbase-customer/', {
            charge_url: url,
        })
        .then(res => {
            window.location.href = url
        })
    }
    return(
        <div>
            <p>{getTranslation(StripeSuccessTranslations, language, 'Text1')}</p>
            <a onClick={submit}><button>{getTranslation(StripeSuccessTranslations, language, 'Text2')}</button></a>
        </div>
    )
}

export default CoinbaseProcess