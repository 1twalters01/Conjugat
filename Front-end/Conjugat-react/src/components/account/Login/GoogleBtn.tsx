import '../../../sass/Components/account/Login/GoogleBtn.scss'

function GetGoogleURL() {

    const getGoogleUrl = () => {
        const rootUrl = `https://accounts.google.com/o/oauth2/v2/auth`;
      
        const options = {
            redirect_uri: import.meta.env.VITE_OAUTH_REDIRECT as string,
            client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID as string,
            access_type: "offline",
            response_type: "code",
            prompt: "consent",
            scope: [
                "https://www.googleapis.com/auth/userinfo.email",
            ].join(" "),
            state: 'google-oauth2-Conjugat',
        };
      
        const qs = new URLSearchParams(options);
        window.location.href = `${rootUrl}?${qs.toString()}`
    };

    return (
        <button onClick={getGoogleUrl} type='button'
        className="google-btn">Google</button>
    )
}

export default GetGoogleURL