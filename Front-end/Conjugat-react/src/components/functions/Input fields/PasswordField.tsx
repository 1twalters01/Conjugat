function PasswordField({ password, handlePassword }: {password:string, handlePassword:Function}) {
    return (
        <div className='field'>
        <label htmlFor="password" className="field-text">Password</label>
        <input
            id="password"
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