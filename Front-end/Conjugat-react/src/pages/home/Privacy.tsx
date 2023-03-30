import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import '../../sass/pages/home/Privacy.scss'

function Privacy() {
    return (
        <div className="Privacy-container container">
            <div className="Header-spacer">
                <Header />
            </div>

            <div className="navbar">
                <MiscNavbar/>
            </div>

            <div className="para">
                <h1 className="text">Privacy</h1>
                <h3 className="subtitle text">
                    Please note that this Privacy policy is an extract that was copied from Duolingo
                </h3>
                
                <ol>
                    <li className="text">
                        <h3 className="text">General</h3>
                        <p className="text">
                            At Duolingo, we care about your personal data, so we have prepared this Privacy Policy to explain how we collect, use and share it.
                        </p>

                        <p className="text">
                        This Privacy Policy (“Privacy Policy”) details the personal data Duolingo, Inc. (“Duolingo”, “we”, “us” or “our”) receives about you, how we process it and your rights and obligations in relation to your personal data. Duolingo, Inc., a company registered at 5900 Penn Ave, Second Floor, Pittsburgh, PA 15206, United States of America is the data controller for the purposes of the General Data Protection Regulation (“GDPR”) and any relevant local legislation (“Data Protection Laws”).
                        </p>

                        <p className="text">
                        By using or accessing the Service, you agree to the terms of this Privacy Policy. Capitalized terms not defined here have the meanings set forth in the terms and conditions (the “Terms and Conditions”), located at www.duolingo.com/terms. We may update our Privacy Policy to reflect changes to our information practices. If we do this and the changes are material, we will post a notice that we have made changes to this Privacy Policy on the Website for at least 7 days before the changes are made, and we will indicate the date these terms were last revised at the bottom of the Privacy Policy. Any revisions to this Privacy Policy will become effective at the end of that 7 day period.
                        </p>

                        <p className="text">
                        If you are an employee, worker or contractor of Duolingo, the information about how we handle your personal information is available in the Duolingo internal knowledge base. With respect to employees based in Europe, we are committed to cooperating with European data protection authorities (DPAs) and comply with the advice given by such authorities with regard to human resources data transferred from Europe in the context of the employment relationship.
                        </p>
                    </li>

                    <li className="text">
                        <h3 className="text">Information We Collect</h3>
                        <p className="text">
                            This Privacy Policy explains how we collect, use and share your personal data.    
                        </p>

                        <p className="italics text">
                        Information you provide
                        </p>

                        <p className="text">
                        When you use the Service, you will submit information and content to your profile. We will also generate data about your use of our Services including your engagement in educational activities on the Service, or your sending of messages and otherwise transmitting information to other users (“Activity Data”). We also collect technical data about how you interact with our Services; for more information, see Cookies.
                        </p>

                        <p className="italics text">
                        Activity Data
                        </p>

                        <p className="text">
                        When you use Duolingo in our app or on our website, we use a service named FullStory to log your activity. This provides us with a set of data and a session replay of your activity on Duolingo in the form of a video. FullSory captures and analyzes your usage data to help us make your Duolingo experience better.
                        </p>
                    </li>
                </ol>
            </div>
        </div> 
    )
}

export default Privacy