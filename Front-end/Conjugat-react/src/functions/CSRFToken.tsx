import Cookies from 'js-cookie'
import React, { useState, useEffect } from 'react'
import AxiosInstance from './AxiosInstance'

const CSRFToken = () => {
    const [csrftoken, setcsrftoken] = useState('')

    const getCookie = (name: string) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                var cookie = await (AxiosInstance.Authorised.get('account/obtain-csrfToken/'))
                Cookies.set('csrftoken', cookie.data.token)
                console.log(cookie.data.token, 'token')
            } catch (err) {

            }
        }

        fetchData()
        setcsrftoken(getCookie('csrftoken'))
        console.log(csrftoken)
    })
    return (
        <input type='hidden' name='csrfmiddlewaretoken' value={csrftoken} />
    )
}

export default CSRFToken