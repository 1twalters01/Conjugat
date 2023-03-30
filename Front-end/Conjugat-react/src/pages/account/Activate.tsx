import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { toast } from 'react-toastify'
import Header from '../../components/account/Header'
import Authorization from '../../functions/Authorization'
import AxiosInstance from '../../functions/AxiosInstance'
import '../../sass/pages/account/Activate.scss'

function Activate() {
    Authorization.NotAuthRequired()
    const [Activated, SetActivated] = useState(false)
    const [Error, SetError] = useState(false)
    const { uidb64, token } = useParams()
    const activateAccount = async () => {const res = await (
        AxiosInstance.Unauthorised
        .post('/account/activate/', {
            uidb64: uidb64,
            token: token
        })
        .then(res =>
            SetActivated(true)
        )
        .catch(err => {
            SetError(true)
        })
    )}

    useEffect(() => {
      activateAccount();
    }, [])

    if(Activated == false && Error == false) {
        return (
          <></>
        )
    }
    else if(Activated == true) {
        return (
          <div className='Activate-container container'>
              <div className="header-spacer">
                  <Header />
              </div>

              <div className="text-spacer">
                  <p className='text'>You have successfully activated your account.</p>
              </div>

              <div className="btn-spacer">
                  <Link to='../Login' ><div className="login-btn strong-gold-btn">Login</div></Link>
              </div>
          </div>
        )
    }
    if (Error == true && Activated == false) {
      console.log('hi')
        return (
          <div className="Activate-container container">
              <div className="header-spacer">
                  <Header />
              </div>

              <div className="text-spacer">
                  <p className='text'>Something went wrong. Please try again later.</p>
              </div>

              <div className="btn-spacer">
                  <Link to='../Login' ><div className="login-btn strong-gold-btn">Login</div></Link>
              </div>
          </div>
        )
    }
    return <></>
}

export default Activate