<template>
  <div class="modal" :class="{ 'is-active': isModalActive }">
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="box box-color">
        <CreatePost :testProp="trigger" />
      </div>
    </div>
    <button class="modal-close is-large" aria-label="close" @click="cancelModal"></button>
  </div>
  <nav class="navbar">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item" href="#">
          <span class="icon logo-color">
            <i class="fas fa-heart"></i>
          </span>
          <p class="title is-4 logo-color">Wedding Gallery</p>
        </a>
        <span class="navbar-burger burger" data-target="navbarMenu">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
      <div id="navbarMenu" class="navbar-menu">
        <div class="navbar-end">
          <a class="navbar-item" @click="isModalActive=true">
            <span class="icon"><i class="fas fa-upload"></i></span>
            <span>Send Photo</span>
          </a>
          <div class="navbar-item has-dropdown is-hoverable">
            <a v-if="!user" class="navbar-link">
              Guest
            </a>
            <a v-if="user" class="navbar-link">
              {{fullName}}
            </a>
            <div class="navbar-dropdown is-boxed">
              <a class="navbar-item sign-out-item">
                <amplify-sign-out></amplify-sign-out>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import CreatePost from '@/components/CreatePost.vue'
import { Auth } from 'aws-amplify';

export default {
  name: 'Navbar',
  components: {
    CreatePost
  },
  data() {
    return {
      isModalActive: false,
      trigger: false,
      user: undefined
    }
  },
  methods: {
    cancelModal() {
      this.isModalActive=false;
      this.trigger = !this.trigger;
    },
    checkUser(){
      Auth.currentAuthenticatedUser().then(user => {
        var groups = user.signInUserSession.accessToken.payload["cognito:groups"];
        var scope = 'guest'
        if (['admin'].indexOf(groups) >= 0) {
          scope = 'admin'
        }
        this.user = {
          name: 'Douglas',
          lastName: 'Rossi',
          scope: scope
        }
      });
    }
  },
  created() {
    this.checkUser();
  },
  computed: {
    fullName() {
      var full = ''
      if(this.user){
        var scope = ''
        if(this.user){
          scope = '(Admin)';
        }
        full = `${this.user.name}  ${this.user.lastName}${scope}`;
      }
      return full
    }
  }
}
</script>

<style scoped>
.navbar-item .sign-out-item {
  padding-right: 1rem;
}

.logo-color {
  color: #690200;
}

.box-color {
  background-color: white;
}
</style>