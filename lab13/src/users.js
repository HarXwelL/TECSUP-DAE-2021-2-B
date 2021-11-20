import React from 'react'
import { useParams } from 'react-router-dom';

const Users = () => {
    let params = useParams();
    return (
        <div>
            <center>
                <h1>Usuarios</h1>
                <p>Id: {params.id}</p>
            </center>
        </div>
    )
}
export default Users;
