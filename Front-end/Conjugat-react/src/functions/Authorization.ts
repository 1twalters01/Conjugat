import { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom"
import AxiosInstance from "./AxiosInstance";

function AuthRequired() {
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        const userToken = localStorage.getItem('token');

        if (userToken) {
            AxiosInstance.Authorised
            .get('token-validator')
            .then(res => {
                if (res.data !== true) {
                    setIsLoggedIn(false);
                    return navigate('/');
                }
                setIsLoggedIn(true);
            })
            .catch(err => {
                var response
                try {
                    response = err.response.data.detail
                } catch{ response = null }
                if (response == 'Invalid token.') {
                    setIsLoggedIn(false);
                    localStorage.removeItem('token');
                    return navigate('/');
                }
            })
        }
        else {
            setIsLoggedIn(false);
            localStorage.removeItem('token');
            return navigate('/');
        }
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

function NotAuthRequired() {
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
        const userToken = localStorage.getItem('token');
        if (userToken) {
            setIsLoggedIn(true);
            return navigate('/home');
        }
        setIsLoggedIn(false);
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

export default {AuthRequired, NotAuthRequired}