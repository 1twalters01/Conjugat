import { FormEvent, useState } from "react"
import { useDispatch, useSelector } from "react-redux";
import AxiosInstance from "../../../functions/AxiosInstance";
import { onThemeChange } from "../../../redux/slices/themeSlice";
import { RootState } from "../../../redux/store";
import { getTranslation } from '../../../functions/getTranslation'
import { ThemeFunctionalityTranslations } from '../../../content/settings/Themes'
import '../../../sass/Components/settings/Themes/ThemeFunctionality.scss'

function ThemeFunctionality({ language }: { language:string }) {
    const{ theme } = useSelector((state: RootState) => state.persistedReducer.theme)
    const dispatch = useDispatch();

    var init_width
    if (window.innerWidth > 1201) {
      init_width = 125
    }
    else{
      init_width = window.innerWidth/7.5
    }

    const [themeSize, SetThemeSize] = useState(init_width)
    function resizeFunction() {
        var width = window.innerWidth
        if (width > 1201){
            SetThemeSize(125)
        }
        else {
            SetThemeSize(width/7.5)
        }
    }

    window.addEventListener("resize", resizeFunction);

    function submit(choice:string, e:FormEvent<HTMLDivElement>) {
      if (choice != theme) {
        e.preventDefault();

        AxiosInstance.Authorised
        .post('settings/themes/', {
          choice: choice
        })
        .then(res=>{
          dispatch(onThemeChange(res.data.theme))
        })
        .catch(err=>{
          console.log(err)
        })
      }
    }
  
    return(
      <div className="Themes-container" style={{width: `${2*themeSize}px`}}>
        <div onClick={(e) => submit('Dark', e)} style={{height: `${themeSize}px`, width: `${themeSize}px`, background: 'black'}}>
        
        </div>
        {getTranslation(ThemeFunctionalityTranslations, language, 'Dark')}
        <div onClick={(e) => submit('Light', e)} style={{height: `${themeSize}px`, width: `${themeSize}px`, background: 'yellow'}}>
        
        </div>
        {getTranslation(ThemeFunctionalityTranslations, language, 'Light')}
      </div>
    )
}

export default ThemeFunctionality