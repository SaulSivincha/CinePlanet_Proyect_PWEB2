import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Device({ table }) {
  const [movies, setMovies] = useState([]);
  const endpoint = `http://localhost:8080/${table}`;

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(endpoint);
        setMovies(response.data);
      } catch (error) {
        console.error('Error fetching data: ', error);
      }
    };

    fetchData();
  }, [endpoint]);

  return (
    <div>
      <h1>Películas</h1>
      <ul>
        {movies.map(movie => (
          <li key={movie.id}>{movie.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default Device;
