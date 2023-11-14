import React, { Component } from 'react';
import axios from 'axios';
import Signin from '../signinandsignup/Signin';

class Client extends Component {
  constructor(props) {
    super(props);

    this.state = {
      userId: props.userId,
      files: [],
      loggedIn: true,
      editing: false,
      editedData: null,
    };
  }

  componentDidMount() {
    this.fetchFiles(this.state.userId);
  }

  fetchFiles = async () => {
    try {
      const stateJson = JSON.stringify(this.state);
      const response = await axios.post('http://127.0.0.1:5000/getFiles', JSON.parse(stateJson));
      this.setState({ files: response.data });
    } catch (error) {
      console.error('Error fetching files:', error);
    }
  };

  handleEditClick = (id, filename) => {
    const data = {
      userId: id,
      filename: filename,
    };

    axios
      .post('http://127.0.0.1:5000/getExcel', data)
      .then((response) => {
        console.log('hi');
        this.setState({
          editing: true,
          editedData: response.data,
        });
      })
      .catch((error) => {
        console.log(error);
      });
  };

  handleCommitChanges = () => {
    const { userId, editedData } = this.state;
    console.log({
      userId,
      tableData: editedData,
    });
    axios.post('http://127.0.0.1:5000/UpdateExcel',{userId,tableData: editedData,}).then((response)=>{
      console.log(response.data);
    }).catch((error)=>{
      console.log(error);
    });
    this.setState({
      editing: false,
      editedData: null,
    });
  };

  handleEditChange = (rowIndex, key, newValue) => {
    // Create a shallow copy of the editedData
    const updatedData = [...this.state.editedData];
    
    // Update the value at the specified row and column
    updatedData[rowIndex][key] = newValue;
  
    // Update the state with the modified data
    this.setState({ editedData: updatedData });
  };

  
  logouter = (e) => {
    this.setState({ loggedIn: false });
  };

  render() {
    const { loggedIn, editing, editedData } = this.state;

    if (!loggedIn) {
      return <Signin />;
    }

    return (
      <div>
        {editing ? (
          <div>
            <h2>Edit Mode</h2>
            {/* Render the edited data as a table */}
            <table>
              <thead>
                <tr>
                  {/* Dynamically generate table headers */}
                  {Object.keys(editedData[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {editedData.map((row, rowIndex) => (
                  <tr key={rowIndex}>
                    {Object.entries(row).map(([key, value], colIndex) => (
                      <td key={colIndex}>
                        <input
                          type="text"
                          value={value}
                          onChange={(e) => this.handleEditChange(rowIndex, colIndex, e.target.value)}
                        />
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
            <button onClick={this.handleCommitChanges}>Commit Changes</button>
          </div>
        ) : (
          <div>
            <h2>File Table</h2>
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
            <button onClick={this.logouter}>Logout</button>
          </div>
        )}
      </div>
    );
  }
}

export default Client;
