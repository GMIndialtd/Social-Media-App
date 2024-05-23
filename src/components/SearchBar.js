import React from 'react';

const SearchBar = () => {
  return (
 
  <div className="flex flex-col sm:flex-row items-center mb-6 space-y-2 sm:space-y-0 sm:space-x-2">
  <input type="text" placeholder="What are you looking for?" 
    className="w-full sm:flex-grow px-4 py-2 rounded-md border border-gray-300 focus:outline-none focus:border-purple-500" />
  <button className="ml-2 bg-purple-500 text-white px-4 py-2 rounded-md">Post</button>
</div>
  );
}

export default SearchBar;
