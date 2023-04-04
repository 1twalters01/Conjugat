import { useState } from 'react'
import '../../../sass/Components/home/FAQ/Dropdowns.scss'

function Dropdowns() {
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
                <h2 className="text subtitle">General questions</h2>
                
                {generalData.map((item, i) => (
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
                <h2 className="text">Account</h2>
                
                {accountData.map((item, j) => (
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

const generalData = [
    {
        question: 'What is conjugat?',
        answer: 'Conjugat is an app made to practice verb conjugations. It is currently on browsers only, though mobile and pc apps will be made soon.'
    },
    {
        question: 'Can you become fluent with conjugat?',
        answer: 'Conjugat alone most likely will not be enough for you to become fluent. It is made to help you become fluent in addition to other things, not by itself alone.'
    },
    {
        question: 'What else should you do to become fluent?',
        answer: 'You should practice the language in practical senses, spending the majority of your time getting input rather than output. This means doing things such as reacing and listening to the language.'
    },
    {
        question: 'What is in the newsletter?',
        answer: 'The newsletter is sent weekly and includes helpful things I find on my language learning journey.'
    }
]

const accountData = [
    {
        question: 'How do I change my username/email/password?',
        answer: 'Go to settings once you have logged in and go to the appropriate section.'
    },
    {
        question: 'How do I reset my account?',
        answer: 'Go to settings once you have logged in and go to the appropriate section.'
    },
    {
        question: 'How do I change the theme?',
        answer: 'Go to settings once you have logged in and go to the appropriate section.'
    }
]

export default Dropdowns