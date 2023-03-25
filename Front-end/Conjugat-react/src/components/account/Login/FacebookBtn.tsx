function GetFacebookURL() {
    const getFacebookUrl = () => {
        const rootUrl = 'https://www.facebook.com/v16.0/dialog/oauth?'

        const options = {
            client_id: import.meta.env.VITE_FACEBOOK_OAUTH_APP_ID as string,
            redirect_uri: import.meta.env.VITE_OAUTH_REDIRECT as string,
            response_type: "code",
            prompt: "consent",
            scope: 'email',
            state: 'facebook-Conjugat',
        };
        const qs = new URLSearchParams(options);
        window.location.href = `${rootUrl}${qs.toString()}`
    }

    return (
        <button onClick={getFacebookUrl}>Facebook</button>
    )
}

export default GetFacebookURL