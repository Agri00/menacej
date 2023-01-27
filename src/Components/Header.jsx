import React from 'react';
import './Header.css';
import friends from './friends.png'

const Header = () => {
    return (
        <div className='siteHeader'>
            <h1>
                Bienvenue
            </h1>
               {/* <img src={friends} className='friends' alt="image d'amis" />  */}
        </div>
    )
}

export default Header