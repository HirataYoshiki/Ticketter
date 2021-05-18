<template>
  <div>
    <b-list-group-item class="button" @click="changeModal">
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
    <b-modal centered title="Select One" v-model="modal" ok-disabled>
      <template #modal-header>
        <b-container>
          <b-row>
            <b-col><strong :class="textcolor">{{GiveOrTake}}</strong></b-col>
            <b-col><b-avatar :src="user.photoURL"/></b-col>
            <b-col><strong>{{ticket.name}}</strong></b-col>
          </b-row>
        </b-container>
      </template>
      <b-list-group flush>
        <b-list-group-item @click="gotoprofile">
          <b-row>
            <b-col>
              <strong>プロフィールを見る</strong>
            </b-col>
            <b-col>
              <b-icon icon="arrow-right"/>
            </b-col>
          </b-row>
        </b-list-group-item>
        <b-list-group-item v-if="!give" @click="deleteTicket">
          <b-row>
            <b-col>
              <strong>削除</strong>
            </b-col>
            <b-col>
              <b-icon icon="trash-fill"/>
            </b-col>
          </b-row>
        </b-list-group-item>
      </b-list-group>
      <template #modal-footer>
        <b-button size="sm" variant="danger" @click="changeModal">
          Cancel
        </b-button>
      </template>
    </b-modal>
  </div>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'ticketminiinteractioninner',
  props: {
    interaction: {
      type: Object,
      default: null
    },
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
      },
      modal: false
    }
  },
  computed: {
    trimmedTicketText () {
      if (this.ticket.text.length > 20) {
        return this.ticket.text.substr(0,18) + '...'
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
  methods: {
    gotoprofile () {
      this.changeModal()
      this.$router.push({name: 'profile', params: {uid: this.user.uid}})
    },
    deleteTicket: async function () {
      const delete_my_ticket = [this.interaction.interactionid]
      await this.requestMethods.interactions.delete_my_ticket(delete_my_ticket)
      this.$destroy
    },
    changeModal () {
      this.modal =! this.modal 
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
