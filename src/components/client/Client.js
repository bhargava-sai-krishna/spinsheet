import React, { Component } from 'react';
import axios from 'axios';

class Client extends Component {
  constructor(props) {
    super(props);

    this.state = {
      userId: props.userId,
      files: [],
    };
  }

  componentDidMount() {
    this.fetchFiles(this.state.userId);
  }

  fetchFiles = async () => {
    try {
      const stateJson = JSON.stringify(this.state);
      console.log(JSON.parse(stateJson))
      const response = await axios.post('http://127.0.0.1:5000/getFiles',JSON.parse(stateJson));
      console.log(response.data)
      this.setState({ files: response.data });
    } catch (error) {
      console.error('Error fetching files:', error);
    }
  };

  handleEditClick = (id, filename) => {
    console.log('Edit clicked for ID:', id, 'and filename:', filename);
    
    const data = {
      "userId": id,
      "filename": filename
    };
  
    axios.post('http://127.0.0.1:5000/getExcel', data)
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  

  render() {
    return (
      <div>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>File Name</th>
              <th>File Type</th>
              <th>Edit</th>
            </tr>
          </thead>
          <tbody>
            {this.state.files.map((file, index) => (
              <tr key={index}>
                <td>{file.id}</td>
                <td>{file.filename}</td>
                <td>{file.filetype}</td>
                <td>
                  <button onClick={() => this.handleEditClick(file.id, file.filename)}>
                    Edit
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Client;
