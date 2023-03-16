import AxiosInstance from "../../../functions/AxiosInstance"

function CoinbaseProcess({url}: {url:string}) {
    function submit() {
        console.log(url, 'Coinbase')

        AxiosInstance.Authorised
        .post('subscriptions/process/', {
            charge_url: url,
            method: 'Coinbase',
        })
        .then(res => {
            window.location.href = url
        })
    }
    return(
        <div>
            <p>Coinbase</p>
            <a href='#' onClick={submit}><button>Purchase</button></a>
        </div>
    )
}

export default CoinbaseProcess