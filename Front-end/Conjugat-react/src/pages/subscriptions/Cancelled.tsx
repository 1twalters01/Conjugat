import Authorization from '../../functions/Authorization'
import { Link } from 'react-router-dom'
import '../../sass/pages/subscriptions/Cancelled.scss'

function Cancelled() {
  Authorization.AuthRequired()
  return (
    <div className='Cancelled-container container'>
      <h1 className='text'>Payment cancelled</h1>
      
      <div className="text-spacer">
          <p className='text'>There was a problem processing your payment.</p>
      </div>
      

      <div className="btn-spacer">
          <Link to="../process" className='retry-btn strong-gold-btn'> Try again</Link>
      </div>
      
    </div>
  )
}

export default Cancelled