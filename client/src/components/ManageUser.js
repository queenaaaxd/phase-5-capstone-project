import React, { useState } from "react";

function ManageUser({ users, onUpdate, onDelete }) {
  const [selectedUser, setSelectedUser] = useState(null);
  const [updateData, setUpdateData] = useState({
    username: "",
    password: "",
    admin: false,
  });

  const handleUserChange = (event) => {
    const userId = event.target.value;
    const user = users.find((u) => u.id === parseInt(userId));
    setSelectedUser(user);
    if (user) {
      setUpdateData({
        email: user.email,
        password: user.password,
        admin: user.admin,
      });
    }
  };

  const handleInputChange = (event) => {
    const value =
      event.target.type === "checkbox"
        ? event.target.checked
        : event.target.value;
    setUpdateData({ ...updateData, [event.target.name]: value });
  };

  const handleUpdate = () => {
    onUpdate(selectedUser.id, updateData);
  };

  const handleDelete = () => {
    onDelete(selectedUser.id);
  };

  return (
    <div>
      <h2>Manage Users</h2>
      <select onChange={handleUserChange}>
        <option value="">Select a user</option>
        {users.map((user) => (
          <option key={user.id} value={user.id}>
            {user.email}
          </option>
        ))}
      </select>
      {selectedUser && (
        <div>
          <input
            type="text"
            name="email"
            value={updateData.email}
            onChange={handleInputChange}
            placeholder="new email"
          />
          <input
            type="text"
            name="password"
            value={updateData.password}
            onChange={handleInputChange}
            placeholder="new password"
          />
          <label>
            Admin:
            <input
              type="checkbox"
              name="admin"
              checked={updateData.admin}
              onChange={handleInputChange}
            />
          </label>
          <button onClick={handleUpdate}>Update User</button>
          <button onClick={handleDelete}>Delete User</button>
        </div>
      )}
    </div>
  );
}

export default ManageUser;
