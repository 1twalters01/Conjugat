import { useRef } from 'react';
import { useSelector } from "react-redux"
import { RootState } from '../../../redux/store';
import { Link } from 'react-router-dom'
import { translations } from '../../../content/home/Landing page/TopContainer'
import '../../../sass/Components/home/Landing page/TopContainer.scss'


function TopContainer() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const getTranslation = (language, text) => {
        return translations[language][text];
    }

    const para1 = useRef<HTMLDivElement>(null);
    const para2 = useRef<HTMLDivElement>(null);
    const dot1 = useRef<HTMLSpanElement>(null);
    const dot2 = useRef<HTMLSpanElement>(null);
    
    function leftBtn() {
        // https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#non-null-assertion-operator-postfix-
        para1.current!.style.display = "block"
        para2.current!.style.display = "none"
        dot1.current!.style.backgroundColor = '#00c04b'
        dot2.current!.style.backgroundColor = '#b9b8b9'
    }
    function rightBtn() {
        para1.current!.style.display = "none"
        para2.current!.style.display = "block"
        dot1.current!.style.backgroundColor = "#b9b8b9"
        dot2.current!.style.backgroundColor = "#00c04b"
    }
    return (
        <div className="Landing-page-top-container">
            <div className="right-container">
                <p className='text'>Image will go here</p>
            </div>
            <div className="left-container">
                <div className="title">
                    <h1 className='header'>Conjugat</h1>
                    <h2 className='subheader'>{getTranslation(language, 'Subheader')}</h2>
                </div>
                <div className="main-section">
                    <div className="paragraphs">
                        <div className="para para-1" ref={para1}>
                            <p className="text">{getTranslation(language, 'Text1')}</p>
                            <p className="text">{getTranslation(language, 'Text2')}</p>
                        </div>
                        <div className="para para-2" ref={para2}>
                            <p className="text">{getTranslation(language, 'Text3')}</p>
                            <p className="text">{getTranslation(language, 'Text4')}</p>
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