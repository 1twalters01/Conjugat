function RememberMeField({rememberMe, handleRememberMe}: {rememberMe: boolean|undefined, handleRememberMe: Function}) {
  return (
    <div className='remember-me'>
      <input
        id="rememberMe"
        type="checkbox"
        name="rememberMe"
        checked={rememberMe}
        onChange={(e) => handleRememberMe(e)} />
      <label htmlFor="rememberMe" className="field-text">remember me</label>
    </div>
  )
}

export default RememberMeField