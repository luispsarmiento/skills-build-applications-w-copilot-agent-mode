import React from 'react';

function Users() {
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
          <tr>
            <td>JaneDoe</td>
            <td>jane.doe@example.com</td>
            <td>
              <button className="btn btn-primary">Edit</button>
              <button className="btn btn-danger ms-2">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Users;
