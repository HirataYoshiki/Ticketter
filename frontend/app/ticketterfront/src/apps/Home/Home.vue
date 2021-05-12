<template>
  <b-container>
    <b-row>
      <b-col>
        チケット一覧
      </b-col>
      <b-col>
        <b-button @click="changeTicket">{{showOnlyMyTicketsText}}</b-button>
      </b-col>
    </b-row>
    <b-row>
      <b-card-group >
        <div v-if="!tickets.length">
          <b-card
           border-variant="light"
           class="text-center shadow-lg m-2"
           title="チケットがありません">
            <b-card-text>
              チケットを作成しましょう。
            </b-card-text>
          </b-card>
        </div>
        <div v-else>
          <Ticket v-for="ticket in tickets" :key="ticket.ticketid" :ticket="ticket"/>
        </div>
      </b-card-group>
    </b-row>
  </b-container>
</template>

<script>
import firebase from 'firebase'
import Ticket from '@/components/Ticket.vue'
export default {
  name: 'Home',
  components: {
    Ticket
  },
  inject: [
    'user',
    'requestMethods'
  ],
  data () {
    return {
      tickets: [],
      showOnlyMyTickets: false
    }
  },
  methods: {
    changeTicket () {
      this.showOnlyMyTickets = !this.showOnlyMyTickets
    },
    gotoInteractions: function (ticket) {
      this.$router.push({name: 'interactions', params: {ticket: ticket}})
    }
  },
  computed: {
    myTickets () {
      return this.tickets.filter(ticket => ticket.uid === firebase.auth().currentUser.uid)
    },
    showOnlyMyTicketsText () {
      if (this.showOnlyMyTickets) {
        return 'すべてのチケットを表示'
      }
      return '自分のチケットを表示'
    }
  },
  created: async function () {
    if (this.user()) {
      try {
        const tickets = await this.requestMethods.tickets.get_all_tickets()
        if (tickets) {
          this.tickets = tickets
          return true
        } 
      } catch (e) {
        this.tickets = []
        return true
      }
    } else {
      this.tickets = []
    }
  }
}
</script>
