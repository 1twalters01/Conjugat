import '../../sass/Components/Input fields/SubmitBtn.scss'

function SubmitBtn({value}: {value:string}) {
    return (
        <div className="submit-btn">
            <input type="submit" className="strong-btn" value={value} />
        </div>
    )
}

export default SubmitBtn