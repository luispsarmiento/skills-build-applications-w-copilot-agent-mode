import React from 'react';

function Workouts() {
  return (
    <div className="container mt-4">
      <h1 className="text-center">Workouts</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Workout</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Yoga</td>
            <td>Relaxing and stretching exercises</td>
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

export default Workouts;
