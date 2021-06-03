import React from 'react'
import MapComponent from './components/map.jsx'
import Sidebar from './components/Sidebar.jsx'

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