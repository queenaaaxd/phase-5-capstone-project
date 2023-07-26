import React from "react";
import { NavLink } from "react-router-dom";
// import { ShoppingCartSimple, HouseLine, User, SquaresFour, PencilLine, Scroll } from "phosphor-react";

function NavBar(){
    return (
        <nav>
            <div className='navbar'>
                <NavLink to="/home">HOME</NavLink>
                <NavLink to="/products">PRODUCTS</NavLink>
                <NavLink to="/signups">SIGN UP</NavLink>
                <NavLink to="/login">LOG IN</NavLink>
                <NavLink to="/cart">MY CART</NavLink>
                <NavLink to="/transaction">ORDERS</NavLink>
                {/* <NavLink to="/home"><HouseLine size={32} /></NavLink>
                <NavLink to="/products"><SquaresFour size={32} /></NavLink>
                <NavLink to="/signup"><PencilLine size={32}/></NavLink>
                <NavLink to="/login"><User size={32}/></NavLink>
                <NavLink to="/cart"><ShoppingCartSimple size={32}/></NavLink>
                <NavLink to="/transaction"><Scroll size={32}/></NavLink> */}
            
            </div>
        </nav>
    )
}

export default NavBar;