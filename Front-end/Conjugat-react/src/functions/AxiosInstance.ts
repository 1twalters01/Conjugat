import axios from 'axios'
// import Cookies from 'js-cookie'

// axios.defaults.withCredentials = true
// axios.defaults.xsrfCookieName = 'Cookie'
// axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.baseURL = 'http://conjugat.io:8000/'
axios.defaults.timeout = 5000

const token = localStorage.getItem("token")


const Unauthorised = axios.create({
    headers: {
        'Content-Type': 'application/json',
        accept: 'application/json',
    }
})

const Authorised = axios.create({
    headers: {
        'Authorization': 'Token '+ token,
        'Content-Type': 'application/json',
        accept: 'application/json',
    }
})

export default { Unauthorised, Authorised }