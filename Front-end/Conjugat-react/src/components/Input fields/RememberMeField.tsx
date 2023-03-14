import '../../sass/Components/Input fields/RememberMeField.scss'

function RememberMeField({rememberMe, handleRememberMe}: {rememberMe: boolean|undefined, handleRememberMe: Function}) {
  return (
    <div className='remember-me'>
      <div>
      <input
        id="rememberMe"
        type="checkbox"
        name="rememberMe"
        checked={rememberMe}
        onChange={(e) => handleRememberMe(e)}
        className="checkbox"
      />
      <label htmlFor="rememberMe" className="field-text">remember me</label>
      </div>
      
    </div>
  )
}

export default RememberMeField