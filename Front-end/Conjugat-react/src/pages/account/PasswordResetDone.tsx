import Authorization from '../../Authorization'

function PasswordResetDone() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Registration Done</h1>

      </div>
    )
  }

  export default PasswordResetDone