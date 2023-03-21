import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js"
import AxiosInstance from "../../../functions/AxiosInstance";

function PaypalProcess({trial} : {trial:boolean|null}) {
    const paypalSubscribe = (data:any, actions:any) => {
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
    };
  
    if (trial==true || trial==false) {
      return(
        <div>
          <p>Paypal</p>
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
      <div></div>
    )
}

export default PaypalProcess