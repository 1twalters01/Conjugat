import '../../sass/Components/Input fields/SelectField.scss'

function SelectField({labelText, field, changeField, FieldList, FieldListValues}: {labelText:string, field:string[], changeField:Function, FieldList:string[], FieldListValues:string[]}) {
    return(
        <div className="select-field">
            <label htmlFor="languages" className="field-text line-label">{labelText}</label>
            <select name="languages" size={Math.max(FieldList.length, 1)} id="languages" value={field || []} onChange={(e) => changeField(e)} multiple={true}>
                {FieldList.map((option, i) => (
                    <option value={FieldListValues[i]}>{option}</option>
                ))}
            </select>
        </div>
    )
}

export default SelectField