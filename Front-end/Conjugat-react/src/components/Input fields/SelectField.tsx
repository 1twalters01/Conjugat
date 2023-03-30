import '../../sass/Components/Input fields/SelectField.scss'

function SelectField({languages, changeLanguage}: {languages:string[], changeLanguage:Function}) {
    return(
        <div className="select-field">
            <label htmlFor="languages" className="field-text line-label">Languages</label>
            <select name="languages" size={3} id="languages" value={languages || []} onChange={(e) => changeLanguage(e)} multiple={true}>
                <option value="English">English</option>
                <option value="French">French</option>
                <option value="Italian">Italian</option>
                <option value="Portuguese">Portuguese</option>
                <option value="Spanish">Spanish</option>
            </select>
        </div>
    )
}

export default SelectField