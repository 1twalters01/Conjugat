import Authorization from '../../Authorization'

function PasswordResetConfirm() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Registration Confirmation</h1>

      </div>
    )
  }

  export default PasswordResetConfirm