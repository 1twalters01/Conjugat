import { useParams } from 'react-router-dom'
import Authorization from '../../functions/Authorization'
import AxiosInstance from '../../functions/AxiosInstance'

function Activate() {
    Authorization.NotAuthRequired()
    activateAccount()
    return (
      <h1>Activate</h1>
    )
}

function activateAccount() {
    const { uidb64, token } = useParams()
    AxiosInstance.Unauthorised
    .post('/account/activate/', {
        uidb64: uidb64,
        token: token
    })
}

export default Activate