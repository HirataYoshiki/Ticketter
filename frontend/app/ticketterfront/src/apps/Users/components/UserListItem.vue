<template>
  <div>
    <b-list-group-item>
      <b-container>
        <b-row>
          <b-col>
            <b-avatar :src="user.photoURL"/>
          </b-col>
          <b-col>
            <b-row><strong>{{user.name}}</strong></b-row>
            <b-row><small class="text-muted">{{user.email}}</small></b-row>
          </b-col>
          <b-col>
            <b-row class="d-flex justify-content-md-center align-item-center">
              <b-button variant="primary" size="sm" @click="alert('hi')">チケットを渡す</b-button>
            </b-row>
          </b-col>
        </b-row>
      </b-container>
    </b-list-group-item>
  </div>
</template>
<script>
export default {
  name: 'userlistitem',
  props: {
    user: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
    }
  },
  methods: {
    gotoprofile () {
      this.$router.push({name: 'profile', params: {uid: this.user.uid}})
    },
    gotoInteraction () {}
  }
}
</script>