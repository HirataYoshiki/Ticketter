<template>
  <div id="app">
    <b-container>
      <HeaderColumn/>
      <b-row class="justify-content-md-center">
        <b-col lg="5" md="7" sm="12">
          <router-view/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import firebase from 'firebase'
import HeaderColumn from '@/apps/HeaderColumn'
export default {
  name: 'app',
  components: {
    HeaderColumn
  },
  data () {
    return {
      user: {},
      endpoints: {
        users: 'https://ticketter-fi7wohnrcq-an.a.run.app/users',
        tickets: 'https://ticketter-fi7wohnrcq-an.a.run.app/tickets',
        interactions: 'https://ticketter-fi7wohnrcq-an.a.run.app/interactions'
      }
    }
  },
  methods: {
    _get_idToken: async function () {
      const idToken = await firebase.auth().currentUser.getIdToken(true)
      return idToken
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
    _get_request_to_backend: async function (url) {
      const headers = await this.create_headers()
      try {
        const result = await this.axios.get(url, headers)
        return result.data
      } catch (e) {
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
    get_all_tickets: async function () {
      return await this._get_request_to_backend(this.endpoints.tickets)
    },
    get_ones_interactions: async function (uid) {
      const url = `${this.endpoints.interactions}/${uid}`
      return await this._get_request_to_backend(url)
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
    post_ticket: async function (name, text) {
      const data = {
        name: name,
        text: text
      }
      return await this._post_request_to_backend(this.endpoints.tickets, data)
    },
    post_interactions: async function (ticketid, uidList) {
      const data = {
        ticketid: ticketid,
        to_: uidList
      }
      return await this._post_request_to_backend(this.endpoints.interactions, data)
    }
  },
  provide () {
    return {
      user: this.user,
      requestMethods: {
        users: {
          get_one_user: this.get_one_user,
          get_all_users: this.get_all_users,
          post_user: this.post_user
        },
        tickets: {
          get_all_tickets: this.get_all_tickets,
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
    firebase.auth().onAuthStateChanged(async user => {
      if (user) {
        this.user = user
        try {
          const uid = firebase.auth().currentUser.uid
          const userdata = await this.get_one_user(uid)
          if (userdata) {
            return true
          } else {
            await this.post_user()
            return true
          }
        } catch (e) {
          alert ('error occured. try again')
          return true
        }
      }
      this.user = {}
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
}
</style>
