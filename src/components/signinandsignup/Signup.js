import React, { Component } from 'react';
import axios from 'axios';
import './sign.css'
import Signin from './Signin';

export class Signup extends Component {
    constructor(props) {
        super(props);
        this.state = {
          userName: '',
          password: '',
          email: '',
          signup: 'False',
        }
      };
    changeHandler = (e) => {
        this.setState({ [e.target.name]: e.target.value });
      };
    submitHandler=(e)=>{
        e.preventDefault();
        console.log(this.state);
        const stateJson = JSON.stringify(this.state);
        axios.post('http://127.0.0.1:5000/signup',JSON.parse(stateJson)).then((response)=>{
            console.log(response.data);

        }).catch((error)=>{
            console.log(error);
        })
    };
    toPostForm=(e)=>{
        e.preventDefault();
        this.setState({signup:'True'})
    };
  render() {
    const {userName,email, password, signup}=this.state;
    if(signup === "True")
    {
        return <Signin />
    }
    return (
      <div className='something'>
          <div className='box'>
          <form onSubmit={this.submitHandler} action='POSTS' className='wrapper'>
            <h2>Signup</h2>
            <div className='inputbox'>
              <input type='text' name='userName' value={userName} onChange={this.changeHandler}/>
              <span>Enter Name</span>
              <i></i>
            </div>
            <div className='inputbox'>
              <input type='text' name='email' value={email} onChange={this.changeHandler} />
              <span>Enter Email</span>
              <i></i>
            </div>
            <div className='inputbox'>
              <input type='password' name='password' value={password} onChange={this.changeHandler} />
              <span>Enter Password</span>
              <i></i>
            </div>
            <div > 
              <button type='submit' className="SubmitButton">Submit</button>
            </div>
            <div>
              <button onClick={this.toPostForm} className="SubmitButton">Signin</button>
            </div>
        </form>
        </div>
      </div>
    )
  }
}

export default Signup
