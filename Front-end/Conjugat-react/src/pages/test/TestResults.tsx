import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import AxiosInstance from "../../functions/AxiosInstance"

function TestResults() {
    const { testID } = useParams()
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
    )
}

export default TestResults