<template>
  <b-list-group-item>
    <b-row>
      <b-col id="photourl">
        <b-row class="d-flex justify-content-center"><b-avatar :src="user.photoURL"/></b-row>
        <b-row>
          <b-col id="numberofticketgive">
            <small class="text-muted">発行数:{{ticket.volumemax}}</small>
          </b-col>
        </b-row>
      </b-col>
      <b-col>
        <b-row><strong>{{ticket.name}}</strong></b-row>
        <b-row><small class="text-muted">{{trimmedTicketText}}</small></b-row>
      </b-col>
    </b-row>
  </b-list-group-item>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'ticketminiinner',
  inject: ['requestMethods'],
  props: {
    ticket: Object
  },
  data () {
    return {
      user: {},
      interactions: []
    }
  },
  computed: {
    trimmedTicketText () {
      if (this.ticket.text.length > 16) {
        const text = this.ticket.text.substr(0,16) + '...'
        return text
      }
      return this.ticket.text
    }
  },
  created () {
    firebase.database().ref(`/users/${this.ticket.uid}`).once('value', (snap)=> {
      this.user = snap.val()
    })
  
  }
}
</script>