
import '../static/HomePage.css'
import React from "react"
import { Link } from "react-router-dom";

export default function HomePage(){
    return(
    <div className='flex'>
        <div className="sidebar">
            <h1>image</h1>
        </div>
        <main className='main-content'>
            <h1>Co-Meet</h1>
            <form>
                <div>
                    <label for="email">Email</label>
                    <input type="email" id="email" placeholder="email"/>
                </div>
                <div>
                    <label for="college"> College : </label>
                    <select id="college" name="college">
                    <option value="umbc">UMBC</option>
                </select>
                </div>
            <button type="submit">Login</button>
            </form>
            <p>Dont have an account, no problem : <Link to="/register">Register</Link></p>
        </main>
    </div>
    )
}