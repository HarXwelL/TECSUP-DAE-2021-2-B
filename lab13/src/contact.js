import React from 'react'
import { useParams } from 'react-router-dom';

const Contact = () => {
    let params = useParams();
    return (
        <div>
            <center>
                <h1>Contactos</h1>
            </center>
        </div>
    )
}
export default Contact;
