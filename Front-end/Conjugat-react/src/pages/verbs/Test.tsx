import { ChangeEvent, FormEvent, useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { toast } from "react-toastify"
import AxiosInstance from "../../functions/AxiosInstance"
import '../../sass/Components/Input fields/TextField.scss'
import '../../sass/Components/Input fields/SubmitBtn.scss'
import '../../sass/pages/verbs/Test.scss'
import '../../sass/Components/account/DualLinks.scss'

function Test() {
    const [page, setPage] = useState(0)
    const [inputValues, setInputValues] = useState({})
    const [QuestionData, SetQuestionData] = useState([{
        language: '',
        Base: '',
        Tense: '',
        IDs: [''],
        Subjects: [''],
        Auxiliaries: [""],
        Verbs: [""],
    }])

    const fetchdata = async () => {
        const res = await (
            AxiosInstance.Authorised
            .post('verbs/verb-random-retrieval',{
                language: ['English'],
                number: 5
            })
        )
        SetQuestionData(res.data) 
    }

    useEffect(() => {
        fetchdata();
      }, [])

    const handleChange = (e:ChangeEvent<HTMLInputElement>) => {
        setInputValues({...inputValues, [e.target.id]: e.target.value})
    }

    function handlePrevious(i:number) {
        if (i > 0) {
            setPage(i - 1)
        }
    }
    function handleNext(i:number) {
        if (i < QuestionData.length-1)
        setPage(i + 1)
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
            {QuestionData.map((test, i) => (
                // <div className='Test-container container'>
                <div className={`Test-container container${page == i ? ' active' : ''}`}>
                    <div className="Header-spacer">
                        <h1 className="title header">{test.Base.charAt(0).toUpperCase()+test.Base.slice(1)}</h1>
                        <h2 className="subtitle subheader">{test.Tense}</h2>
                    </div>

                    <div className="view-answers-spacer">
                        <div className="dual-links">
                            <div className="link weak-gold-btn" onClick={() =>handlePrevious(i)}>Previous</div>
                            <div className="link weak-gold-btn" onClick={() =>handleNext(i)}>Next</div>
                        </div>
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
                                    <button type="button"  className="strong-btn strong-gold-btn" onClick={() =>handleNext(i)}>Continue</button>
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