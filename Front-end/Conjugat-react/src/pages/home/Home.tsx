import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"
import AxiosInstance from "../../functions/AxiosInstance"

import SettingsNavbar from "../../components/settings/SettingsNavbar"
import HomeChart from "../../components/home/Home/HomeChart"


import {Bar} from 'react-chartjs-2'
import {Chart as ChartJS} from 'chart.js/auto'

function Home() {
    Authorization.AuthRequired()
    type TData = null|{
        labels: any;
        datasets: {
            label: string;
            data: any;
        }[];
    }
    const [basicData, setBasicData] = useState<TData>(null)
    async function retrieveData() {
      const res = await(
        AxiosInstance.Authorised
        .get('/home')
      )
      const formatted_data = {
        labels: res.data?.map((data: { Date: String }) => data.Date),
        datasets: [{
          label: "Test Results",
          data: res.data?.map((data: { Correct: String }) => data.Correct)
        }],
      }
      setBasicData(formatted_data)
      
    }

    useEffect(() => {
      retrieveData()
    }, [])
    console.log(basicData)

    if (basicData != null) {
      return (
        <>
            <SettingsNavbar />
            <div>
                <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
                
                <h1>Home</h1>

                <Bar data={basicData}/>
                
                
                <br />
            </div>
        </>
      )
    }
    else{
        return(
            <></>
        )
    }
}

export default Home