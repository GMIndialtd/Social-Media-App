
import React from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import UserCard from './components/UserCard';
import PeopleYouMayKnow from './components/PeopleYouMayKnow';
import Trends from './components/Trends';
import profile from './assets/user.jpg';

const App = () => {
  const user = {
    image: profile,
    name: 'Code With Stein',
    friends: 182,
    posts: 120
  };
  const users = [
    { image: 'profile', name: 'One' }, // Replace with actual paths
    { image: 'User', name: 'Another User' },
    { image: 'User', name: 'Third User' }
  ];

  const trends = [
    'codewithstein',
    'webdevelopment',
    'reactjs',
    'tailwindcss',
    'programming'
  ];

  return (
    <div className="bg-gray-100 min-h-screen">
     <Header/>
       <div className="container mx-auto  px-4 py-6 ">
       <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
          <div className="lg:col-span-3">
           <SearchBar />
           <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
             {/* Repeat this UserCard component for each user */}
             <UserCard {...user} />
             <UserCard {...user} />
             <UserCard {...user} />
             <UserCard {...user} />
           </div>
         </div>
         <div className="lg:col-span-2">
            <div className="hidden lg:block">
                
         <PeopleYouMayKnow users={users} />
         </div>
        <div className="bg-white p-4 shadow rounded-lg"> 
           <Trends trends={trends} />
          </div>
          </div> 
         </div>
       </div>
     </div>
    
     
  );
}
export default App;

// export default App;
// import React from 'react';
// import Header from './components/Header';
// import SearchBar from './components/SearchBar';
// import Trends from './components/Trends';

// function App() {
//   return (
//     <div>
//     <Header></Header>
//     <SearchBar></SearchBar>
//      <PeopleYouMayKnow></PeopleYouMayKnow> 
    
//     {/* <div className="flex items-center justify-center min-h-screen bg-gray-100">
//       <h1 className="text-4xl font-bold text-blue-600">
        
//       </h1>
//     </div> */}
//     </div>
//   );
// }


