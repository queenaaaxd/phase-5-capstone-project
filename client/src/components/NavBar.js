import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav>
            <div className='navbar'>
                <NavLink to="/">home</NavLink>
                <NavLink to="/add_hotel">signup</NavLink>
                <NavLink to="/add_hotel">login</NavLink>
                <NavLink to="/add_hotel">cart</NavLink>
                <NavLink to="/update_hotel">orders</NavLink>
                
            </div>
        </nav>
    )
}

export default NavBar;