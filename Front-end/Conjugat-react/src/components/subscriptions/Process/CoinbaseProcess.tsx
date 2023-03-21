import AxiosInstance from "../../../functions/AxiosInstance"

function CoinbaseProcess({url}: {url:string}) {
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
            <p>Coinbase</p>
            <a onClick={submit}><button>Purchase</button></a>
        </div>
    )
}

export default CoinbaseProcess