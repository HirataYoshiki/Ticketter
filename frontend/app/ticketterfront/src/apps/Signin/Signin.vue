<template>
  <div>
    <h3>以下よりログインしてください。</h3>
    <div id="firebaseui-auth-container"/>
    <b-button @click="requestMethods.users.post_user" variant="success">Register</b-button>
  </div>
</template>

<script>
import firebase from 'firebase'
import * as firebaseui from 'firebaseui'
import 'firebaseui/dist/firebaseui.css'
export default {
  name: 'signin',
  inject: [
    'requestMethods'
  ],
  mounted () {
    var ui = new firebaseui.auth.AuthUI(firebase.auth())
    const uiConfig = {
      signInSuccessUrl: '/signin',
      signInFlow: 'redirect',
      signInOptions: [
        {
          provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
          signInMethod: firebase.auth.EmailAuthProvider.EMAIL_LINK_SIGN_IN_METHOD
        }
      ]
    }
    ui.start('#firebaseui-auth-container', uiConfig)
  }
}
</script>
