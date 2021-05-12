<template>
  <b-list-group-item>
    <b-row>
      <b-col>
        <small :class="textcolor">{{GiveOrTake}}</small>
        <b-avatar :src="user.photoURL"/>
      </b-col>
      <b-col>
        <b-row><small>{{ticket.name}}</small></b-row>
        <b-row><small class="text-muted">{{trimmedTicketText}}</small></b-row>
      </b-col>
    </b-row>
  </b-list-group-item>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'ticketminiinteractioninner',
  props: {
    interaction: Object,
    give: {
      type: Boolean,
      default: false
    }
  },
  inject: ['requestMethods'],
  data () {
    return {
      user: {},
      ticket: {}
    }
  },
  computed: {
    trimmedTicketText () {
      if (this.ticket.text.length > 16) {
        return this.ticket.text.substr(0,15) + '...'
      }
      return this.ticket.text
    },
    textcolor () {
      if (this.give) {
        return 'text-danger'
      }
      return 'text-success'
    },
    GiveOrTake () {
      if (this.give) {
        return 'Give'
      }
      return 'Take'
    }
  },
  created: async function () {
    var personid = this.interaction.from_ 
    if (this.give) {
      personid = this.interaction.to_
    }
    const snap = firebase.database().ref(`/users/${personid}`).once('value')
    const ticketsnap = this.requestMethods.tickets.get_one_ticket(this.interaction.ticketid)
    let snapped
    [snapped, this.ticket] = await Promise.all([snap,ticketsnap])
    this.user = snapped.val()
  }
}
</script>
