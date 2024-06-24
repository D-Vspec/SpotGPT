import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const [playlistName, setPlaylistName] = useState('');
  const [description, setDescription] = useState('');
  const [playlistLink, setPlaylistLink] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setPlaylistLink(''); // Reset playlist link when a new request is made

    try {
      const response = await fetch('http://localhost:5000/create_playlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ playlistName, description }),
      });
      const data = await response.json();
      if (response.ok) {
        setPlaylistLink(data.playlistLink);
      } else {
        console.error('Error:', data);
      }
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
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
        {loading ? (
          <div className="loading">
            <div className="spinner"></div>
            <p>Generating...</p>
          </div>
        ) : (
          playlistLink && (
            <div className="playlist-link">
              <p>Link to the playlist:</p>
              <a href={playlistLink} target="_blank" rel="noopener noreferrer" className="playlist-button">
                Open Playlist
              </a>
            </div>
          )
        )}
      </header>
    </div>
  );
};

export default App;
