import React from 'react'
import MapComponent from './components/map.jsx'
import Sidebar from './components/Sidebar.jsx'
//import Pin from './components/pin.jsx'

// DEF REMOVE THIS
// const position = { lat: 51.501169613351145, lng: -0.18215957215504935};
// const pin = new Pin({
//     position: position,
//     key: 1,
//     icon: "../assets/location-pin.svg"
// })
// const pins = [pin]

const MapViewStyle = {
    height: "100vh",
    width: "100%"
}

function App() {
    return (
        <div style={MapViewStyle}>
            <Sidebar/>
            <MapComponent/>
        </div>
    )
}

export default App;