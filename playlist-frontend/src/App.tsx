import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const [playlistName, setPlaylistName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Playlist Name:', playlistName);
    console.log('Description:', description);

    // Here you can add the code to call your Python backend API
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Create Playlist</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="playlistName">Playlist Name:</label>
            <input
              type="text"
              id="playlistName"
              value={playlistName}
              onChange={(e) => setPlaylistName(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="description">Description:</label>
            <input
              type="text"
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="submit-button">Create</button>
        </form>
      </header>
    </div>
  );
};

export default App;
