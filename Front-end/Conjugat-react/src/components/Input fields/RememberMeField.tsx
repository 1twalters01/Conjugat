import '../../sass/Components/Input fields/RememberMeField.scss'

function RememberMeField({labelText, rememberMe, handleRememberMe}: {labelText:string, rememberMe: boolean|undefined, handleRememberMe: Function}) {
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
        <div className="rememberMe-spacer"></div>
        <label htmlFor="rememberMe" className="field-text text">{labelText}</label>
      </div>
      
    </div>
  )
}

export default RememberMeField