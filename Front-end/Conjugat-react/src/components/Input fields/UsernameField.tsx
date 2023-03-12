function UsernameField({ username, handleUsername }: {username:string, handleUsername:Function}) {
    return (
      <div className='field'>
        <label htmlFor="password" className="field-text">Email or Username</label>
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