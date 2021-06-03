import React from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

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

/*const onLoad = {

}*/

//do we want a "load tasks in this area" when someone stops dragging e.g. onDragEnd
//probably onLoad needs to get tasks
function MapComponent() {
    return (
        <LoadScript googleMapsApiKey = "AIzaSyDQmclEsdFsHCs6sjDjBxBF-KNX-GcGCDg" >
            <GoogleMap
                mapContainerStyle = { containerStyle }
                center = { center }
                zoom = { 15 }
                clickableIcons = { false }
                //onLoad = { onLoad }
            />
        </LoadScript>
    )
}

export default MapComponent;