import { useState } from 'react'
import { getTranslation, getTranslationList } from '../../../functions/getTranslation'
import { dropdownTranslations, generalData, accountData } from "../../../content/home/Faq"
import '../../../sass/Components/home/FAQ/Dropdowns.scss'


function Dropdowns({language}: {language:string}) {
    type TSelected = number|null
    const [generalSelected, setGeneralSelected] = useState<TSelected>(null)
    const [actionSelect, setActionSelected] = useState<TSelected>(null)

    const generalToggle = (i:number) => {
        if(generalSelected == i) {
            return setGeneralSelected(null)
        }
        setGeneralSelected(i)
    }
    const actionToggle = (j:number) => {
        if(actionSelect == j) {
            return setActionSelected(null)
        }
        setActionSelected(j)
    }

    return(
        <div className="Dropdown-container">

            <div className="section">
                <h2 className="text subtitle">{getTranslation(dropdownTranslations, language, 'Title1')}</h2>
                
                {getTranslationList(generalData, language).map((item:any, i:number) => (
                    <div className={`faq${generalSelected == i ? ' active' : ''}`} onClick={() => generalToggle(i)}>
                        <h3 className="question text-blue-link">
                            {item.question}
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className='text' viewBox="0 0 16 16">
                                <path d="M3.204 5h9.592L8 10.481 3.204 5zm-.753.659 4.796 5.48a1 1 0 0 0 1.506 0l4.796-5.48c.566-.647.106-1.659-.753-1.659H3.204a1 1 0 0 0-.753 1.659z"/>
                            </svg>
                        </h3>
                        
                        <div className="answer">
                            <p className='text'>{item.answer}</p>
                        </div>
                    </div>
                ))}
            </div>
            
            <div className="section">
                <h2 className="text">{getTranslation(dropdownTranslations, language, 'Title2')}</h2>
                
                {getTranslationList(accountData, language).map((item:any, j:number) => (
                    <div className={`faq${actionSelect == j ? ' active' : ''}`} onClick={() => actionToggle(j)}>
                        <h3 className="question text-blue-link">
                            {item.question}
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className='text' viewBox="0 0 16 16">
                                <path d="M3.204 5h9.592L8 10.481 3.204 5zm-.753.659 4.796 5.48a1 1 0 0 0 1.506 0l4.796-5.48c.566-.647.106-1.659-.753-1.659H3.204a1 1 0 0 0-.753 1.659z"/>
                            </svg>
                        </h3>

                        
                        <div className="answer">
                            <p className='text'>{item.answer}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}



export default Dropdowns