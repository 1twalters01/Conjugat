import { ChangeEvent, FormEvent, useState } from "react"
import '../../sass/Components/Input fields/TextField.scss'
import '../../sass/Components/Input fields/SubmitBtn.scss'
import '../../sass/pages/verbs/Test.scss'
import AxiosInstance from "../../functions/AxiosInstance"
import { toast } from "react-toastify"

function Test() {
    const [inputValues, setInputValues] = useState({})    

    const handleChange = (e:ChangeEvent<HTMLInputElement>) => {
        setInputValues({...inputValues, [e.target.id]: e.target.value})
    }

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        
        let results = (
            {
                IDs: Object.keys(inputValues),
                answers: Object.values(inputValues),
            }
        )
        
        AxiosInstance.Authorised
        .post('verbs/verb-test', {
            results: results
        })
        .then(res=>{
            
        })
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }

    return (
        <div>
            {exampleQustionData.map((test, i) => (
                <div className='Test-container container'>
                    <div className="Header-spacer">
                        <h1 className="title header">{test.Base.charAt(0).toUpperCase()+test.Base.slice(1)}</h1>
                        <h2 className="subtitle subheader">{test.Tense}</h2>
                    </div>

                    <div className="view-answers-spacer">
                        
                    </div>

                    <div className="form-width">
                        <form action="" key={i} onSubmit={(e) => submit(e)}>
                            {test.IDs.map((id, j) => (
                            
                                <div className="text-spacer" key={id}>
                                    <p className="text">{test.Subjects[j]}</p>
                                    
                                    <div className="text-field">
                                        <input
                                        id={id.toString()}
                                        type="text"
                                        name="text"
                                        className='line'
                                        onChange={(e:ChangeEvent<HTMLInputElement>) => handleChange(e)} />
                                    </div>
                                </div>                   
                            ))}
                            
                            <div className="btn">
                                {i === exampleQustionData.length-1 ?
                                <div className="submit-btn">
                                    <input type="submit" value="Submit" className="strong-btn strong-gold-btn"/>
                                </div>
                                :
                                <div className="submit-btn">
                                    <button type="button"  className="strong-btn strong-gold-btn">Continue</button>
                                </div>
                                
                                }
                            </div>
                            
                        </form> 
                        
                    </div>

                    
                </div>
            ))}
        </div>
    )
}

const idealAnswers = [
    {
        IDs: [1, 5, 6],
        answers: ["am", "are", "ar"],
    }
]

const exampleQustionData = [
    {
        language: 'English',
        Base: 'be',
        Tense: 'Present',
        IDs: [1, 2, 3, 4, 5, 6],
        Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
        Auxiliaries: ["", "", "", "", "", "", ""],
        Verbs: ["am", "are", "is", "are", "are", "are"],
    },
    {
        language: 'English',
        Base: 'have',
        Tense: 'Present',
        IDs: [7, 8, 9, 10, 11, 12],
        Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
        Auxiliaries: ["", "", "", "", "", "", ""],
        Verbs: ["have", "have", "have", "have", "have", "have"],
    },
    {
        language: 'English',
        Base: 'know',
        Tense: 'Present',
        IDs: [25, 14, 15, 16],
        Subjects: ['He/She/It', 'We', 'You', 'They'],
        Auxiliaries: ["", "", "", "", ""],
        Verbs: ["know", "know", "knows", "know"],

    }
]

export default Test