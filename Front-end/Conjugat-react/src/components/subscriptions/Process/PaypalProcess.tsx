import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js"
import { useSelector } from "react-redux"
import { RootState } from "../../../redux/store"
import AxiosInstance from "../../../functions/AxiosInstance"
import { getTranslation } from "../../../functions/getTranslation"
import { StripeSuccessTranslations } from "../../../content/settings/Premium"

function PaypalProcess({trial} : {trial:boolean|null}) {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)

    const paypalSubscribe = (_data: any, actions: any) => {
      if (trial==false) {
        return actions.subscription.create({
          'plan_id': `${import.meta.env.VITE_paypal_no_trial_plan_id}`,
        });
      }
      else if (trial==true) {
        return actions.subscription.create({
          'plan_id': `${import.meta.env.VITE_paypal_with_trial_plan_id}`,
        });
      }
    };
  
    const paypalOnError = (err:any) => {
      console.log("Error", err)
    }
  
    const paypalOnCancel = (err:any) => {
      console.log("cancelled", err)
    }
  
    const paypalOnApprove = (data:any, detail:any) => {
      AxiosInstance.Authorised
      .post('subscriptions/new-paypal-customer/', {
        subscriber_id: data.subscriptionID,
      })
      .then(res=>{
        window.location.href = "/subscriptions/success"
      })
      return Promise.resolve();
    };
  
    if (trial==true || trial==false) {
      return(
        <div>
          <p>{getTranslation(StripeSuccessTranslations, language, 'Text1')}</p>
          <PayPalScriptProvider
            options={{"client-id":`${import.meta.env.VITE_paypal_client_id}`, vault:true}}
          >
            <PayPalButtons
              createSubscription={paypalSubscribe}
              onApprove={paypalOnApprove}
              onError={paypalOnError}
              onCancel={paypalOnCancel}
            />
          </PayPalScriptProvider>
        </div>
      )
    }
  
    return (
      <div>
        <p>{getTranslation(StripeSuccessTranslations, language, 'Text2')}</p>
      </div>
    )
}

export default PaypalProcess