import axios from "axios";
import { useDispatch } from "react-redux";
import Authorization from "../../functions/Authorization";
import AxiosInstance from "../../functions/AxiosInstance";
import { onThemeChange } from "../../redux/slices/themeSlice";

function OauthLogin() {
    Authorization.NotAuthRequired()
    const dispatch = useDispatch()

    const url = window.location.href
    var code = decodeURIComponent(url.match(/code=(.*?)&/i)[1])

    AxiosInstance.Unauthorised
    .post('api/login/social/knox/google-oauth2/',{
        "code": code
    })
    .then(res => {
        localStorage.setItem("token", res.data.token)
        axios
        .get('settings/themes/',{
            headers: {
                'Authorization': 'Token '+ localStorage.getItem("token"),
                'Content-Type': 'application/json',
                accept: 'application/json',
            }
        })
        .then((result: { data: { theme: string; }; }) => {
            dispatch(onThemeChange(result.data.theme))
            window.location.href = '/home'
        })
        .catch(err=>{
            console.log(err.response.data)
        })
    })
    .catch(err=>{
        console.log(err.response.data)
    })

    return (
        <></>
    )
}

export default OauthLogin