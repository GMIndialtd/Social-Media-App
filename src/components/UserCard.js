import React from 'react';

const UserCard = ({ image, name, friends, posts }) => {
  return (
    <div className="bg-white rounded-lg shadow p-4">
      <img className="w-24 h-24 rounded-full mx-auto" src={image} alt="User" />
      <div className="text-center mt-4">
        <div className="font-bold">{name}</div>
        <div className="text-gray-500">{friends} friends</div>
        <div className="text-gray-500">{posts} posts</div>
      </div>
    </div>
  );
}

export default UserCard;
