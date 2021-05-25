<template>
  <div>
    <b-list-group-item @click="changeModal">
      <b-row>
        <b-col id="photourl">
          <b-row class="d-flex justify-content-center"><b-avatar :src="user.photoURL"/></b-row>
          <b-row>
            <b-col id="numberofticketgive">
              <small class="text-muted">残り数:{{ticket.volumemax-number_of_ticket_gave(ticket.ticketid)}}/{{ticket.volumemax}}枚</small>
            </b-col>
          </b-row>
        </b-col>
        <b-col>
          <b-row><strong>{{ticket.name}}</strong></b-row>
          <b-row><small class="text-muted">{{trimmedTicketText}}</small></b-row>
        </b-col>
      </b-row>
    </b-list-group-item>
    <b-modal v-model="modal" centered>
      <template #modal-title>{{ticket.name}}</template>
      <p>チケットを配りますか？</p>
      <template #modal-footer>
        <b-button variant="primary" @click="gotoInteraction">OK</b-button>
        <b-button variant="secondary" @click="changeModal">Cancel</b-button>
      </template>
    </b-modal>
  </div>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'ticketminiinner',
  inject: ['requestMethods', 'profile_is_user','number_of_ticket_gave'],
  props: {
    ticket: Object
  },
  data () {
    return {
      user: {},
      interactions: [],
      modal: false
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
  methods: {
    changeModal () {
      if (this.profile_is_user()) {
        this.modal = !this.modal
      }
    },
    gotoInteraction () {
      this.$router.push({name: 'interactions', params: {ticket: this.ticket}})
    }
  },
  created () {
    firebase.database().ref(`/users/${this.ticket.uid}`).once('value', (snap)=> {
      this.user = snap.val()
    })
  
  }
}
</script>