import React from 'react';
//import ReactDOM from 'react-dom'
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
    width: '80%',
    height: '100vh',
    float: 'right'
};

// need this to be CURRENT LOCATION/user's default address?
const center = {
    lat: 51.49954166513176,
    lng: -0.17449287744865882
};

//NEED TO GET DETAILS, POSITION AND KEY FROM DB
const key = 1
const position = {
    lat: 51.501169613351145,
    lng: -0.18215957215504935  
}
const details = "These are some bits of tasks details"

// For now auto-accepts, for later will display overlay and ask to accept
function onClick() {
    document.getElementById("task text").innerText = details
    // acceptRequest()
    // retrieve info for pin and replace with this

    return
}

/*function onLoad() {
    const marker = new Marker({
        key: 1,
        position: { lat: 51.501169613351145, lng: -0.18215957215504935},
        //icon: "../assets/image.jpg",
        map: document.getElementById("map"),
        clickable: true,
        visible: true
    });
    console.log(marker)
    //ReactDOM.render(marker, document.getElementById("root"));
}*/

//do we want a "load tasks in this area" when someone stops dragging e.g. onDragEnd
//probably onLoad needs to get tasks
function MapComponent() {
    return (
        <LoadScript googleMapsApiKey = "AIzaSyDQmclEsdFsHCs6sjDjBxBF-KNX-GcGCDg" >
            <GoogleMap
                id = { "map" }
                mapContainerStyle = { containerStyle }
                center = { center }
                zoom = { 15 }
                clickableIcons = { false }
            >
                <Marker key={key} position={position} onClick={onClick}/>
            </GoogleMap>
        </LoadScript>
    )
}

export default MapComponent;