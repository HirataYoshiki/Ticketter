<template>
  <div>
    <b-container>
      <b-row>
        <b-col>
          <b-img :src="src"/>
        </b-col>
        <b-col>
          <h4>ログインはこちら</h4>
          <div id="firebaseui-auth-container"/>
        </b-col>
      </b-row>
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
