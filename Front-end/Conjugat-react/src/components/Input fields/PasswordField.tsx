import '../../sass/Components/Input fields/PasswordField.scss'

function PasswordField({ password, handlePassword, id='password', labelText='Password' }: {password:string, handlePassword:Function, id:string, labelText:string}) {
    return (
        <div className='password-field'>
            <label htmlFor="password" className="field-text line-label">{labelText}</label>
            <input
                id={ id }
                type="password"
                name="password"
                className='line'
                value={ password }
                onChange={(e) => handlePassword(e)}
                required={true}
            />
        </div>
    )
}

export default PasswordField