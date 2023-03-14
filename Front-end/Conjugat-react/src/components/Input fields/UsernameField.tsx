import '../../sass/Components/Input fields/UsernameField.scss'

function UsernameField({ username, handleUsername, labelText="Email or Username" }: {username:string, handleUsername:Function, labelText:string}) {
  return (
    <div className='username-field'>
      <label htmlFor="username" className="field-text">{labelText}</label>
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