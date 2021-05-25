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
              <b-nav pills>
                <b-nav-item active>
                  <b-nav-item-dropdown
                    text="チケットを渡す"
                    toggle-class="nav-link-custom text-white">
                    <div v-for="ticket in tickets" :key="ticket.ticketid">
                      <b-dropdown-item @click="openModal(ticket)">{{ticket.name}}</b-dropdown-item>
                      <b-modal v-model="modal" title="確認">
                        <b-overlay :show="overlay" rounded="sm">
                          <p class="text-center">このチケットを渡しますか？</p>
                          <p>チケット名：<strong>{{selectedTicket.name}}</strong></p>
                          <p>渡す相手：<strong>{{user.name}}</strong></p>
                        </b-overlay>
                        <template #modal-footer>
                          <b-button variant="primary" @click="giveTicket" :disabled="overlay">OK</b-button>
                          <b-button variant="secondary" @click="changeModal" :disabled="overlay">Cancel</b-button>
                        </template>
                      </b-modal>
                    </div>
                  </b-nav-item-dropdown>
                </b-nav-item>
              </b-nav>
            </b-row>
          </b-col>
        </b-row>
      </b-container>
    </b-list-group-item>
  </div>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'userlistitem',
  inject: ['requestMethods'],
  props: {
    user: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      tickets: [],
      modal: false,
      selectedTicket: {
        name: ''
      },
      overlay: false
    }
  },
  methods: {
    gotoprofile () {
      this.$router.push({name: 'profile', params: {uid: this.user.uid}})
    },
    gotoInteraction (ticket) {
      this.$router.push({name: 'interactions', params: {ticket: ticket}})
    },
    changeModal () {
      this.modal = !this.modal
    },
    changeOverlay () {
      this.overlay = !this.overlay
    },
    openModal (ticket) {
      this.selectedTicket = ticket
      this.changeModal()
    },
    giveTicket () {
      this.overlay = true
      const uidList = [this.user.uid]
      this.requestMethods.interactions.post_interactions(this.selectedTicket.ticketid, uidList).then(() => {
        this.changeOverlay()
        this.changeModal()
        alert('Success')
      })
    }
  },
  created: async function () {
    const params = {uid: firebase.auth().currentUser.uid}
    this.tickets = await this.requestMethods.tickets.get_all_tickets(params)
  }
}
</script>