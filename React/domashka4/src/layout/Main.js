import React from "react";
import "./Main.css"
import MovieList from "../components/MovieList";
import Preloader from "../components/Preloader";
import Search from "../components/Search";

class Main extends React.Component {

    state = {
        movies: [],
        loading: true,
        res: ""


    }



    componentDidMount() {
        fetch("http://www.omdbapi.com/?apikey=5548b982&s=matrix")
            .then(response => response.json())
            .then(data => this.setState({ movies: data.Search, loading: false, res: data.totalResults}))
    }

    searchMovie = (str, type = "all", page) => {
        this.setState({ loading: true })
        fetch(`http://www.omdbapi.com/?apikey=5548b982&s=${str}${type !== "all" ? `&type=${type}` : ""}${`&page=${page}`}`)
            .then(response => response.json())
            .then(data => this.setState({ movies: data.Search, loading: false, res: data.totalResults}))
            
    }

    pagesCount = (res) => Math.round(res / 10) + 1

    render() {
        const { movies, loading, res} = this.state
        let pages = this.pagesCount(this.state.res)


        


        return (
            <div className="main">
                <div className="wrap">
                    <Search searchMovie={this.searchMovie}  res={res} pages={pages}/>
                    {loading ? <Preloader /> : <MovieList movies={movies} />}

                </div>
            </div>
        )
    }
}

export default Main;