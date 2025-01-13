import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import './components/global.css';

const app = createApp(App);

app.use(router); // Use the router
app.mount('#app');