<template>
  <b-navbar type="dark" variant="dark">
    <b-navbar-nav>
      <b-nav-item to="/"><b-icon icon="house"/><small>ホーム</small></b-nav-item>
      <b-nav-item to="/create"><b-icon icon="vector-pen"/><small>つくる</small></b-nav-item>
      <b-nav-item to="/"><b-icon icon="card-heading"/><small>コレクション</small></b-nav-item>
      
      <b-nav-item-dropdown
        id="my-nav-dropdown"
        text="その他"
        toggle-class="nav-link-custom"
        right
        >
        <b-dropdown-item :to="to"><b-icon icon="people"/><small>プロフィール</small></b-dropdown-item>
        <b-dropdown-item to="/"><b-icon icon="code-slash"/><small>開発者の方</small></b-dropdown-item>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item @click="Logout"><b-icon icon="door"/><small>ログアウト</small></b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </b-navbar>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'headercolumn',
  inject: [
    'user'
  ],
  data () {
    return {
      to: ""
    }
  },
  methods: {
    Logout () {
      this.$router.push('/')
      firebase.auth().signOut()
    }
  },
  created () {
    firebase.auth().onAuthStateChanged(user => {
      if (user) {
        const myUid = user.uid
        this.to = `/profile/${myUid}`
      } else {
        this.to = '/'
      }
    })
  }
}
</script>