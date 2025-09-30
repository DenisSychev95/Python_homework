
import "./Search.css";
import React from "react";

class Search extends React.Component {

    state = {
        search: ""
    }




    render() {
        let { searchMovie } = this.props
        return (
            <>
                <div className="search">
                    <input
                        type="search"
                        name=""
                        id=""
                        placeholder="Search"
                        value={this.state.search}
                        onChange={(e) => this.setState({ search: e.target.value }, () => searchMovie(this.state.search))
                        } />
                </div>

            </>
        )
    }
}

export default Search;
