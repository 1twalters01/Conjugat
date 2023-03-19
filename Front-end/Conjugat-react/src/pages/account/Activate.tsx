import { useEffect } from 'react'
import { useParams } from 'react-router-dom'
import Authorization from '../../functions/Authorization'
import AxiosInstance from '../../functions/AxiosInstance'

function Activate() {
    Authorization.NotAuthRequired()
    const { uidb64, token } = useParams()
    const activateAccount = async () => {const res = await (
        AxiosInstance.Unauthorised
        .post('/account/activate/', {
            uidb64: uidb64,
            token: token
        })
        .catch(err => {
            console.log(err.response.data.error)
        })
    )}

    useEffect(() => {
      activateAccount();
    }, [])

    return (
      <h1>Activate</h1>
    )
}

function activateAccount() {

    
}

export default Activate