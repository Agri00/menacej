import React, {useState} from 'react';
import Particles from "react-particles";
import Header from './Components/Header'
import Questions from './Components/Questions'
import Homepage from './Components/Homepage';
import { loadFull } from "tsparticles";
import './App.css';




function App() {
    const [login, setLogin] = useState(false)
    const [fillNum, setFillNum] = useState(0)

    const changeLogin = () => {
        setLogin(true)
    }

    const changeFillNum = () => {
        setFillNum++
    }

    function handleSubmit(event) {
        event.preventDefault();
    }

    return ( 
        <div className="App">
            <Header />

            {!login?
                <div>
                    
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
                
                </div> 
            :
            <Questions />}

            {/* <Particles options={particlesOptions} init={particlesInit}/> */}
        </div>
    );

    
}

export default App;
