function GetTwitterURL() {
    const getTwitterUrl = () => {
        const rootUrl = ''

        const options = {
            client_id: import.meta.env.VITE_Twitter_OAUTH_CLIENT_ID as string,
            redirect_uri: import.meta.env.VITE_OAUTH_REDIRECT as string,
            response_type: "code",
            prompt: "consent",
            scope: 'email',
            state: 'twitter-Conjugat',
        };
        const qs = new URLSearchParams(options);
        window.location.href = `${rootUrl}?${qs.toString()}`
    }

    return (
        <button onClick={getTwitterUrl}>Twitter</button>
    )
}

export default GetTwitterURL