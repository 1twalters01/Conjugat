function CoinbaseSuccess({charge} : {charge:string}) {
    return (
      <div>
        <p>Coinbase</p>
        <a href={charge}><button>View Purchase</button></a>
      </div>
      
    )
}

export default CoinbaseSuccess