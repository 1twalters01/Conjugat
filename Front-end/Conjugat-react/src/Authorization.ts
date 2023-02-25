import React, { useEffect, useState } from "react"
import { Route, useNavigate } from "react-router-dom"

function AuthRequired() {
    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const checkUserToken = () => {
    const userToken = localStorage.getItem('token');
    if (!userToken) {
        setIsLoggedIn(false);
        return navigate('/account/login');
    }
    setIsLoggedIn(true);
    }
    useEffect(() => {checkUserToken()}, [isLoggedIn]);
}

function NotAuthRequired() {
    const navigate = useNavigate();
    const [isNotLoggedIn, setIsLoggedIn] = useState(true);
    const checkUserToken = () => {
    const userToken = localStorage.getItem('token');
    if (userToken) {
        setIsLoggedIn(true);
        return navigate('/home')   
    }
    setIsLoggedIn(false);
    }
    useEffect(() => {checkUserToken()}, [isNotLoggedIn]);
}

export default {AuthRequired, NotAuthRequired}