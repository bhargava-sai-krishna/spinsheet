import React, { Component } from 'react'
import axios from 'axios';
import Signup from './Signup';
import Client from '../client/Client';
import './signin.css'

export class Signin extends Component {
    constructor(props) {
        super(props);
        this.state = {
          userId: '',
          password: '',
          userRole: '', 
          signup: 'False',
          name: "",
          showPassword: false,
        };
      }

      toSignup=(e)=>{
        e.preventDefault();
        this.setState({signup:'True'})
      };
    
      changeHandler = (e) => {
        this.setState({ [e.target.name]: e.target.value });
      };
    
      submitHandler = (e) => {
        e.preventDefault();
        console.log(this.state);
        const stateJson = JSON.stringify(this.state);
        console.log(JSON.parse(stateJson))
        axios
          .post('http://127.0.0.1:5000/signin', JSON.parse(stateJson))
          .then((response) => {
            console.log("hahaha: "+response.data.flag);
            if (response.data.flag !== 'False') 
            {
                const jsonData = response.data;
                this.setState({ userRole: 'client', name: jsonData.name });
            } else {
              console.log('Enter correct details');
            }
          })
          .catch((error) => {
            console.log(error);
          });
      };

      togglePasswordVisibility = () => {
        this.setState((prevState) => ({ showPassword: !prevState.showPassword }));
      };
  render() {
    const { userId, password, signup, name, userRole } = this.state;
    if(signup === "True")
    {
        return <Signup />
    }
    if (userRole === 'client') 
    {
      return <Client userId={userId} name={name}/>;
    }
    return (
      <div>
        <form onSubmit={this.submitHandler}>
            <h2>Sign In</h2>
            <h2>User Id</h2>
            <input type='text' name='userId' value={userId} onChange={this.changeHandler} />
            <h2>Password</h2>
            <input type={this.state.showPassword ? 'text' : 'password'} name='password' value={password} onChange={this.changeHandler} />
            <input type="checkbox" onChange={this.togglePasswordVisibility} checked={this.state.showPassword}/>
            <br />
            Show Password
            <br />
            <button type='submit'>Submit</button>
            <button onClick={this.toSignup}>Signup</button>
        </form>
      </div>
    )
  }
}

export default Signin