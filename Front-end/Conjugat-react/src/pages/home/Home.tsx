import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import Authorization from "../../functions/Authorization"
import AxiosInstance from "../../functions/AxiosInstance"

import SettingsNavbar from "../../components/settings/SettingsNavbar"
import HomeChart from "../../components/home/Home/HomeChart"

import { Bar } from 'react-chartjs-2';
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);


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
    // const [basicData, setBasicData] = useState<TData>({
    //   labels: ['2023-04-19', '2023-04-20','2023-04-22', '2023-04-23'],
    //     datasets: [{
    //       label: "Test Results",
    //       data: [5, 4, 8, 1]
    //     }]
    //   }
    // )

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
              data: res.data?.map((data: { Correct: String }) => data.Correct[0]),
              backgroundColor: 'rgba(10, 199, 53, 0.8)',
              hoverBackgroundColor: 'rgba(10, 199, 53, 0.95)',
              borderColor: 'rgba(0,0,0,1)',
              borderWidth: 1,
            },
            {
              label: "Incorrect",
              data: res.data?.map((data: { Incorrect: String }) => data.Incorrect[0]),
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
    // console.log(basicData)

    if (basicData != null) {
      return (
        <>
            <SettingsNavbar />
            <div>
                <Link to='../subscriptions/' className="text-blue-link">Subscribe</Link>
                
                <h1>Home</h1>

                <Bar data={basicData} options={{
                  color: "white",
                }}/>
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