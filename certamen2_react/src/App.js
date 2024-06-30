import React, { useEffect, useState } from 'react';
import './App.css'; // Asegúrate de que este importe está correcto

function App() {
  const [pokemons, setPokemons] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8080/api/random-pokemons/')
      .then(response => response.json())
      .then(data => setPokemons(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
      <div className="background"></div> {/* Capa de fondo */}
      <div className="container"> {/* Contenedor para el contenido */}
        <h1 className="title">Random Pokemons</h1>
        <ul className="pokemonList">
          {pokemons.map(pokemon => (
            <li key={pokemon.numero_Pokedex} className="pokemonItem">
              <img src={pokemon.url_imagen} alt={`Imagen de ${pokemon.nombre}`} className="pokemonImage"/>
              <h2>{pokemon.nombre}</h2>
              <p>Número en Pokedex: {pokemon.numero_Pokedex}</p>
              <p>Tipo Primario: {pokemon.tipo_primario}</p>
              <p>Tipo Secundario: {pokemon.tipo_secundario}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
