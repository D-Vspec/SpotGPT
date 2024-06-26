import React, { useState } from 'react';
import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub } from '@fortawesome/free-brands-svg-icons';

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
        <div className="github-container">
          <a
            href="https://github.com/D-Vspec/SpotGPT"
            target="_blank"
            rel="noopener noreferrer"
            className="github-button"
          >
            <FontAwesomeIcon icon={faGithub} />
          </a>
          <span className="tooltip-text">Visit my GitHub</span>
        </div>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="playlistName">Playlist Name:</label>
            <input
              type="text"
              id="playlistName"
              value={playlistName}
              onChange={(e) => setPlaylistName(e.target.value)}
              placeholder="Enter playlist name"
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
              placeholder="Example: Make a playlist of old bollywood songs"
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
            <a href={playlistLink} target="_blank" rel="noopener noreferrer" className="playlist-button">
              Link to the playlist
            </a>
          )
        )}
      </header>
    </div>
  );
};

export default App;
