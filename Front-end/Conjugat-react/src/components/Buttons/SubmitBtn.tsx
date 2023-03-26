import '../../sass/Components/Input fields/SubmitBtn.scss'

function SubmitBtn({value, style}: {value:string, style:string}) {
    return (
        <div className="submit-btn">
            <input type="submit" className={"strong-btn strong-gold-btn"} value={value} />
        </div>
    )
}

export default SubmitBtn