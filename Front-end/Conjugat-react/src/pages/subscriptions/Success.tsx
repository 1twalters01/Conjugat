import { useSelector } from "react-redux"
import { RootState } from "../../redux/store"

import Authorization from '../../functions/Authorization'

import { getTranslation } from "../../functions/getTranslation"
import { translations } from "../../content/subscriptions/Success"

import RetrieveSuccessStatus from "../../components/subscriptions/success/RetrieveSuccessStatus"

function Success() {
    Authorization.AuthRequired()
    const { language } = useSelector((state: RootState) => state.persistedReducer.language)
    return (
        <div>
            <h1>{getTranslation(translations, language, 'Text1')}</h1>

            <RetrieveSuccessStatus />
        </div>
    )
}

export default Success