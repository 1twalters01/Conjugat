import { ChangeEvent, FormEvent, useEffect, useState } from "react"
import { toast } from "react-toastify"
import AxiosInstance from "../../functions/AxiosInstance"
import TextSlideshow from "../../components/test/TestSlideshow"
import TestHeader from "../../components/test/TestHeader"
import TestForm from "../../components/test/TestForm"
import SettingsNavbar from "../../components/settings/SettingsNavbar"
import '../../sass/Components/Input fields/TextField.scss'
import '../../sass/Components/Input fields/SubmitBtn.scss'
import '../../sass/Components/account/DualLinks.scss'
import '../../sass/pages/verbs/Test.scss'
import { useNavigate } from "react-router-dom"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"

function Test() {
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    
    const navigate = useNavigate()
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
            navigate(`/verbs/test/results/${res.data}`)
            
        })
        .catch(err=>{
            toast.error(err.response.data.error)
        })
    }

    return (
        <div>
            <div className="Settings-navbar-container container">
                <SettingsNavbar language={language} />
            </div>

            {QuestionData.map((test, i) => (
                <div className={`Test-container container${page == i ? ' active' : ''}`}>
                    <div className="Header-spacer">
                        <TestHeader
                            test={test}
                        />
                    </div>

                    <div className="view-answers-spacer">
                        <TextSlideshow
                            language={language}
                            setPage={setPage}
                            QuestionData={QuestionData}
                            i={i}
                        />
                    </div>

                    <div className="form-width">
                        <TestForm
                            language={language}
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

export default Test