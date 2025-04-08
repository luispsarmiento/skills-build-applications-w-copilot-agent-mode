import React from 'react';

function Teams() {
  return (
    <div className="container mt-4">
      <h1 className="text-center">Teams</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Team Name</th>
            <th>Members</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Team Alpha</td>
            <td>5</td>
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

export default Teams;
