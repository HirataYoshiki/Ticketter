<template>
  <b-card-group>
    <ProfileCard :uid="uid"/>
  </b-card-group>
</template>

<script>
import ProfileCard from './ProfileCard.vue'
  export default {
    name: 'profile',
    inject: [ 'requestMethods' ],
    props: {
      uid: String
    },
    components: {ProfileCard},
    data () {
      return {
      }
    }
  }
</script>