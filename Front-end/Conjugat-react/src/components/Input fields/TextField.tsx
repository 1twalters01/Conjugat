import '../../sass/Components/Input fields/TextField.scss'

function TextField({ id, labelText, value, handleText, required=true }: { id:string, labelText:string, value:string, handleText:Function, required:boolean}) {
  return (
    <div className='username-field'>
      <label htmlFor="username" className="field-text">{labelText}</label>
      <input
        id={id}
        type="text"
        name="username"
        value={ value }
        onChange={(e) => handleText(e)}
        required={ required }
      />
    </div>
  )
}

export default TextField