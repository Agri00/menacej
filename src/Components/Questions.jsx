import React, {useState} from 'react'
import './Questions.css'

const Questions = () => {
    const [questions, SetAnswer] = useState([
    {
        id: 1,
        quest: 'Tu es en quelle classe?',
        options: ['Seconde', 'Premiere', 'Terminale'],
    }, 
    {
        id: 2,
        quest:'Avec qui veux tu être mis en binôme ? ',
        options:['Gars', 'Fille', 'Les deux', 'Peu importe'],
        
    },
    {
        id: 3,
        quest:'Ton premier date idéal:',
        options:['Au macdo', 'Se balader dans un parc', 'Rdv romantique'],
    },
    {
        id: 4,
        quest:'Tu te qualifierais d’une personne:',
        options:['Sociable', 'Franche', 'Attentionnée', 'Drôle'],
    },
    {
        id: 5,
        quest:'La qualité que tu recherches chez la personne:',
        options:['Sociable', 'Franche', 'Attentionnée', 'Drôle'],
    },
    {
        id: 6,
        quest:'Ton principal défaut:',
        options:['Jalousie excessive', 'Tu calcules plus tes potes que ta meuf', 'Casanier'],
    },
    {
        id: 7,
        quest:'Qu’est ce que tu ne peux pas accepter chez la personne:',
        options:['Jalousie excessive', 'Trop proche de ses ami(e)s', 'Casanier'],
    },
    {
        id: 8,
        quest:'Ton/ta partenaire peut avoir un(e) meilleur(e) pote',
        options:['Oui', 'Non'],
    },
    {
        id: 9,
        quest:'Lors d’une embrouille tu:',
        options:['Essayes de communiquer pour arranger les choses','T’excuses pas car t’as toujours raison','Cries un peu puis ça passe'],
    },
    {
        id: 10,
        quest:'Avec quelle citation es-tu le plus d’accord en amour ?',
        options:['Les opposés s’attirent', 'Qui se ressemble s’assemble'],
    },
    {
        id: 11,
        quest:'Ta destination de rêve',
        options:['Afrique', 'Amérique du Nord','Amérique du Sud ','Asie','Europe','Océanie' ],
    },
    {
        id: 12,
        quest:'Ton rappeur préféré',
        options:[],
    }
    ])

    document.getElementById("")

    
    return(

        <div className='questions'>
            {questions.map((ques, indexy) => {
                if (ques.id !== 12) {
                //maps through the questions
                return (
                <div key={indexy} className="questSub">
                    <h2>{ques.quest}</h2> 
                    
                    {ques.options.map((option, index) => {
                    return(

                        <div key={index} className="options">
                            <input type="radio" name={indexy} className="radio"/>
                                <label>{option}</label>
                        </div>
                        
                        );
                    }
                    )}
                    
                </div>
                )
            }
            })}
            <h2 className='questSub'>Ton rappeur préferé</h2>
            <h3 className='rapper'><input type="text" className='rap'/></h3>
        </div>
    )
}

export default Questions