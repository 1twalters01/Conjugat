import '../../sass/Components/Input fields/EmailField.scss'

function EmailField({ id, email, labelText, handleEmail, required=true}: { id:string, email:string, labelText:string, handleEmail: Function, required: boolean}) {
    return(
      <div className='email-field'>
          <label htmlFor="email" className="field-text line-label">{labelText}</label>
          <input
              id={id}
              type="email"
              name="email"
              className='line'
              value={ email }
              onChange={(e) => handleEmail(e)}
              required={required}
          />
      </div>
    )
}

export default EmailField