import { useState } from "react"
import AxiosInstance from "../../functions/AxiosInstance"
import { Outlet, useNavigate } from "react-router-dom"

function Newsletter() {
    // If not auth then redirect to subscribe page
    const navigate = useNavigate()
    type ISubscribed = null|boolean
    const [subscribed, setSubscribed] = useState<ISubscribed>(null)
    
    if (subscribed == null) {
        AxiosInstance.Authorised
        .get('newsletter/obtain-status/')
        .then((res: { data: { status: string } })=> {
            if (res.data.status == 'Subscribed') {
                setSubscribed(true)
                navigate('/newsletter/unsubscribe')
            }
            else {
                setSubscribed(false)
                navigate('/newsletter/subscribe/')
            }
            console.log(res.data.status)
        })
    }
    return (
        <>
        <Outlet />
        </>
    )
}

export default Newsletter