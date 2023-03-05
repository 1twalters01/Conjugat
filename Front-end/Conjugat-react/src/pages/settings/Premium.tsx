function Premium() {
  return (
    <div>
      <h1>Premium</h1>

      <RetrieveStatus />
    </div>
  )
}

function RetrieveStatus() {
  const [method, setMethod] = useState(null)
  const [subscribed, setSubscribed] = useState(null)
  const [charge, setCharge] = useState('')
  const [status, setStatus] = useState('')
  
  if(count < 2){
    Axios.get(url, {headers: headers})
    .then(res =>{
      setMethod(res.data.method)
      setSubscribed(res.data.subscribed)
      setCharge(res.data.charge)
      setStatus(res.data.status)
    })
    count += 1
  }
  else{
    if(subscribed == false) {
      window.location.href = "/subscriptions/process"
    }

    if(method == 'Stripe' && subscribed == true) {
      return (
        <div>
          <StripeSuccess />
        </div>
      )
    }
    else if(method == 'Paypal' && subscribed == true) {
      console.log(status, 'paypal')
      return (
        <div>
          <PaypalSuccess status={status}/>
        </div>
      )
    }
    else if(method == 'Coinbase' && subscribed == true) {
      console.log(charge)
      return (
        <div>
          <CoinbaseSuccess charge={charge} />
        </div>
      )
    }
    return (
      <div>
        <p>Loading...</p>
      </div>
    )
  }
  return(
    <div></div>
  )
}

export default Premium