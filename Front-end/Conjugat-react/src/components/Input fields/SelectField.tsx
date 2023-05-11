import '../../sass/Components/Input fields/SelectField.scss'

function SelectField({labelText, languages, changeLanguage, FieldList, FieldListValues}: {labelText:string, languages:string[], changeLanguage:Function, FieldList:string[], FieldListValues:string[]}) {
    return(
        <div className="select-field">
            <label htmlFor="languages" className="field-text line-label">{labelText}</label>
            <select name="languages" size={Math.max(FieldList.length, 1)} id="languages" value={languages || []} onChange={(e) => changeLanguage(e)} multiple={true}>
                {FieldList.map((option, i) => (
                    <option value={FieldListValues[i]}>{option}</option>
                ))}
            </select>
        </div>
    )
}

export default SelectField