import axios from "axios";
import { useDispatch } from "react-redux";
import Authorization from "../../functions/Authorization";
import AxiosInstance from "../../functions/AxiosInstance";
import { onThemeChange } from "../../redux/slices/themeSlice";


// I am repeating the functions here as I don't know if the twitter one works yet
// Refactoring once I do will be easier than the other way
// I am waiting for Twitter to accept my pettition for api usage

function OauthLogin() {
    Authorization.NotAuthRequired()
    const dispatch = useDispatch()

    const url = window.location.href
    if (url.includes('google')) {
        var code:string|null = decodeURIComponent(url.match(/code=(.*?)&/i)[1])
        AxiosInstance.Unauthorised
        .post('account/login/Oauth/social/knox/google-oauth2/',{
            "code": code
        })
        .then(res => {
            localStorage.setItem("token", res.data.token)
            axios
            .get ('settings/themes/', {
                headers: {
                    'Authorization': 'Token '+ localStorage.getItem("token"),
                    'Content-Type': 'application/json',
                    accept: 'application/json',
                }
            })
            .then ((result: { data: { theme: string; }; }) => {
                dispatch(onThemeChange(result.data.theme))
                window.location.href = '/home'
            })
            .catch (err=>{
                console.log(err.response.data)
            })
        })
        .catch(err=>{
            console.log(err.response.data)
        })
    }

    else if (url.includes('facebook')) {
        var code:string|null = decodeURIComponent(url.match(/code=(.*?)&/i)[1])
        AxiosInstance.Unauthorised
        .post('account/login/Oauth/social/knox/facebook/',{
            "code": code
        })
        .then(res => {
            localStorage.setItem("token", res.data.token)
            axios
            .get ('settings/themes/', {
                headers: {
                    'Authorization': 'Token '+ localStorage.getItem("token"),
                    'Content-Type': 'application/json',
                    accept: 'application/json',
                }
            })
            .then ((result: { data: { theme: string; }; }) => {
                dispatch(onThemeChange(result.data.theme))
                window.location.href = '/home'
            })
            .catch (err=>{
                console.log(err.response.data)
            })
        })
        .catch(err=>{
            console.log(err.response.data)
        })
    }

    else if (url.includes('twitter')) {
        console.log('twitter')
    }
    
    return (
        <p className="text">Loading...</p>
    )
}

export default OauthLogin