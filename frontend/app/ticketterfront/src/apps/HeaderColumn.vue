<template>
  <b-navbar type="dark" variant="dark">
    <b-navbar-nav>
      <b-nav-item to="/home"><b-icon icon="house"/>ホーム</b-nav-item>
      <b-nav-item to="/"><b-icon icon="vector-pen"/>つくる</b-nav-item>
      <b-nav-item to="/"><b-icon icon="card-heading"/>コレクション</b-nav-item>
      <b-nav-item to="/"><b-icon icon="people"/>プロフィール</b-nav-item>
      <b-nav-item to="/signin"><b-icon icon="person-fill"/>ログイン</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>
<script>
export default {
  name: 'headercolumn'
}
</script>