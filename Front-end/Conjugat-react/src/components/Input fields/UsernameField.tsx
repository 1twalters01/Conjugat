function UsernameField({ username, handleUsername, labelText="Email or Username" }: {username:string, handleUsername:Function, labelText:string}) {
    return (
      <div className='field'>
        <label htmlFor="password" className="field-text">{labelText}</label>
        <input
          id="username"
          type="text"
          name="username"
          value={ username }
          onChange={(e) => handleUsername(e)}
          required={true}
        />
      </div>
    )
  }

export default UsernameField