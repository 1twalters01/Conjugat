import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"

function AuthRequired() {
    const token = localStorage.getItem("token")
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        if (!token) {
            setIsLoggedIn(false);
            return navigate('/');
        }
        setIsLoggedIn(true);
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

function NotAuthRequired() {
    const token = localStorage.getItem("token")
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        if (token) {
            setIsLoggedIn(false);
            return navigate('/home')   
        }
        setIsLoggedIn(true);
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

export default {AuthRequired, NotAuthRequired}