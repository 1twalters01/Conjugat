import '../../sass/Components/Input fields/SelectField.scss'

function SelectField({languages, changeLanguage, FieldList, FieldListValues}: {languages:string[], changeLanguage:Function, FieldList:string[], FieldListValues:string[]}) {
    return(
        <div className="select-field">
            <label htmlFor="languages" className="field-text line-label">Languages</label>
            <select name="languages" size={3} id="languages" value={languages || []} onChange={(e) => changeLanguage(e)} multiple={true}>
                {FieldList.map((option, i) => (
                    <option value={FieldListValues[i]}>{option}</option>
                ))}
            </select>
        </div>
    )
}

export default SelectField