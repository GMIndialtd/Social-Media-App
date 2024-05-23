// import React from 'react'

// function Register() {
//   return (


//     <div className="flex gap-10 my-10 bg-gray-200 p-20 ">



import React from 'react';
import { Link } from 'react-router-dom';

function Register() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        {/* <h2 className="text-2xl font-bold mb-6 text-gray-800">Login</h2> */}
        <h2 className="text-2xl font-bold text-center ">Register</h2>
        <p className="  text-center  mb-10 mt-2">Alredy have an account ? <Link to={'/login'} className='text-purple-600 underline'>Login here</Link></p>
        <form>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="username">Full-Name</label>

            <input
              type="username"
              id="username"
              placeholder="Enter your full name"
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 mb-2" htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              placeholder="Enter your email"
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500"
              required
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 mb-2" htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              placeholder="Enter your password"
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500"
              required
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 mb-2" htmlFor="password">Confirm Password</label>
            <input
              type="password"
              id="confirmPassword"
              placeholder="Confirm your password"
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500"
              required
            />
          </div>
          <div className="mb-6 flex items-center">
            <input
              type="checkbox"
              id="keepSignedIn"
              className="mr-2"
            />
            <label htmlFor="keepSignedIn" className="text-gray-700">Keep me signed in</label>
          </div>
          <button
            type="submit"
            className="w-full bg-purple-600 text-white py-2 rounded-lg hover:bg-indigo-600 focus:outline-none focus:bg-indigo-600"
          >
            Sinup
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;
