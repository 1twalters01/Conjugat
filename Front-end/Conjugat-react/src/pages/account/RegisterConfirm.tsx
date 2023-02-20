import Authorization from '../../Authorization'

function RegisterConfirmation() {
    Authorization.NotAuthRequired()
    return (
      <div>
        <h1>Registration Confirmation</h1>

      </div>
    )
  }

  export default RegisterConfirmation