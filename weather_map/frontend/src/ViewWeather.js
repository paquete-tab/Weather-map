import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Control from 'react-leaflet-custom-control';

function ViewWeather({lat, lon, date}) {
    const [data, setData] = useState(null);

    useEffect(() => {
      setData(null);
      const params = {
        lat: lat,
        lon: lon,
        year: date.getFullYear(),
        month: date.getMonth()+1,
        day: date.getDate()
      }
      axios.post(`http://ec2-54-183-158-158.us-west-1.compute.amazonaws.com/api/`, params)
        .then(response => {
          setData(response.data);
        })
        .catch(error => {
          console.error('There was an error fetching the data!', error);
        });
    }, [lat, lon, date]);

    return (
      <Control position='topright'>
          {data ? (
            <div>
              <p>{date.getFullYear()}年{date.getMonth()+1}月{date.getDate()}日</p>
              <p>{data["city"]}</p>
              <p>Weather: {data["weather"]}</p>
            </div>
          ) : (
            <p>Loading...</p>
          )}
      </Control>
    );
}

export default ViewWeather;
