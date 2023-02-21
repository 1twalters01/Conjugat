import { useParams } from 'react-router-dom'
import Axios from 'axios'
import Authorization from '../../Authorization'

function Activate() {
  Authorization.NotAuthRequired()
  
  activateAccount()

  return (
    <h1>Activate</h1>
  )
}

function activateAccount() {
  const { uidb64, token } = useParams();
  console.log(token)
  const url = "http://conjugat.io:8000/account/activate/"
  Axios.post(url, {
    uidb64: uidb64,
    token: token,
  })
}

export default Activate