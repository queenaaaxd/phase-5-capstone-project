import { useState } from "react";

function Signup({ updatePostFormData, addUser }) {
  const [formSubmitted, setFormSubmitted] = useState(false);

  console.log(updatePostFormData);

  return (
    <div>
      {formSubmitted ? (
        "Registration Success. Welcome to Simply Beverages."
      ) : (
        <form
          onSubmit={(event) => {
            addUser(event);
            setFormSubmitted((formSubmitted) => !formSubmitted);
          }}
          className="signup-form"
        >
          <div>
            <input
              onChange={updatePostFormData}
              type="text"
              name="email"
              placeholder="email"
              required
            />
            <input
              onChange={updatePostFormData}
              type="password"
              name="password"
              placeholder="password"
              required
            />
          </div>
          <div className="button-div">
            <button className="button" type="submit">
              Sign Up
            </button>
          </div>
        </form>
      )}
    </div>
  );
}

export default Signup;
