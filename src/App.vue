<template>
  <amplify-authenticator>
    <!-- The rest of your app code -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <amplify-sign-out></amplify-sign-out>
  </amplify-authenticator>
  <!--<img alt="Vue logo" src="./assets/logo.png">-->
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
