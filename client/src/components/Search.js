import React from "react";

function Search( {search, setSearch} ) {
    
    console.log(setSearch)
    return (
        <div className="searchbar">
            <h1>SEARCH</h1>
            <label htmlFor="search">Search : </label>
            <input
                type="text"
                id="search"
                placeholder=""
                onChange={(e) => setSearch(e.target.value)}
                value={search}
            />
        </div>
    );
}

export default Search;