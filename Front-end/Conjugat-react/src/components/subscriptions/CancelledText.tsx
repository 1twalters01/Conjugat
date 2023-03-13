import { Link } from "react-router-dom"
function CancelledText() {
    return(
        <p>There was a problem processing your payment. <Link to="../process">Try again</Link></p>
    )
}

export default CancelledText