import '../../../sass/Components/account/Login/FacebookBtn.scss'

function GetFacebookURL() {
    const getFacebookUrl = () => {
        const rootUrl = 'https://www.facebook.com/v16.0/dialog/oauth'

        const options = {
            client_id: import.meta.env.VITE_FACEBOOK_OAUTH_APP_ID as string,
            redirect_uri: import.meta.env.VITE_OAUTH_REDIRECT as string,
            response_type: "code",
            prompt: "consent",
            scope: 'email',
            state: 'facebook-Conjugat',
        };
        const qs = new URLSearchParams(options);
        window.location.href = `${rootUrl}?${qs.toString()}`
    }

    return (
        <button type='button' className="btn-fb" onClick={getFacebookUrl}>
            <div className="fb-content">
                <div className="logo">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" version="1">
                        <path fill="#FFFFFF" d="M32 30a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h28a2 2 0 0 1 2 2v28z"/>
                        <path fill="#4267b2" d="M22 32V20h4l1-5h-5v-2c0-2 1.002-3 3-3h2V5h-4c-3.675 0-6 2.881-6 7v3h-4v5h4v12h5z"/>
                    </svg>
                </div>
                <p>Facebook</p>
            </div>
        </button>
    )
}

export default GetFacebookURL