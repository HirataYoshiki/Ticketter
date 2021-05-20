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
              <b-button variant="primary" size="sm" @click="modal=!modal">チケットを渡す</b-button>
            </b-row>
          </b-col>
        </b-row>
      </b-container>
    </b-list-group-item>
    <b-modal v-model="modal">
      <b-nav vertical pills>
        <b-nav-item v-for="ticket in tickets" :key="ticket.ticketid" @click="gotoInteraction(ticket)">
          {{ticket.name}}
        </b-nav-item>
      </b-nav>
    </b-modal>
  </div>
</template>
<script>
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
      modal: false
    }
  },
  methods: {
    gotoprofile () {
      this.$router.push({name: 'profile', params: {uid: this.user.uid}})
    },
    gotoInteraction (ticket) {
      this.$router.push({name: 'interactions', params: {ticket: ticket}})
    }
  },
  created: async function () {
    const params = {uid: this.user.uid}
    this.tickets = await this.requestMethods.tickets.get_all_tickets(params)
  }
}
</script>