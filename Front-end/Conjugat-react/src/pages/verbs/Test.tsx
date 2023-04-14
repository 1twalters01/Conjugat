import { ChangeEvent, FormEvent, useEffect, useState } from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../functions/AxiosInstance"
import '../../sass/Components/Input fields/TextField.scss'
import '../../sass/Components/Input fields/SubmitBtn.scss'
import '../../sass/pages/verbs/Test.scss'
import '../../sass/Components/account/DualLinks.scss'
import TextSlideshow from "../../components/test/TestSlideshow"
import TestHeader from "../../components/test/TestHeader"
import TestForm from "../../components/test/TestForm"

function Test() {
    type ITestID = null|number
    const [page, setPage] = useState(0)
    const [inputValues, setInputValues] = useState({})
    const [TestID, setTestID] = useState<ITestID>(null)
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
                number: 50
            })
        )
        console.log(res.data)
        setPage(0)
        SetQuestionData(res.data.Test)
        setTestID(res.data.TestID)
    }

    useEffect(() => {
        fetchdata();
      }, [])

    const handleChange = (e:ChangeEvent<HTMLInputElement>) => {
        setInputValues({...inputValues, [e.target.id]: e.target.value})
    }

    function handleNext(i:number) {
        if (i < QuestionData.length-1) {
            setPage(i + 1)
        }
    }

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        
        let results = (
            {
                TestID: TestID,
                IDs: Object.keys(inputValues),
                answers: Object.values(inputValues),
            }
        )
        
        AxiosInstance.Authorised
        .post('verbs/verb-test', {
            TestID: TestID,
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
                <div className={`Test-container container${page == i ? ' active' : ''}`}>
                    <div className="Header-spacer">
                        <TestHeader
                            test={test}
                        />
                    </div>

                    <div className="view-answers-spacer">
                        <TextSlideshow
                            setPage={setPage}
                            QuestionData={QuestionData}
                            i={i}
                        />
                    </div>

                    <div className="form-width">
                        <TestForm
                            submit={submit}
                            handleNext={handleNext}
                            handleChange={handleChange}
                            QuestionData={QuestionData}
                            test={test}
                            i={i}
                        />
                    </div>
                </div>
            ))}
        </div>
    )
}

// const idealAnswers = [
//     {
//         IDs: [1, 5, 6],
//         answers: ["am", "are", "ar"],
//     }
// ]

// const exampleQustionData = [
//     {
//         language: 'English',
//         Base: 'be',
//         Tense: 'Present',
//         IDs: [1, 2, 3, 4, 5, 6],
//         Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
//         Auxiliaries: ["", "", "", "", "", "", ""],
//         Verbs: ["am", "are", "is", "are", "are", "are"],
//     },
//     {
//         language: 'English',
//         Base: 'have',
//         Tense: 'Present',
//         IDs: [7, 8, 9, 10, 11, 12],
//         Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
//         Auxiliaries: ["", "", "", "", "", "", ""],
//         Verbs: ["have", "have", "have", "have", "have", "have"],
//     },
//     {
//         language: 'English',
//         Base: 'know',
//         Tense: 'Present',
//         IDs: [25, 14, 15, 16],
//         Subjects: ['He/She/It', 'We', 'You', 'They'],
//         Auxiliaries: ["", "", "", "", ""],
//         Verbs: ["know", "know", "knows", "know"],
//     }
// ]

// const exampleQustionDataNew = [
//     {   TestID: 234594,
//         Test: [
//             {
//                 language: 'English',
//                 Base: 'be',
//                 Tense: 'Present',
//                 IDs: [1, 2, 3, 4, 5, 6],
//                 Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
//                 Auxiliaries: ["", "", "", "", "", "", ""],
//                 Verbs: ["am", "are", "is", "are", "are", "are"],
//             },
//             {
//                 language: 'English',
//                 Base: 'have',
//                 Tense: 'Present',
//                 IDs: [7, 8, 9, 10, 11, 12],
//                 Subjects: ['I', 'You', 'He/She/It', 'We', 'You', 'They'],
//                 Auxiliaries: ["", "", "", "", "", "", ""],
//                 Verbs: ["have", "have", "have", "have", "have", "have"],
//             },
//             {
//                 language: 'English',
//                 Base: 'know',
//                 Tense: 'Present',
//                 IDs: [25, 14, 15, 16],
//                 Subjects: ['He/She/It', 'We', 'You', 'They'],
//                 Auxiliaries: ["", "", "", "", ""],
//                 Verbs: ["know", "know", "knows", "know"],
//             }
//         ]
//     }
// ]

export default Test