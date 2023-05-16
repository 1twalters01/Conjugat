import { useEffect, useState } from "react"
import { Helmet } from "react-helmet-async"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import { useParams } from "react-router-dom"
import AxiosInstance from "../../functions/AxiosInstance"
import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/verbs/TestResults"

function TestResults() {
    const { testID } = useParams()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    const [answers, setAnswers] = useState([{
        Language: '',
        Base: '',
        Tense: '',
        IDs: [''],
        Subjects: [''],
        Auxiliaries: [""],
        Conjugations: [""],
        Answers: [""],
        Status: [],
    }])

    const fetchdata = async () => {const res = await (
        AxiosInstance.Unauthorised
        .post('verbs/verb-test-results', {
            testID: testID,
        })
        .then(res => {
            setAnswers(res.data)
            console.log(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    )}

    useEffect(() => {
        fetchdata();
    }, [])
    
    return (
        <>
            <Helmet>
                <title>{getTranslation(translations, language, 'Title1')}</title>
                <meta name="description"
                    content={getTranslation(translations, language, 'metaContent1')}
                />
                <link rel="canonical" href="/test/success" />
            </Helmet>
            
            <div>
                {answers.map((answer, i) => (
                    <div>
                        <div className="Header-spacer">
                            <p className="text">{answer.Language}</p>
                            <p className="text">{answer.Base}, {answer.Tense}</p>
                            {answer.IDs.map((result, j) => (
                                <>
                                <p className="text">
                                    {answer.Subjects[j]} {answer.Auxiliaries[j]} {answer.Conjugations[j]}
                                </p>
                                <p className={`${answer.Status[j] == true? 'green-text':'red-text'}`}>
                                    {answer.Answers[j]}
                                </p>
                                </>
                            ))}
                        </div>
                        <br />
                    </div>
                ))}
            </div>
        </>
    )
}

export default TestResults