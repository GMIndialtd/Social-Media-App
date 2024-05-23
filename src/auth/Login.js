import React from 'react';
import { Link } from 'react-router-dom';

function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-sm">

        <h2 className="text-2xl font-bold text-center ">Login</h2>
        {/* <p className="  text-center  mb-10 mt-2">Alredy have an account ? <Link to={'/login'} className='text-purple-600 undeline'>Login here</Link></p> */}
        {/* <h2 className="text-2xl font-bold text-center mb-4">Create an Account</h2> */}
        <p className="text-center mb-10  mt-2">Don't have an account yet? <Link to={'/register'} className='text-purple-600 underline'>Sign up here</Link></p>

        <form>

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
              id="Password"
              placeholder="Enter your password"
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
            Login
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;
