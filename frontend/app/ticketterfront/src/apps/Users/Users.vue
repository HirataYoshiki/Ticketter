<template>
  <b-form class="pt-2">
    <b-form-group label="ユーザー一覧" label-cols="4">
      <b-input-group size="sm" class="mb-2">
        <b-input-group-prepend is-text>
          <b-icon icon="search"></b-icon>
        </b-input-group-prepend>
        <b-form-input placeholder="Search by ID..." v-model="search"/>
        <b-input-group-append>
          <b-button @click="filterUser">Search</b-button>
        </b-input-group-append>
      </b-input-group>
    </b-form-group>
    <b-form-group>
      <b-list-group v-if="displayUsers">
        <UserListItem v-for="user in displayUsers" :user="user" :key="user.uid"/>
      </b-list-group>
      <b-list-group v-else>
        <b-list-group-item>
          お探しのユーザーは見つかりません。
        </b-list-group-item>
      </b-list-group>
    </b-form-group>
  </b-form>
</template>
<script>
import firebase from 'firebase'
import UserListItem from './components/UserListItem.vue'
export default {
  name: 'users',
  components: { UserListItem },
  data () {
    return {
      users: {},
      displayUsers: null,
      search: ''
    }
  },
  methods: {
    filterUser () {
      if (this.search == '') {
        this.displayUsers = this.users
      } else {
        this.displayUsers = this._filtering_user(this.search)
      }
    },
    _filtering_user (uid) {
      const result = this.users[uid]
      if (result == null) {
        return null
      }
      return {uid: result}
    }
  },
  created: async function () {
    const usersSnap = await firebase.database().ref('/users').once('value')
    this.users = usersSnap.val()
    this.displayUsers = usersSnap.val()
  }
}
</script>