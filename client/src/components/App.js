import "../App.css";
// import {useState, useEffect} from 'react'
import React, { useState, useEffect } from "react";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Route, Routes } from "react-router-dom";

import NavBar from "./NavBar";
import Header from "./Header";
import Home from "./Home";
import ProductPage from "./ProductPage";
import Signup from "./Signup";
import Login from "./Login";
import Cart from "./Cart";
import ManageUser from "./ManageUser";
// import ProductCard from "./ProductCard";

function App() {
  // setting and populated
  const [products, setProducts] = useState([]);

  // keeep track of users in the frontend
  const [users, setUsers] = useState(null);

  // form data login
  const [formData, setFormData] = useState({});

  // state for login user
  const [loggedInUser, setLoggedInUser] = useState(null);

  console.log(loggedInUser);

  // console.log(users);

  // fetch from my backend
  useEffect(() => {
    fetch("http://127.0.0.1:5555/products")
      .then((res) => res.json())
      // .then((products) => console.log(products))
      .then((products) => setProducts(products));
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/users")
      .then((res) => res.json())
      // .then((products) => console.log(products))
      .then((users) => setUsers(users));
  }, []);

  // console.log(products);

  // post new user to backend
  function addUser(event) {
    event.preventDefault();

    fetch("http://127.0.0.1:5555/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(postFormData),
    })
      .then((res) => res.json())
      .then((newUser) => setUsers((users) => [...users, newUser]));
  }

  // state for signup input
  const [postFormData, setPostFormData] = useState({});

  function updatePostFormData(event) {
    setPostFormData({
      ...postFormData,
      [event.target.name]: event.target.value,
    });
    console.log(postFormData);
  }

  function updateUser(userId, userData) {
    fetch(`http://127.0.0.1:5555/users/${userId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(userData),
    })
      .then((res) => res.json())
      .then((updatedUser) => {
        setUsers((users) => {
          return users.map((user) => {
            if (user.id === userId) {
              return updatedUser;
            } else {
              return user;
            }
          });
        });
      });
  }

  function deleteUser(userId) {
    fetch(`http://127.0.0.1:5555/users/${userId}`, {
      method: "DELETE",
    }).then(() =>
      setUsers((users) => {
        return users.filter((user) => {
          return user.id !== userId;
        });
      })
    );
  }

  function handleLogin(event) {
    event.preventDefault();
    // console.log(formData);

    fetch("http://127.0.0.1:5555/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((res) => res.json())
      .then((userData) => setLoggedInUser(userData));
  }

  function updateFormData(event) {
    setFormData({ ...formData, [event.target.id]: event.target.value });
  }

  return (
    <div className="App">
      <Header />
      <NavBar />
      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/products" element={<ProductPage products={products} />} />
        <Route
          path="/signup"
          element={
            <Signup updatePostFormData={updatePostFormData} addUser={addUser} />
          }
        />
        <Route
          path="/login"
          element={
            <Login handleLogin={handleLogin} updateFormData={updateFormData} />
          }
        />
        <Route path="/cart" element={<Cart />} />
        <Route path="/transaction" />
        <Route
          path="/manage"
          element={
            <ManageUser
              users={users}
              onUpdate={updateUser}
              onDelete={deleteUser}
            />
          }
        />
      </Routes>
    </div>
  );
}

export default App;
