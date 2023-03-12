function EmailField({email, handleEmail}: {email:string, handleEmail: Function}) {
    return(
      <div className='field'>
          <label htmlFor="email" className="field-text">Email</label>
          <input
              id="email"
              type="email"
              name="email"
              value={ email }
              onChange={(e) => handleEmail(e)}
              required={true}
          />
      </div>
    )
}

export default EmailField