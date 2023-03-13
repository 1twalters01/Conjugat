import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

function AuthRequired() {
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        const userToken = localStorage.getItem('token');
        if (!userToken) {
            setIsLoggedIn(false);
            return navigate('/');
        }
        setIsLoggedIn(true);
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

function NotAuthRequired() {
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        const userToken = localStorage.getItem('token');
        if (userToken) {
            setIsLoggedIn(false);
            return navigate('/home')   
        }
        setIsLoggedIn(true);
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

export default {AuthRequired, NotAuthRequired}