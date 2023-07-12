import '../App.css';
import {useState, useEffect} from 'react'
import { BrowserRouter, Routes, Route, Switch } from "react-router-dom"

import NavBar from './NavBar'
import Header from './Header'
import Home from "./Home";

function App() {
  return (
      
    <div className='app'>
      <Header /> 
      <NavBar />

    </div>

    )
}
//   return (
//     <div className="app">
//       <Header />
//       <NavBar/>
//       <Switch>
//         <Route exact path="/">
//           <h1>Simply just beverages!</h1>
//         </Route>
//         <Route path="/signup">
//         </Route>
//         <Route path="/login">
//         </Route>
//         <Route path="/cart">
//         </Route>
//         <Route path="/orders">
//         </Route>
//       </Switch>
//     </div>
//   );
// }

export default App;
