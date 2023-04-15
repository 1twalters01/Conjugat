import { useEffect, useState } from "react"
import { Outlet, useNavigate } from "react-router-dom"
import AxiosInstance from "../../functions/AxiosInstance"
import Authorization from "../../functions/Authorization"

function Subscriptions() {
    Authorization.AuthRequired()
    const navigate = useNavigate()
    const [subscribed, setSubscribed] = useState(null)
    const base = 'http://localhost:5000/'
    
    if (window.location.href == base + 'subscriptions/' || window.location.href == base + 'subscriptions') {
        async function getStatus() {
            const res = await (
                AxiosInstance.Authorised
                .post('subscriptions/retrieve-status/', {
                    success_url: 'http://localhost:5000/subscriptions/success',
                    cancel_url: 'http://localhost:5000/subscriptions/cancelled',
                })
            )
            setSubscribed(res.data.subscribed)
        }
        
        getStatus()
    
        if (subscribed == true) {
            navigate('/subscriptions/success')
        }
        else if (subscribed == false) {
            navigate('/subscriptions/process')
        }
    }
    
    

    return (
        <>
            <Outlet />
        </>
    )
}

export default Subscriptions