import React from "react";
import "./Main.css"
import MovieList from "../components/MovieList";
import Preloader from "../components/Preloader";
import Search from "../components/Search";

class Main extends React.Component {

    state = {
        movies: []
    }

    componentDidMount() {
        fetch("http://www.omdbapi.com/?apikey=5548b982&s=matrix")
            .then(response => response.json())
            .then(data => this.setState({ movies: data.Search }))
    }

    searchMovie = (str) => {
        
        fetch(`http://www.omdbapi.com/?apikey=5548b982&s=${str}`)
            .then(response => response.json())
            .then(data => this.setState({ movies: data.Search || []}))
    }

    render() {
        const { movies } = this.state
        

        return (
            <div className="main">
                <div className="wrap">
                    <Search searchMovie={this.searchMovie} />
                    {movies.length ? <MovieList movies={movies} /> : <Preloader />}

                </div>
            </div>
        )
    }
}

export default Main;