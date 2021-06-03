import React from 'react';

const sidebarStyle = {
    width: "20%",
    float: "left",
    height: "100vh",
    backgroundColor: "#E25353",
    position: "relative"
}

const headingStyle = {
    fontFamily: "Saira",
    fontStyle: "normal",
    fontWeight: 600,
    fontSize: "40px",
    lineHeight: "63px",
    alignItems: "center",
    textAlign: "center",
    color: "#FFFFFF"
}

function Sidebar() {
    return (
        <div style={ sidebarStyle }>
            <h1 style={ headingStyle }>My tasks</h1>
        </div>
    )
};

export default Sidebar;