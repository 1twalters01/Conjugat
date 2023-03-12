function PasswordField({ password, handlePassword, id='password', labelText='Password' }: {password:string, handlePassword:Function, id:string, labelText:string}) {
    return (
        <div className='field'>
            <label htmlFor="password" className="field-text">{labelText}</label>
            <input
                id={ id }
                type="password"
                name="password"
                value={ password }
                onChange={(e) => handlePassword(e)}
                required={true}
            />
        </div>
    )
}

export default PasswordField