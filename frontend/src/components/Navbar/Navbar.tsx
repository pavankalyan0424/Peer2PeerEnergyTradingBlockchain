import { NavLink } from "react-router-dom";
import "./Navbar.css";
import SystemStatus from "../SystemStatus/SystemStatus";

function Navbar() {
    return (
        <nav className="navbar">
            <h2>EnerChain Marketplace</h2>
            <div className="nav-links">
                <NavLink to="/">Marketplace</NavLink>
                <NavLink to="/buyer">Buyer</NavLink>
                <NavLink to="/admin">Admin</NavLink>
            </div>
            <SystemStatus/>
        </nav>
    )
}

export default Navbar;