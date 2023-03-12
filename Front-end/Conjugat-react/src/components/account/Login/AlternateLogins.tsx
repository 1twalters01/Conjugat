function AlternateLogins() {
    return (
      <div className="alternatives">
        <p className="options">Or log-in via:</p>
        <div className="alt-login">
          <a href="{% url 'social:begin' 'facebook' %}"><div className="facebook Facebook-btn"><p>Facebook</p></div></a>
          <a href="{% url 'social:begin' 'google-oauth2' %}"><div className="google Google-btn"><p>Google</p></div></a>
          <a href="{% url 'social:begin' 'twitter' %}"><div className="twitter Twitter-btn"><p>Twitter</p></div></a>
        </div>
      </div>
    )
  }

export default AlternateLogins