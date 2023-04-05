import Authorization from '../../functions/Authorization'
import RetrieveStatus from "../../components/subscriptions/Process/RetrieveStatus"
import '../../sass/pages/subscriptions/Process.scss'

function Process() {
    Authorization.AuthRequired()
    return (
        <div className='Process-container container'>
            <h1>Process</h1>

            <div className="status-container">
                <RetrieveStatus />
            </div>
        </div>
    )
}

export default Process