import React from "react";
import logo from "../../imgs/logo.png";
import agent from "../../agent"
const Banner = ({ onSearch }) => {
  const handleSearch = (e) => {
    e.preventDefault()
    if (e.target.value.length >+ 3) {
      const title = e.target.value
      onSearch(
        e.target.value,
        (page) => agent.Items.search(title, page),
        agent.Items.search(title)
      )
    }
  }


  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div>
          <span>A place to </span>
          <span id="get-part">get</span>
          <input id="search-box" className="form-control-sm" onChange={handleSearch} />
          <span> the cool stuff.</span>
        </div>
      </div>
    </div>
  );
};

export default Banner;
