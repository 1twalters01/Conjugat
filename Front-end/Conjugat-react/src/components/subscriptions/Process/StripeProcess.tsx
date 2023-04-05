import AxiosInstance from "../../../functions/AxiosInstance"
import '../../../sass/Components/subscriptions/Process/StripeProcess.scss'

function StripeProcess({url, stripeCustomerID}: {url:string, stripeCustomerID:string}) {
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
          <h2>Stripe</h2>
          <div>
              <div>
                  <h3>Premium plan</h3>
                  <h5>$3.00 / month</h5>
              </div>
              
              <button onClick={click} className="StripeBtn">Checkout with <span>stripe</span></button>
          </div>
      </div>
    )
}

export default StripeProcess