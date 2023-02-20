import Authorization from '../../Authorization'

function PasswordResetToken() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Registration Confirmation</h1>

      </div>
    )
  }

  export default PasswordResetToken