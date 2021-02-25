<template>
  <input type="file" @change="createTodo" multiple>
</template>

<script>
//import { API } from 'aws-amplify';
import { Storage } from 'aws-amplify';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods: {
    async createTodo(event) {
      console.log('calling');
      const result = await Storage.put(event.target.files[0].name, event.target.files[0]);
      //const result = await API.post('pythonapi', '/pictures/update');
      console.log(result);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
