import "../App.css";
// import {useState, useEffect} from 'react'
import React, { useState, useEffect } from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Route, Routes } from "react-router-dom";

import NavBar from "./NavBar";
import Header from "./Header"; 
import Home from "./Home";
import ProductPage from "./ProductPage";
import ProductCard from "./ProductCard";

function App() {
  // setting and populated
  const [products, setProducts] = useState([]);

  // fetch from my backend
  useEffect(() => {
    fetch("http://127.0.0.1:5555/products")
      .then((res) => res.json())
      // .then((products) => console.log(products))
      .then((products) => setProducts(products));
  }, []);

  console.log(products);

  return (
    <div className="App">
        <Header />
        <NavBar />
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route
            path="/products"
            element={<ProductPage products={products} />}
          />
          <Route path="/signup" element={<ProductPage products={products} />} />
          <Route path="/login" element={<ProductPage products={products} />} />
          <Route path="/cart" element={<ProductPage products={products} />} />
          <Route
            path="/transaction"
            element={<ProductPage products={products} />}
          />
        </Routes>
    </div>
  );
}

export default App;
