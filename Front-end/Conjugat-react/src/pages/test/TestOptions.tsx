import { useState } from "react"
import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"
import SettingsNavbar from "../../components/settings/SettingsNavbar"
import TestNavbar from "../../components/test/Test Options/TestNavbar"
import ExampleTest from "../../components/test/Test Options/ExampleTest"
import TestControls from "../../components/test/Test Options/TestControls"
import TestSettings from "../../components/test/Test Options/TestSettings"


function TestOptions() {
    type TtimerBool = null | {
        'timerBool':boolean,
        'timer': Number
    }

    const { language } = useSelector((state: RootState) => state.persistedReducer.language)

    const [mode, setMode] = useState() // Battle mode, Teacher mode, etc.
    const [wordtype, setWordType] = useState() // Verbs, Nouns, Adjectives, etc.
    const [languageChoices, setLanguageChoices] = useState([])
    const [sentenceBool, setSentenceBool] = useState<null|Boolean>(null) // single or sentences
    const [checkAccents, setCheckAccents] = useState()

    const [timerBool, setTimerBool] = useState<TtimerBool>(null)
    const [timer, setTimer] = useState()
    const [questionCount, setQuestionCount] = useState()

    return (
        <div>
            <SettingsNavbar language={language} />

            <div>
                <TestNavbar />
            </div>

            <div>
                <ExampleTest />
            </div>

            <div>
                <TestControls />
            </div>

            <div>
                <TestSettings />
            </div>
        </div>
    )
}

export default TestOptions