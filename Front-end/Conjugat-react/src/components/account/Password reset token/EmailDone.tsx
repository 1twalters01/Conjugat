import { Link } from 'react-router-dom'

function EmailDone(){
    return(
      <div>
        <h1>Registration Done</h1>
  
        <div>
          <p>Your password has successfully been reset.</p>
          <Link to="../login"><div>Login</div></Link>
        </div>
      </div>
    )
}

export default EmailDone