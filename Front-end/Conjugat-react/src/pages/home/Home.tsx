import { useEffect, useState, useRef, MouseEvent } from "react"
import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"
import AxiosInstance from "../../functions/AxiosInstance"

import SettingsNavbar from "../../components/settings/SettingsNavbar"
import HomeChart from "../../components/home/Home/HomeChart"

import { Bar, getElementAtEvent } from 'react-chartjs-2';
import { Chart, registerables, ChartType } from 'chart.js';

Chart.register(...registerables);

function Home() {
    Authorization.AuthRequired()
    type TData = null | {
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
        const formatted_data =
        {
          labels: res.data?.map((data: { Date: String }) => data.Date),
          
          datasets: [{
              label: "Correct",
              data: res.data?.map((data: { Correct: String }) => data.Correct),
              backgroundColor: 'rgba(10, 199, 53, 0.8)',
              hoverBackgroundColor: 'rgba(10, 199, 53, 0.95)',
              borderColor: 'rgba(0,0,0,1)',
              borderWidth: 1,
            },
            {
              label: "Incorrect",
              data: res.data?.map((data: { Incorrect: String }) => data.Incorrect),
              backgroundColor: 'rgba(204, 10, 10, 0.8)',
              hoverBackgroundColor: 'rgba(204, 10, 10, 0.95)',
              borderColor: 'rgba(0,0,0,1)',
              borderWidth: 1,
            }],
        }    
      
        setBasicData(formatted_data)
    }

    useEffect(() => {
      retrieveData()
    }, [])
    
    const options = {

    }

    // const chartRef = useRef<Chart<"bar", number[]>>(null)
    const chartRef = useRef<any>(null)
    const onClick = (event: MouseEvent<HTMLCanvasElement>) => {
      if (getElementAtEvent(chartRef.current, event).length > 0){
        if (getElementAtEvent(chartRef.current, event)[0].datasetIndex === 0){
          console.log('Correct')
        }
        else if(getElementAtEvent(chartRef.current, event)[0].datasetIndex === 1){
          console.log('Incorrect')
        }
      }
    }

    if (basicData != null) {
      return (
        <>
            <SettingsNavbar />
            <div>
                <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
                
                <h1>Home</h1>

                <Bar
                ref={chartRef}
                data={basicData}
                options={options}
                onClick={onClick}
                />
                
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