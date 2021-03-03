<template>
  <div class="container">
    <div class="section">
      <div class="row columns is-multiline">
        <div v-for="card in cardData" :key="card.id" class="column is-4">
          <div class="card large">
            <div class="card-image">
              <figure class="image is-16by9">
                <img :src="card.image" alt="Image">
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img :src="card.avatar" alt="Image">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4 no-padding">{{card.user.title}}</p>
                  <p>
                    <span class="title is-6">
                      <a href=""> {{card.user.handle}} </a> </span> </p>
                  <p class="subtitle is-6">{{card.user.title}}</p>
                </div>
              </div>
              <div class="content">
                {{card.content}}
                <div class="background-icon"><span class="icon-twitter"></span></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//import { API } from 'aws-amplify';
import { Storage } from 'aws-amplify';

let cardsData = [{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
{
  id: 1,
  image: 'https://source.unsplash.com/h-ACUrBngrw/1280x720',
  avatar: 'https://avatars.dicebear.com/api/initials/john%20doe.svg',
  user: {
    name: 'Okinami',
    handle: 'twitterid',
    title: 'Lead Developer'
  },
  content: 'The Beast stumbled in the dark for it could no longer see the path. It started to fracture and weaken, trying to reshape itself into the form of metal. Even the witches would no longer lay eyes upon it, for it had become hideous and twisted.'
},
]

export default {
  name: 'HelloWorld',
  data() {
    return {
      imgKey: '',
      cardData: cardsData
    }
  },
  methods: {
    getImages() {
      Storage.list('').then(storageFull => {
        var keys = []
        for (var item in storageFull){
          keys.push(storageFull[item].key);
        }
        for (var key in keys) {
          Storage.get(keys[key]).then(imgUrl => {
            this.imgKey = imgUrl;
          });
        }
      }).catch(err => console.log(err));
    },
    async createTodo(event) {
      console.log('calling');
      const result = await Storage.put(event.target.files[0].name, event.target.files[0]);
      //const result = await API.post('pythonapi', '/pictures/update');
      console.log(result);
    }
  },
  created() {
    this.getImages();
  },
}
</script>