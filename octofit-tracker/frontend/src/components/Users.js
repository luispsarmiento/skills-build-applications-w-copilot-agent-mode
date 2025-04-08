import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://reimagined-winner-9656444q4r7fprp9-8000.app.github.dev/api/users')
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center">Users</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Username</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.username}</td>
              <td>{user.email}</td>
              <td>
                <button className="btn btn-primary">Edit</button>
                <button className="btn btn-danger ms-2">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
