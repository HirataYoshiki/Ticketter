<template>
  <div>
    <b-container>
      <b-row>
        <b-img :src="src" width="400px" fluid/>
      </b-row>
      <p>ログインはこちら</p>
      <div id="firebaseui-auth-container"/>
    </b-container>
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
  data () {
    return {
      src: require('@/assets/logo.png')
    }
  },
  created () {
    var ui = firebaseui.auth.AuthUI.getInstance() || new firebaseui.auth.AuthUI(firebase.auth())
    const uiConfig = {
      signInSuccessUrl: '/',
      signInFlow: 'redirect',
      signInOptions: [
        {
          provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID
        },
        {
          provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
          signInMethod: firebase.auth.EmailAuthProvider.EMAIL_LINK_SIGN_IN_METHOD
        }
      ],
      callbacks: {
        signInSuccessWithAuthResult (authResult) {
          const data = {
            uid: authResult.user.uid,
            name: authResult.user.displayName,
            photoURL: authResult.user.photoURL,
            email: authResult.user.email
          }
          firebase.database().ref(`/users/${authResult.user.uid}`).set(data)
          return true
        }
      }
    }
    ui.start('#firebaseui-auth-container', uiConfig)
  }
}
</script>
