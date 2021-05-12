<template>
  <b-form-group>
    <Ticket :ticket="ticket"/>
    <b-form-checkbox-group 
      v-model="selectedUser"
      :options="users"
      value-field="uid"
      text-field="name"
      />
    <b-button @click="giveticket">Interactiontest</b-button>
  </b-form-group>
</template>
<script>
  import firebase from 'firebase'
  import Ticket from '@/components/Ticket.vue'
  export default {
    name: 'interactions',
    inject: ['requestMethods'],
    components: {
      Ticket
    },
    props: {
      ticket: {
        type: Object,
        default: null
      }
    },
    data () {
      return {
        selectedTicket: {
          name: 'チケットを選択してください'
        },
        selectedUser: [],
        tickets: [],
        users: []
      }
    },
    methods: {
      giveticket: async function () {
        await this.requestMethods.interactions.post_interactions(this.selectedTicket.ticketid, this.selectedUser)
      }
    },
    created () {
      firebase.database().ref('/users').once('value').then((snap) => {
        this.users = snap.val()
      })
      this.requestMethods.tickets.get_all_tickets().then((tickets) => {
        this.tickets = tickets.filter(ticket => ticket.uid === firebase.auth().currentUser.uid)
      })
      if (this.ticket) {
        this.selectedTicket = this.ticket
      }
    }
  }
</script>