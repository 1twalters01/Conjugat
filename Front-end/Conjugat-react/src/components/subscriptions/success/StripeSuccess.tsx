function StripeSuccess({url} : {url:string}) {
    return (
        <div>
            <p>Stripe</p>
            <p>Your payment has been processed successfully</p>

            <a href={url}><button>Manage your billing information</button></a>
        </div>
    )
}

export default StripeSuccess