import { ChangeEvent, FormEvent, useEffect, useState } from "react"
import { FontFormTranslations } from "../../../content/settings/Font"
import { getTranslation } from "../../../functions/getTranslation"
import SubmitBtn from "../../Buttons/SubmitBtn"
import SelectField from "../../Input fields/SelectField"
import AxiosInstance from "../../../functions/AxiosInstance"
import { onFontChange } from "../../../redux/slices/fontSlice"
import { toast } from "react-toastify"

function FontForm({language}: {language:string}) {
    // fetch list of supported fonts from settings/font/read/
    // Post on update of font to settings/font/
    type TFetchedFonts = {
        "font": '',
        "typeface": ''
    }[]

    const [fetchedFonts, setfetchedFonts] = useState<TFetchedFonts>([])
    const [typeface, setTypeface] = useState<string[]>([])
    const [FieldList, setFieldList] = useState<string[]>([])
    const [font, setFont] = useState<string>('')

    const fetchdata = async () => {
        const res = await (
            AxiosInstance.Authorised
            .get('settings/font/read/')
        )
        console.log(res.data.fonts)
        console.log(res.data.typefaces)
        setfetchedFonts(res.data.fonts)
        setTypeface(res.data.typefaces)
    }

    useEffect(() => {
        fetchdata()
    }, [])

    const updateFieldlist = async () => {
        const fontHolder: string[] = []
        
        fetchedFonts.map((font, i) => (font.typeface in fetchedFonts) ?
            fontHolder.push(font["font"]) :
            fontHolder.push()
        )
        setFieldList(fontHolder)
    }

    useEffect(() =>{
        updateFieldlist()
    }, [typeface])

    function changeFont(e:ChangeEvent<HTMLSelectElement>) {
        setFont(e.target.value)
    }

    function submit(e:FormEvent<HTMLFormElement>) {
        e.preventDefault();
        AxiosInstance.Authorised
        .post('settings/font/', {
          font: font,
        })
        .then(res=>{
            dispatch(onFontChange(res.data.font))
        })
        .catch(err=>{
          toast.error(err.response.data.error)
        })
    }

    return (
        <div>
            <form onSubmit={(e) => submit(e)}>
                <div className="password-spacer">
                    <SelectField
                    labelText={getTranslation(FontFormTranslations, language, 'Select')}
                    field={[font]}
                    changeField={changeFont}
                    FieldList = {FieldList}
                    FieldListValues = {FieldList}
                    />
                </div>

                <SubmitBtn
                    value={getTranslation(FontFormTranslations, language, 'Submit')}
                    style="strong-red-btn"
                />
            </form>
        </div>
    )
}

export default FontForm

function dispatch(arg0: { payload: string; type: "font/onFontChange" }) {
    throw new Error("Function not implemented.")
}
