import { useParams } from 'react-router-dom'
import Axios from 'axios'
import Authorization from '../../Authorization'

function Activate() {
  const { uidb64, token } = useParams();
  const url = "http://conjugat.io:8000/account/activate/"
  Axios.post(url, {
    uidb64: uidb64,
    token: token,
  })

  Authorization.NotAuthRequired()
  return (
    <h1>Activate</h1>
  )
}

export default Activate