import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import AxiosInstance from "../../../functions/AxiosInstance"
import { getTranslation } from "../../../functions/getTranslation"
import { StripeSuccessTranslations } from "../../../content/settings/Premium"
import '../../../sass/Components/subscriptions/Process/StripeProcess.scss'

function StripeProcess({url, stripeCustomerID}: {url:string, stripeCustomerID:string}) {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)

    function click() {
        AxiosInstance.Authorised
        .post('subscriptions/new-stripe-customer/', {
            customer_id: stripeCustomerID,
        })
        .then(res => {
            window.location.href = url
        })
    }
    return(
      <div>
          <h2>{getTranslation(StripeSuccessTranslations, language, 'Text1')}</h2>
          <div>
              <div>
                  <h3>{getTranslation(StripeSuccessTranslations, language, 'Text2')}</h3>
                  <h5>{getTranslation(StripeSuccessTranslations, language, 'Text3')}</h5>
              </div>
              
              <button onClick={click} className="StripeBtn">{getTranslation(StripeSuccessTranslations, language, 'Text4')}<span>{getTranslation(StripeSuccessTranslations, language, 'Text5')}</span></button>
          </div>
      </div>
    )
}

export default StripeProcess