import Vue from 'vue'
import App from './App.vue'
import router from './router'
import firebase from 'firebase'

Vue.config.productionTip = false
var firebaseConfig = {
  apiKey: "AIzaSyDcHeQbYaKJQ8cTmyEDDH1P314X8JruIck",
  authDomain: "ticketter.firebaseapp.com",
  projectId: "ticketter",
  storageBucket: "ticketter.appspot.com",
  messagingSenderId: "941864709396",
  appId: "1:941864709396:web:d252f2c8acad7475ca6601"
}
// Initialize Firebase 
firebase.initializeApp(firebaseConfig)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')