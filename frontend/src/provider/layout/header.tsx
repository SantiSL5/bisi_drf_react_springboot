import { Link } from "react-router-dom";
import "./style.css"
import { useUsers } from "../hooks/useUsers";

interface HeaderProps {
    title: string,
}

const Header = (props: HeaderProps) => {
    const { user, isAdmin, logout } = useUsers();
    
    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/">{props.title}</Link>
                    <button type="button" className="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarCollapse">
                        <div className="navbar-nav">
                            <Link className="nav-item nav-link" to="/">Home</Link>
                            {isAdmin ? <Link className="nav-item nav-link" to="/admin">Admin</Link> : <></>}
                        </div>
                        <div className="navbar-nav ms-auto">
                            {user
                                ?
                                <div className="nav-item navbar-collapse">
                                    <button className="nav-item nav-link btn btn-link">{user.username}</button>
                                    <button className="nav-item nav-link btn btn-link" onClick={logout}>Logout</button>
                                </div>
                                : <Link className="nav-item nav-link" to="/login">Login</Link>
                            }
                        </div>
                    </div>
                </div>
            </nav>
        </>
    )
}

export default Header;