<template>
  <b-card bg-variant="light" header-tag="header">
    <template #header>
      <b-container>
        <b-row>
          <b-col>
            Profile
          </b-col>
          <b-col cols="auto">
            <b-icon class="button" @click="showModal" v-show="showProfileEditor" icon="pen-fill" circle/>
          </b-col>
        </b-row>
      </b-container>
    </template>
    <b-card-body>
      <b-container>
        <b-row id="userbasicstatus">
          <b-col cols="auto">
            <b-avatar :src="user.photoURL"/>
          </b-col>
          <b-col>
            <b-row>
              <b-form-group label-cols="4" label-cols-lg="4" label-size="sm" label="Name: " label-for="name">
                <b-form-input v-model="edit.name" v-if="edit.status" id="name" :placeholder="user.name" size="sm"/>
                <b-form-input v-else :value="user.name" disabled size="sm"/>
              </b-form-group>
            </b-row>
            <b-row>
              <b-form-group label-cols="4" label-cols-lg="4" label-size="sm" label="Email: " label-for="email">
                <b-form-input v-model="edit.email" v-if="edit.status" id="email" :placeholder="user.email" size="sm"/>
                <b-form-input v-else :value="user.email" disabled size="sm"/>
              </b-form-group>
            </b-row>
          </b-col>
        </b-row>
          <b-row v-if="edit.status">
            <b-col>
              <b-button @click="changeProfile" variant="outline-success">Save</b-button>
              <b-button @click="showModal" variant="outline-dark">Cancel</b-button>
            </b-col>
          </b-row>
        <b-row id="useraccountbind">
          <b-col>
            Connect Accounts
          </b-col>
        </b-row>
        <b-col>
          <b-icon icon="twitter" @click="connectTwitter"/>
        </b-col>
      </b-container>
    </b-card-body>
  </b-card>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'profilecard',
  inject: ['requestMethods'],
  props: {
    uid: String
  },
  data () {
    return {
      user: {},
      ticketmax: 0,
      edit: {
        status: false,
        name: '',
        email: ''
      }
    }
  },
  methods: {
    showModal () {
      this.edit.status = !this.edit.status
    },
    changeProfile () {
      const data = {}
      if (this.edit.name) {
        data.displayName = this.edit.name
      }
      if (this.edit.email) {
        data.email = this.edit.email
      }
      firebase.auth().currentUser.updateProfile(data).then((user)=> {
        firebase.database().ref(`/users/${user.uid}`).set({
          uid: user.uid,
          name: user.displayName,
          photoURL: user.photoURL,
          email: user.email
        }).then(this.showModal())
      }).catch((e) => {
        alert(e)
      })
    },
    connectTwitter () {
      var twitterProvider = new firebase.auth.TwitterAuthProvider()
      firebase.auth().currentUser.linkWithPopup(twitterProvider).then(() => {
        alert('connect to twitter')
        return true
      })
    }
  },
  computed: {
    showProfileEditor () {
      if (this.uid === firebase.auth().currentUser.uid) {
        return true
      }
      return false
    }
  },
  created: async function () {
    const user = await firebase.database().ref('/users/' + this.uid).once('value')
    this.user = user.val()
    try {
      const profileUserInBackend = await this.requestMethods.users.get_one_user(this.uid)
      this.ticketmax = profileUserInBackend.ticketmax
    } catch (e) {
      this.ticketmax = 0
    }
  }
}
</script>