import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage/LandingPage";
import NotFound from "./pages/NotFound";
import LoginPage from "./pages/LoginPage/LoginPage";

//Switch = Routes 

const Router = () => {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" Component={LandingPage}/>
                <Route Component={NotFound} />
                <Route path="/login" Component={LoginPage} />
            </Routes>
        </BrowserRouter>
    );
};

export default Router