<template>
  <img v-show="!imgToUpload" src="@/assets/imgPlaceHolder.jpg">
  <img v-show="imgToUpload" :src="imgToUploadURL" alt="Image">
  <div class="columns">
    <div class="column is-8">
      <div class="field is-grouped">
        <div class="file">
          <label class="file-label">
            <input class="file-input" type="file" name="resume" @change="upload">
            <span class="file-cta">
              <span class="file-icon">
                <i class="fas fa-upload"></i>
              </span>
              <span class="file-label">
                Choose a file…
              </span>
            </span>
          </label>
        </div>
      </div>
    </div>
    <div v-if="imgToUpload" class="column is-2">
      <p class="control">
        <button class="button" @click="cancel()">
          Cancel
        </button>
      </p>
    </div>
    <div v-if="imgToUpload" class="column is-2">
      <p class="control">
        <button class="button is-link" @click="send">
          Send
        </button>
      </p>
    </div>
  </div>
</template>

<script>
//import { API, Storage } from 'aws-amplify';
import { API } from 'aws-amplify';

export default {
  name: 'CreatePost',
  props: ['testProp'],
  data() {
    return {
      imgToUpload: undefined,
      imgToUploadURL: ''
    }
  },
  methods: {
    upload(event) {
      this.imgToUpload = event.target.files[0];   
      this.imgToUploadURL = URL.createObjectURL(this.imgToUpload);   
    },
    async send(){
      API.get('pythonapi', '/photos');
      /*var myInit = {
        body: {
          'name': 'Douglas Rossi',
          'description': 'Nice Pic!',
          'image': 'test.png'
        }
      }*/
      //API.post('pythonapi', '/photos', myInit);
      //Storage.put(this.imgToUpload.name, this.imgToUpload);
    },
    cancel() {
      this.imgToUpload = undefined;
    },
  },
  watch: { 
    testProp: function() {
      this.cancel();
    }
  }
}
</script>

<style>

</style>