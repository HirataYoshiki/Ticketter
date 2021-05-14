<template>
  <b-list-group-item>
    <b-row>
      <b-col align-self="center">
        <b-row class="d-flex justify-content-center"><small :class="textcolor">{{GiveOrTake}}</small></b-row>
        <b-row class="d-flex justify-content-center"><b-avatar :src="user.photoURL"/></b-row>
        <b-row class="d-flex justify-content-center"><small>{{createdAt}}</small></b-row>
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
      ticket: {
        text: ''
      }
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
    },
    createdAt () {
      const dates = new Date(Date.parse(this.interaction.timestamp))
      const date = dates.getDate()
      const month = dates.getMonth() + 1
      const year = dates.getFullYear()
      return `date: ${year}/${month}/${date}`
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
