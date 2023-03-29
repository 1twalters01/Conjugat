import { useRef } from 'react';
import { Link } from 'react-router-dom'
import '../../../sass/Components/home/Landing page/TopContainer.scss'

function TopContainer() {
    const para1 = useRef(null);
    const para2 = useRef(null);
    const dot1 = useRef(null);
    const dot2 = useRef(null);
    
    function leftBtn() {
        para1.current.style.display = "block"
        para2.current.style.display = "none"
        dot1.current.style.backgroundColor = '#00c04b'
        dot2.current.style.backgroundColor = '#b9b8b9'
    }
    function rightBtn() {
        para1.current.style.display = "none"
        para2.current.style.display = "block"
        dot1.current.style.backgroundColor = "#b9b8b9"
        dot2.current.style.backgroundColor = "#00c04b"
    }
    return (
        <div className="Landing-page-top-container">
            <div className="right-container">
                <p className='text'>Image will go here</p>
            </div>
            <div className="left-container">
                <div className="title">
                    <h1 className='header'>Conjugat Premium</h1>
                    <h2 className='subheader'>Helping you to perfect your verb conjugations</h2>
                </div>
                <div className="main-section">
                    <div className="paragraphs">
                        <div className="para para-1" ref={para1}>
                            <p className="text">At Conjugat we are here to help you learn verbs and tenses in the order that you will be most likely to encounter them. We use spaced repetition to get you to memorise them.</p>
                            <p className="text">We have 5 languages to choose from and growing. Perfect any of our growing list of languages to be able to make friends on your travels around the globe.</p>
                        </div>
                        <div className="para para-2" ref={para2}>
                            <p className="text">We have 2000 verbs for each language so you won't mess up your grammar again. Practice all of the different types of irregular verbs and never make a mistake with them again.</p>
                            <p className="text">Practice more than just verbs - you can practice noun and adjective genders in the same fun way with Conjugat Premium. Let us know what else we should add! </p>
                        </div>
                    </div>
                    
                    <div className="carousel-btns">
                        <div>
                            <span className="dot dot-1" ref={dot1} onClick={leftBtn}></span>
                            <span className="dot dot-2" ref={dot2} onClick={rightBtn}></span>
                        </div>
                    </div>
                </div>


                <Link to='/account/register'>
                    <p className="join strong-blue-btn">Join now</p>
                </Link>
            </div>
    
            
        </div>
    )
}

export default TopContainer