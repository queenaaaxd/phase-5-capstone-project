import React from "react";

function Login({handleLogin, updateFormData}) {

  return (
    <>
      <form onSubmit={handleLogin} className="login-form">
        <input
          onChange={updateFormData}
          id="email"
          type="text"
          placeholder="email"
        />
        <input
          onChange={updateFormData}
          id="password"
          type="password"
          placeholder="password"
        />
        <button className="button" type="submit">
          Login
        </button>
      </form>

      <form className="login-form">
        <button className="button">Logout</button>

        <br />
      </form>
    </>
  );
}

export default Login;
