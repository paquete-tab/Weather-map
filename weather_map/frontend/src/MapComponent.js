import React, {useState} from "react";
import { MapContainer, TileLayer, Marker, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import ViewWeather from "./ViewWeather";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

function MapComponent() {
    const [latlng, setLatlng] = useState([34.39, 135]);
    const [date, setDate] = useState(new Date());
    const ClickableMap = ({latlng, setLatlng}) => {
        useMapEvents({
            click(e) {
                const { lat, lng } = e.latlng;
                setLatlng([lat, lng]);
                console.log([lat, lng]);
                setDate(new Date());
            },
        });
    
        return (
            <>
                <Marker key="marker" position={latlng} />
            </>
        );
    }
    return (
        <MapContainer center={[34.39, 135]} zoom={5} style={{ height: "100vh", width: "100%" }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            <ClickableMap latlng={latlng} setLatlng={setLatlng} />
            <ViewWeather lat={latlng[0]} lon={latlng[1]} date={date}/>
        </MapContainer>
    );
}

export default MapComponent;