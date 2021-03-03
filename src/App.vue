<template>
  <amplify-authenticator>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </amplify-authenticator>
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