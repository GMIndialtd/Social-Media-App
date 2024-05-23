import React from 'react';

const UserCard = ({ image, name, friends, posts }) => {
  return (
    <div>
      <section class="flex flex-col ml-5 w-3/12 max-md:ml-0 max-md:w-full">
                  <div class="flex flex-col grow justify-center px-16 py-4 w-full text-xs rounded-lg border border-solid bg-zinc-200 border-zinc-200 max-md:mt-5">
                    <div class="flex flex-col">
                      <div class="flex flex-col justify-center self-center font-semibold text-neutral-900 w-[98px]">
                        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/e505ea34f83a46156c747fa90e1a65c0be825a41e3e575d541a8a42c93e193f4?apiKey=10db01bc78004f75961b3bb8ed42e6cb&" alt="Profile Image" class="self-center w-full rounded-full aspect-square" />
                        <span class="justify-center mt-2">Code With Stein</span>
                      </div>
                      <div class="flex gap-5 justify-between mt-6 font-medium text-zinc-600">
                        <span>180 Friends</span>
                        <span>120 Post</span>
                      </div>
                    </div>
                  </div>
                </section>
    </div>
  
  );
}

export default UserCard;
