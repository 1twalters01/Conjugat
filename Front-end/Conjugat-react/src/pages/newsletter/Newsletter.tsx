import { useState } from "react"
import AxiosInstance from "../../functions/AxiosInstance"
import { useNavigate } from "react-router-dom"

function Newsletter() {
    // If not auth then redirect to subscribe page
    const navigate = useNavigate()
    type ISubscribed = null|boolean
    const [subscribed, setSubscribed] = useState<ISubscribed>(null)
    AxiosInstance.Authorised
    .get('')
    .then((res: { data: { status: string } })=> {
        if (res.data.status == 'Subscribed') {
            setSubscribed(true)
            navigate('/newsletters/subscribe')
        }
        else {
            setSubscribed(false)
            navigate('/newsletters/subscribe')
        }
    })
}

export default Newsletter