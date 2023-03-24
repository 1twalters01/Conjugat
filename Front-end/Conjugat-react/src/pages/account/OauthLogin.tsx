import axios from "axios";
import AxiosInstance from "../../functions/AxiosInstance";

function OauthLogin() {
    const url = window.location.href
    console.log(url)
    console.log(url.match(/code=(.*?)&/i)[1])
    var code = decodeURIComponent(url.match(/code=(.*?)&/i)[1])
    
    console.log(code)

    AxiosInstance.Unauthorised
    .post('api/login/social/knox/google-oauth2/',{
        "code": code
    })
    .then(res => {
        console.log(res.data.token)
        localStorage.setItem("token", res.data.token)
    })

    return (
        <></>
    )
}

export default OauthLogin