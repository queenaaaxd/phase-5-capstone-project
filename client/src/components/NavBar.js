import React from "react";
import { NavLink } from "react-router-dom";

function NavBar() {
  return (
    <nav>
      <div className="navbar">
        <NavLink to="/home">HOME</NavLink>
        <NavLink to="/products">PRODUCTS</NavLink>
        <NavLink to="/signup">SIGN UP</NavLink>
        <NavLink to="/login">LOG IN</NavLink>
        <NavLink to="/cart">MY CART</NavLink>
        <NavLink to="/transaction">ORDERS</NavLink>
        <NavLink to="/manage">MANAGE</NavLink>
      </div>
    </nav>
  );
}

export default NavBar;
