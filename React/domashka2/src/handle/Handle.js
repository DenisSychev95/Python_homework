import React from "react";
import "./Handle.css"

class Handle extends React.Component {

    state = {
        val: ""
    }

    changeValue = (event) => {
        document.querySelector("#one").className= "Visible";
        document.querySelector("#two").className= "Visible";

        this.setState({ val: event.target.value })
    }

    render() {
        return (
            <div className="App">
                <div>
                    Выберите размер квадрата:
                </div>
                <div>
                    <input type="range" name="range" id="range" min={30} max={300} onChange={this.changeValue} />
                </div>
                <div id="one" className="Hidden" >{this.state.val}px * {this.state.val}px</div>
                <div id="two" className="Hidden" style={{ width: `${this.state.val}px`, height: `${this.state.val}px`, }}></div>
            </div>
        );
    }

}

export default Handle