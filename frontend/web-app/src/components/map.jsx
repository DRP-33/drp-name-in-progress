import React from 'react';
import api from '../api/api'
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

// container style
const containerStyle = {
    width: '80%',
    height: '100vh',
    float: 'right'
};

//center of a map
const center = {
    lat: 51.49954166513176,
    lng: -0.17449287744865882
};

// functional map component
function MapComponent() {
    let [key, setKey] = React.useState(0);
    let [message, setMessage] = React.useState('');
    let [position, setPosition] = React.useState({lat: 0, lng: 0});
    React.useEffect(() => {
        api.getTask().then(function (response){
            setKey(response.data[0].pk);
            setMessage(response.data[0].fields.description);
            setPosition({lat: parseFloat(response.data[0].fields.s_latitude), lng: parseFloat(response.data[0].fields.s_longitude)})
        });
    }, []);

    return (
        <LoadScript googleMapsApiKey = {process.env.REACT_APP_API_KEY} >
            <GoogleMap
                id = { "map" }
                mapContainerStyle = { containerStyle }
                center = { center }
                zoom = { 15 }
                clickableIcons = { false }
            >
                <Marker 
                key = {key} 
                position={position} 
                onClick={() => onClick(key, message)}/>
            </GoogleMap>
        </LoadScript>
    )
}

// For now auto-accepts, for later will display overlay and ask to accept
function onClick(key, message) {
    var formData = new FormData();
    formData.append('id', '3');
    formData.append('acceptor_id', '1');
    api.acceptTask(formData);
    
    document.getElementById('task_text').innerText = message;
}


export default MapComponent;