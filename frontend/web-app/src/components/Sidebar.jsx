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
    color: "#FFFFFF",
    padding: "2%"
}

const bodyStyle = {
    fontFamily: "Saira",
    fontStyle: "normal",
    fontWeight: 600,
    fontSize: "16px",
    lineHeight: "25px",
    alignItems: "center",
    textAlign: "center",
    color: "#FFFFFF",
    padding: "2%"
}

function Sidebar() {
    return (
        <div style={ sidebarStyle }>
            <h1 style={ headingStyle }>My tasks</h1>
            <h2 id="task_text" style={ bodyStyle }></h2>
        </div>
    )
};

export default Sidebar;