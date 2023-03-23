import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const baseURL = 'http://conjugat.io:8000/'
const token = localStorage.getItem("token")
const timeout = 5000

const Unauthorised = axios.create({
    baseURL: baseURL,
    timeout: timeout,
    headers: {
        'Content-Type': 'application/json',
        accept: 'application/json',
    }
})

const Authorised = axios.create({
    baseURL: baseURL,
    timeout: timeout,
    headers: {
        'Authorization': 'Token '+ token,
        'Content-Type': 'application/json',
        accept: 'application/json',
    }
})

export default { Unauthorised, Authorised }