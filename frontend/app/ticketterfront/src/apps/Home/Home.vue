<template>
  <b-container>
    <b-row>
      <b-col>
        チケット一覧
      </b-col>
    </b-row>
    <b-row>
      <b-card-group deck>
        <div v-if="!tickets">
          <b-card
           border-variant="light"
           class="text-center"
           title="チケットがありません">
            <b-card-text>
              チケットを作成しましょう。
            </b-card-text>
          </b-card>
        </div>
        <div v-else>
          <b-card v-for="ticket in tickets" :key="ticket.ticketid"
            border-variant="light"
            class="text-center"
            :title="ticket.name"
            footer-tag="footer"
          >
          <b-card-text>
            {{ticket.text}}
          </b-card-text>
          <template #footer>
            <small class="text-muted">
              timestamp: {{ticket.timestamp}}
            </small>
          </template>
          </b-card>
        </div>
      </b-card-group>
    </b-row>
  </b-container>
</template>

<script>
import firebase from 'firebase'
export default {
  name: 'Home',
  inject: [
    'user',
    'requestMethods'
  ],
  data () {
    return {
      tickets: [] 
    }
  },
  computed: {
    myTickets () {
      return this.tickets.filter(ticket => ticket.uid === firebase.auth().currentUser.uid)
    }
  },
  created: async function () {
    if (this.user) {
      const tickets = await this.requestMethods.tickets.get_all_tickets()
      if (tickets) {
        this.tickets = tickets
        return true
      }
    }
    this.tickets = []
    return true
  }
}
</script>
