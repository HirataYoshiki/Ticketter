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
            <b-avatar :src="user.photoURL" size="4rem"/>
          </b-col>
          <b-col>
            <b-row><b-form-group>ID: <small>{{uid}}</small></b-form-group></b-row>
            <b-row>
              <b-form-group label-cols="4" label-cols-lg="4" label-size="sm" label="Name: " label-for="name">
                <b-form-input v-model="edit.name" v-if="edit.status" id="name" :placeholder="user.name" size="sm"/>
                <b-form-input v-else :value="user.name" disabled size="sm"/>
              </b-form-group>
            </b-row>
            <b-row>
              <b-form-group label-cols="4" label-cols-lg="4" label-size="sm" label="Email: " label-for="email">
                <b-form-input :value="user.email" disabled size="sm"/>
              </b-form-group>
            </b-row>
          </b-col>
        </b-row>
        <div v-if="edit.status">
          <b-row>
            <b-card>
              <b-form-group label-cols>
                <template #label>
                  <p><strong>Connect Account</strong></p>
                  <small>Connect with some SNS to make certificate strong.</small>
                </template>
                <b-list-group>
                  <b-list-group-item
                    v-for="provider in providers"
                    :key="provider.provider">
                    <b-row>
                      <b-col>
                        <b-form-group>
                          <b-icon :icon="provider.provider" :title="provider.provider" class="button"/><br>
                          <b-button variant="primary" :disabled="provider.link" @click="connectProvider(provider.providerId)" size="sm">Connect</b-button>
                          <b-button variant="light" :disabled="!provider.link" @click="unlinkProvider(provider.providerId)" size="sm">Unlink</b-button>
                        </b-form-group>
                      </b-col>
                    </b-row>
                  </b-list-group-item>
                </b-list-group>
              </b-form-group>
            </b-card>
          </b-row>
        </div>
        <div v-else>
          <b-row id="useraccountbind">
            <b-col>
              Connected Accounts
            </b-col>
          </b-row>
          <b-row class="d-flex justify-content-md-center">
            <div v-for="provider in providers" :key="provider.provider">
              <div v-if="provider.link">
                <b-col>
                  <b-icon :icon="provider.provider" @click="gotoTwitter" class="button"/>
                </b-col>
              </div>
            </div>
          </b-row>
        </div>
        <b-row v-if="edit.status">
          <b-col>
            <b-button @click="changeProfile" variant="outline-success">Save</b-button>
            <b-button @click="showModal" variant="outline-dark">Cancel</b-button>
          </b-col>
        </b-row>
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
        name: ''
      },
      providers: [
        {
          provider: 'twitter',
          providerId: 'twitter.com',
          link: false
        }
      ]
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
      firebase.auth().currentUser.updateProfile(data).then(()=> {
        firebase.database().ref(`/users/${this.user.uid}`).update({
          name: firebase.auth().currentUser.displayName
        }).then(this.showModal())
      }).catch((e) => {
        alert(e)
      })
    },
    _link_unlink_provider_local (providerId) {
      this.providers.forEach((p) => {
        if (p.providerId === providerId) {
          p.link = !p.link
        }
      })
    },
    connectProvider:async function (providerId) {
      var provider
      if (providerId === 'twitter.com') {
        provider = new firebase.auth.TwitterAuthProvider()
      } else
      if (providerId === 'facebook.com') {
        provider = new firebase.auth.FacebookAuthProvider()
      }
      await firebase.auth().currentUser.linkWithPopup(provider)
      this._link_unlink_provider_local(providerId)
    },
    unlinkProvider (providerId) {
      firebase.auth().currentUser.unlink(providerId).then(() => {
        this._link_unlink_provider_local(providerId)
      })
    },
    _getConnectedProviderData (providerId) {
      const providers = firebase.auth().currentUser.providerData
      var data = {}
      providers.forEach((p) => {
        if (p.providerId === providerId) {
          data = p
        }
      })
      return data
    },
    gotoTwitter () {
      const data = this._getConnectedProviderData('twitter.com')
      const uid = data.uid
      if (data) {
        const url = `https://twitter.com/intent/user?user_id=${uid}`
        window.open(url)
      } else {
        return true
      }
    },
    init: async function () {
      const user = await firebase.database().ref('/users/' + this.uid).once('value')
      this.user = user.val()
      firebase.auth().currentUser.providerData.forEach((p) => {
        this._link_unlink_provider_local(p.providerId)
      })
      try {
        const profileUserInBackend = await this.requestMethods.users.get_one_user(this.uid)
        this.ticketmax = profileUserInBackend.ticketmax
      } catch (e) {
        this.ticketmax = 0
      }
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
    await this.init()
  },
  watch: {
    uid: async function () {
      await this.init()
    }
  }
}
</script>