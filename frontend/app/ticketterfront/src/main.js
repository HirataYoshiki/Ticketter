import Vue from 'vue'
import App from './App.vue'
import router from './router'
import firebase from 'firebase'
import config from '../.env/config'

Vue.config.productionTip = false
var firebaseConfig = config
// Initialize Firebase 
firebase.initializeApp(firebaseConfig)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')