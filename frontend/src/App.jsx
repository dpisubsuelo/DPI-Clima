// import logo from "./logo.svg";
import { Provider } from "react-redux";
import "./App.css";
import Clima from "./components/Clima";
import { store } from "./store/store";

//Esto seria como el main
function App() {
    return (
        <Provider store={store}>
            <div className="App">
                <Clima />
            </div>
        </Provider>
    );
}

export default App;
