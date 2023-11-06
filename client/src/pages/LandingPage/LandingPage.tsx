import React from "react";

function LandingPage() {
    return (
        <div>
            <h1>Welcome!</h1>
            <p>You are not logged in!</p>
            <div>
                <a href="/login"><button>Login</button></a>
                <a href="/register"><button>Register</button></a>
            </div>
        </div>
    );
}

export default LandingPage