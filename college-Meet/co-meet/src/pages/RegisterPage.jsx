import '../static/RegisterPage.css'
import React from "react"
import { Link } from "react-router-dom";
export default function RegisterPage(){
    return(
        <div className="register-body">
            <div className="register-container">
                <h1>Co-Meet Register</h1>
                <form>
                    <div className="username">
                        <label for="name">Name: </label>
                        <input type="text" id="name" name="name" placeholder="Firstname Lastname"></input>
                    </div>
                    <div className="email">
                        <label for="email">Email: </label>
                        <input type="email" id="email" name="email" placeholder="username@umbc.edu"></input>
                    </div>
                    <div className="password">
                        <label for="password">Password: </label>
                        <input type="password" placeholder=""></input>
                    </div>
                    <button type="submit">Register</button>
                </form>
                <p>Already registered then <Link to="/">Login</Link></p>
            </div>
        </div>
    )
}