import { createApp } from 'vue'
import App from './App.vue'

import Amplify, { Auth } from 'aws-amplify';

import aws_exports from './aws-exports';
import {
  applyPolyfills,
  defineCustomElements,
} from '@aws-amplify/ui-components/loader';

require("./assets/main.css");

Amplify.configure(aws_exports);
applyPolyfills().then(() => {
  defineCustomElements(window);
});

Auth.configure(aws_exports);

createApp(App).mount('#app')
