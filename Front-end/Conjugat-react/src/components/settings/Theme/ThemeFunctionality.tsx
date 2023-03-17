import { FormEvent } from "react"
import { useDispatch } from "react-redux";
import AxiosInstance from "../../../functions/AxiosInstance";
import { onThemeChange } from "../../../redux/slices/themeSlice";

function ThemeFunctionality() {
  const dispatch = useDispatch();
    function submitDark(e:FormEvent<HTMLDivElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/themes/', {
        choice: 'Dark'
      })
      .then(res=>{
        console.log(typeof res.data.theme, res.data.theme)
        dispatch(onThemeChange(res.data.theme))
      })
      .catch(err=>{
        console.log(err)
      })
    }
    
    function submitLight(e:FormEvent<HTMLDivElement>) {
      e.preventDefault();
      AxiosInstance.Authorised
      .post('settings/themes/', {
        choice: 'Light'
      })
      .then(res=>{
        console.log(typeof res.data.theme, res.data.theme)
        dispatch(onThemeChange(res.data.theme))
      })
      .catch(err=>{
        console.log(err)
      })
    }
  
    return(
      <div>
        <div onClick={(e) => submitDark(e)} style={{height: '200px', width: '200px', background: 'black'}}>
        
        </div>
        <div onClick={(e) => submitLight(e)} style={{height: '200px', width: '200px', background: 'yellow'}}>
        
        </div>
      </div>
    )
}

export default ThemeFunctionality