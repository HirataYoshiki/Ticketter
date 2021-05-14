<template>
  <div id="app">
    <b-container>
      <HeaderColumn/>
      <b-row class="justify-content-md-center">
        <b-col lg="7" md="8" sm="11" cols="auto" align-self="center">
          <div v-if="!user">
            <Signin/>
          </div>
          <div v-else>
            <router-view/>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import firebase from 'firebase'
import HeaderColumn from '@/apps/HeaderColumn'
import Signin from '@/apps/Signin/Signin.vue'
export default {
  name: 'app',
  components: {
    HeaderColumn,
    Signin
  },
  data () {
    return {
      user: null,
      endpoints: {
        users: 'https://ticketter-fi7wohnrcq-an.a.run.app/users',
        tickets: 'https://ticketter-fi7wohnrcq-an.a.run.app/tickets',
        interactions: 'https://ticketter-fi7wohnrcq-an.a.run.app/interactions'
      }
    }
  },
  methods: {
    _get_idToken: async function () {
      try {
        const idToken = await firebase.auth().currentUser.getIdToken(true)
        return idToken
      } catch (e) {
        console.log('get idToken error')
        return true
      }
    },
    create_headers: async function () {
      const idToken = await this._get_idToken()
      const headers = {
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${idToken}`
        }
      }
      return headers
    },
    _get_request_to_backend: async function (url, params = null) {
      const headers = await this.create_headers()
      try {
        if (params) {
          headers.params = params
        }
        const result = await this.axios.get(url, headers)
        return result.data
      } catch (e) {
        alert(e)
        return false
      }
    },
    get_one_user: async function (uid) {
      const url = `${this.endpoints.users}/${uid}`
      const result = await this._get_request_to_backend(url)
      return result
    },
    get_all_users: async function () {
      return await this._get_request_to_backend(this.endpoints.users)
    },
    get_one_ticket: async function (ticketid) {
      const url = `${this.endpoints.tickets}/${ticketid}`
      return await this._get_request_to_backend(url)
    },
    get_all_tickets: async function () {
      return await this._get_request_to_backend(this.endpoints.tickets)
    },
    get_ones_interactions: async function (params=null) {
      const url = this.endpoints.interactions
      return await this._get_request_to_backend(url, params)
    },
    _post_request_to_backend: async function (url, data) {
      const headers = await this.create_headers()
      try {
        const result = await this.axios.post(url, data, headers)
        return result.data
      } catch (e) {
        return false
      }
    },
    post_user: async function () {
      return await this._post_request_to_backend(this.endpoints.users, {})
    },
    post_ticket: async function (name, text, volume) {
      const data = {
        name: name,
        text: text,
        volumemax: volume
      }
      return await this._post_request_to_backend(this.endpoints.tickets, data)
    },
    post_interactions: async function (ticketid, uidList) {
      const data = {
        ticketid: ticketid,
        to_: uidList
      }
      return await this._post_request_to_backend(this.endpoints.interactions, data)
    },
    usergetter () {
      return this.user
    }
  },
  provide () {
    return {
      user: this.usergetter,
      requestMethods: {
        users: {
          get_one_user: this.get_one_user,
          get_all_users: this.get_all_users,
          post_user: this.post_user
        },
        tickets: {
          get_all_tickets: this.get_all_tickets,
          get_one_ticket: this.get_one_ticket,
          post_ticket: this.post_ticket
        },
        interactions: {
          get_ones_interactions: this.get_ones_interactions,
          post_interactions: this.post_interactions
        }
      }
    }
  },
  created () {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        this.user = user
        const data = {
          uid: user.uid,
          name: user.displayName,
          photoURL: user.photoURL,
          email: user.email
        }
        try {
          firebase.database().ref(`/users/${user.uid}`).set(data)
          firebase.database().ref(`/users/${user.uid}`).on('child_changed',snap => {
            this.user = snap.val()})
          this.post_user()
        } catch (e) {
          alert(e)
          return true
        }
        return true
      }
      this.user = null
      return true
    })
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: rgb(227, 240, 252);
}
</style>
