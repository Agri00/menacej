import React, {useState} from "react";
import { EventListeners } from "tsparticles-engine";
import './Homepage.css'

var isLoggedIn = false

const Homepage = (props) => {
    const [loga, setLogin] = useState(false)
    const [fillNum, setFillNum] = useState(0)

    function handleSubmit(event) {
        event.preventDefault();
    }

    const changeFillNum = () => {
        setFillNum(1)
        console.log(fillNum)
    }

    const changeLogin = () => {
        setLogin(true)
    }

    return (
    <div className="formComponent">
        <p className="title">Insére tes informations: </p>
        <form onSubmit={handleSubmit}>
            <input type="text" id="fname" name="fname" placeholder="Prénom" onChange={changeFillNum} required/> <br />
            <input type="text" id="lname" name="lname" placeholder="Nom" onChange={changeFillNum} required/> <br />
            <input type="text" id="class" name="class" placeholder="Classe" onChange={changeFillNum} required/> <br />
            <input type="text" id="number" name="number" placeholder="Numéro" onChange={changeFillNum} required/> <br />
            <button type="submit" className="submitClass" onClick={changeLogin} > 
                        Submit
            </button>    
        </form>
    </div>
    );
    
}

export default Homepage;