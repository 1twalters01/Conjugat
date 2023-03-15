import '../../sass/Components/Input fields/EmailField.scss'

function EmailField({ id, email, labelText, handleEmail}: { id:string, email:string, labelText:string, handleEmail: Function}) {
    return(
      <div className='email-field'>
          <label htmlFor="email" className="field-text">{labelText}</label>
          <input
              id={id}
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