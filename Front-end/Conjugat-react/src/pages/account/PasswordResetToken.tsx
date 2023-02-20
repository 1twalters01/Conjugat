import Authorization from '../../Authorization'

function PasswordResetToken() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Registration Token</h1>

      </div>
    )
  }

  export default PasswordResetToken