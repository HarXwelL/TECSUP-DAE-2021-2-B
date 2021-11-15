import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

class App extends Component {
  constructor(props) {
    super(props);
    this.state =({
      prestamos:[],
      pos:null,
      titulo:'Nuevo',
      id:0,
      codigo:'',
      libro:'',
      cliente:'',
      inicio:'',
      fin:'',
    })
    this.cambioCliente = this.cambioCliente.bind(this);
    this.cambioInicio = this.cambioInicio.bind(this);
    this.cambioFin = this.cambioFin.bind(this);
    this.cambioLibroId = this.cambioLibroId.bind(this);
    this.mostrar = this.mostrar.bind(this);
    this.eliminar = this.eliminar.bind(this);
    this.guardar = this.guardar.bind(this);
  }

  componentDidMount(){
    axios.get('http://127.0.0.1:8000/prestamos')
    .then(res=> {
      this.setState({prestamos:res.data})
    })
  }


  cambioCliente(e){
    this.setState({
      cliente : e.target.value
    })
  }

  cambioInicio(e){
    this.setState({
      inicio : e.target.values
    })
  }

  cambioFin(e){
    this.setState({
      fin : e.target.value
    })
  }

  cambioLibroId(e){
    this.setState({
      libroid : e.target.value
    })
  }


  mostrar(cod,prestamodetalle){
    axios.get('http://127.0.0.1:8000/prestamos/'+cod)
    .then(res => {
      this.setState({
        pos: prestamodetalle,
        titulo: 'Editar',
        id: res.data.id,
        libro :res.data.idlibro,
        cliente: res.data.idusuario,
        inicio: res.data.fechaPrestamo,
        fin : res.data.fechaDevolucion
      })
    })
  }

  guardar(e){
    e.preventDefault();
    let cod = this.state.id;
    const datos = {
      libro: this.state.libro,
      cliente: this.state.cliente,
      inicio: this.state.inicio,
      fin: this.state.fin
    }
    if(cod>0){
      //edición de un registro
      axios.put('http://127.0.0.1:8000/prestamos/'+cod,datos)
      .then(res =>{
        let indx = this.state.pos;
        this.state.prestamos[indx] = res.data;
        var temp = this.state.prestamos;
        this.setState({
          pos:null,
          titulo:'Nuevo',
          id:0,
          codigo:'',
          libro:'',
          cliente:'',
          inicio:'',
          fin:'',
          api:temp
        });
      }).catch((error) =>{
        console.log(error.toString());
      });
    }else{
      //nuevo registro
      axios.post('http://127.0.0.1:8000/prestamos/',datos)
      .then(res => {
        this.state.prestamos.push(res.data);
        var temp = this.state.prestamos;
        this.setState({
          id:0,
          codigo:'',
          libro:'',
          cliente:'',
          inicio:'',
          fin:'',
          api:temp
        });
      }).catch((error)=>{
        console.log(error.toString());
      });
    }
  }


  eliminar(cod){
    let rpta = window.confirm("Desea Eliminar?");
    if(rpta){
      axios.delete('http://127.0.0.1:8000/prestamos/'+cod)
      .then(res =>{
        var temp = this.state.prestamos.filter((prestamos)=>prestamos.id !== cod);
        this.setState({
          prestamos: temp
        })
      })
    }
  }

  render() {
    return (
    <div>
      <Container>
          <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>Libro</th>
              <th>Cliente</th>
              <th>Inicio</th>
              <th>Fin</th>
              <th>Opciones</th>
            </tr>
          </thead>
          <tbody>
            {this.state.prestamos.map((prestamos,prestamodetalle) =>{
              return (
                <tr key={prestamos.id}>
                  <td>{prestamos.idlibro}</td>
                  <td>{prestamos.idusuario}</td>
                  <td>{prestamos.fechaPrestamo}</td>
                  <td>{prestamos.fechaDevolucion}</td>
                  <td>
                  <Button variant="success" onClick={()=>this.mostrar(prestamos.id,prestamodetalle)}>Editar</Button>
                  <Button variant="danger" onClick={()=>this.eliminar(prestamos.id,prestamodetalle)}>Eliminar</Button>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </Table>
        <hr />
        <h1>{this.state.titulo}</h1>
        <Form onSubmit={this.guardar}>
            <input type="hidden" value={this.state.id} />
            <Form.Group className="mb-3">
              <Form.Label>idLibro</Form.Label>
              <Form.Control type="text" value={this.state.libro} onChange={this.cambioLibroId} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>idUsuario</Form.Label>
              <Form.Control type="text" value={this.state.cliente} onChange={this.cambioCliente} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Incio</Form.Label>
              <Form.Control type="text" value={this.state.inicio} onChange={this.cambioInicio} />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label>Fin</Form.Label>
              <Form.Control type="text" value={this.state.fin} onChange={this.cambioFin} />
            </Form.Group>
            <Button variant="primary" type="submit">
              Guardar
            </Button>
        </Form>
      </Container>
    </div>)
  }
}

  
export default App;
