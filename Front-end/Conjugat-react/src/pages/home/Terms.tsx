import Header from "../../components/account/Header"
import MiscNavbar from "../../components/home/MiscNavbar"
import '../../sass/pages/home/Terms.scss'

function Terms() {
    return (
        <div className="Terms-container container">
            <div className="Header-spacer">
                <Header />
            </div>

            <div className="navbar">
                <MiscNavbar/>
            </div>

            <div className="para">
                <h1 className="text">Terms</h1>
                <h3 className="subtitle text">
                    Please note that these Terms and Conditions of Service are an extract that was copied from Duolingo
                </h3>
                
                <ol>
                    <li className="text">
                        <h3 className="text">General</h3>
                        <p className="text">Duolingo websites (“Websites”), mobile applications (“Apps”), and related services (together with the Websites and Apps, the “Service”) are operated by Duolingo, Inc. (“Duolingo,” “us,” or “we”). Access and use of the Service is subject to the following Terms and Conditions of Service (“Terms and Conditions”). By accessing or using any part of the Service, you represent that you have read, understood, and agree to be bound by these Terms and Conditions including any future modifications. Duolingo may amend, update, or change these Terms and Conditions. If we do this, we will post a notice that we have made changes to these Terms and Conditions on the Websites for at least 7 days after the changes are posted and will indicate at the bottom of the Terms and Conditions the date these terms were last revised. Any revisions to these Terms and Conditions will become effective the earlier of (i) the end of such 7-day period or (ii) the first time you access or use the Service after such changes. If you do not agree to abide by these Terms and Conditions, you are not authorized to use, access, or participate in the Service.</p>

                        <p className="text bold"><span>PLEASE NOTE THAT THESE TERMS AND CONDITIONS CONTAIN A MANDATORY ARBITRATION OF DISPUTES PROVISION THAT REQUIRES THE USE OF ARBITRATION ON AN INDIVIDUAL BASIS TO RESOLVE DISPUTES IN CERTAIN CIRCUMSTANCES, RATHER THAN JURY TRIALS OR CLASS ACTION LAWSUITS. VIEW THESE TERMS HERE.
                        </span></p>
                    </li>

                    <li className="text">
                        <h3 className="text">Description of Website and Service</h3>
                        <p className="text">The Service allows users to access and use a variety of educational services, including learning or practicing a language. Duolingo may, in its sole discretion and at any time, update, change, suspend, make improvements to or discontinue any aspect of the Service, temporarily or permanently.</p>
                    </li>

                    <li className="text">
                        <h3 className="text">Acceptable Use of the Services</h3>
                        <p className="text">You are responsible for your use of the Services, and for any use of the Services made using your account. Our goal is to create a positive, useful, and safe user experience. To promote this goal, we prohibit certain kinds of conduct that may be harmful to other users or to us. When you use the Services, you must comply with our Community Guidelines.</p>
                    </li>

                    <li className="text">
                        <h3 className="text">Additional Terms</h3>
                        <p className="text">Some of our Services have additional terms and conditions (“Additional Terms”). Where Additional Terms apply to a Service, we will make them available for you to read through your use of that Service. By using that Service, you agree to the Additional Terms.</p>
                    </li>

                    <li className="text">
                        <h3 className="text">Registration</h3>
                        <p className="text">In connection with registering for and using the Service, you agree (i) to provide accurate, current and complete information about you and/or your organization as requested by Duolingo; (ii) to maintain the confidentiality of your password and other information related to the security of your account; (iii) to maintain and promptly update any registration information you provide to Duolingo, to keep such information accurate, current and complete; and (iv) to be fully responsible for all use of your account and for any actions that take place through your account.</p>
                    </li>

                    <li className="text">
                        <h3 className="text">Your Representations and Warranties</h3>
                        <p className="text">You represent and warrant to Duolingo that your access and use of the Service will be in accordance with these Terms and Conditions and with all applicable laws, rules, and regulations of the United States and any other relevant jurisdiction, including those regarding online conduct or acceptable content, and those regarding the transmission of data or information exported from the United States and/or the jurisdiction in which you reside. You further represent and warrant that you have created or own any material you submit via the Service (including Activity Materials and Content) and that you have the right, as applicable, to grant us a license to use that material as set forth above or the right to assign that material to us as set forth below.</p>

                        <p className="text">You represent and warrant that you are not: (1) organized under the laws of, operating from, or otherwise ordinarily resident in a country or territory that is the target of comprehensive U.S. economic or trade sanctions (i.e., an embargo); (2) identified on a list of prohibited or restricted persons, such as the U.S. Treasury Department’s List of Specially Designated Nationals and Blocked Persons; or (3) otherwise the target of U.S. sanctions.</p>
                    </li>
                </ol>
            </div>
        </div> 
    )
}

export default Terms