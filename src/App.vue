<template>
  <amplify-authenticator>
  </amplify-authenticator>
  <div v-if="isAuthenticated">
    <Navbar />
    <PhotoAlbum />
    <Footer />
  </div>
</template>

<script>
import PhotoAlbum from './components/PhotoAlbum.vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import { Auth } from 'aws-amplify';

export default {
  name: 'App',
  components: {
    PhotoAlbum,
    Navbar,
    Footer
  },
  data() {
    return {
      isAuthenticated: false
    }
  },
  created() {
    Auth.currentAuthenticatedUser().then(user => {
      if(user){
        this.isAuthenticated = true;
      }
    });
  },
}
</script>