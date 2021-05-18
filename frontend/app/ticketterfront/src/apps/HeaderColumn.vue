<template>
  <b-navbar type="dark" variant="dark">
    <b-navbar-brand variant="light">Ticketter</b-navbar-brand>
    <b-navbar-nav>
      <b-nav-item to="/"><b-icon icon="house"/><small>ホーム</small></b-nav-item>
      <b-nav-item to="/create"><b-icon icon="vector-pen"/><small>つくる</small></b-nav-item>
      <b-nav-item to="/users"><b-icon icon="people-fill"/><small>ユーザー</small></b-nav-item>
      <b-nav-item-dropdown
        id="my-nav-dropdown"
        text="その他"
        toggle-class="nav-link-custom"
        right
        >
        <b-dropdown-item to="/"><b-icon icon="code-slash"/><small> 開発者の方</small></b-dropdown-item>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item @click="Logout"><b-icon icon="door-closed-fill"/><small> ログアウト</small></b-dropdown-item>
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
  methods: {
    Logout () {
      if (!this.$route.path==='/') {
        this.$router.push('/')
      }
      firebase.auth().signOut()
    }
  }
}
</script>