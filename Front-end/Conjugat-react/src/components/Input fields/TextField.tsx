import '../../sass/Components/Input fields/TextField.scss'

function TextField({ id, labelText, value, handleText, required=true }: { id:string, labelText:string, value:string, handleText:Function, required:boolean}) {
  return (
    <div className='text-field'>
      <label htmlFor="text" className="field-text line-label">{labelText}</label>
      <input
        id={id}
        type="text"
        name="text"
        className='line'
        value={ value }
        onChange={(e) => handleText(e)}
        required={ required }
      />
    </div>
  )
}

export default TextField