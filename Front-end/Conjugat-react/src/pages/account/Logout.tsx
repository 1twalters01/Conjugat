import Authorization from '../../components/functions/Authorization'
import LogoutBtn from '../../components/account/Logout/LogoutBtn'

function Logout() {
  Authorization.AuthRequired()
  return (
    <div>
        <h1>Logout</h1>

        <LogoutBtn />
    </div>
  )
}

export default Logout