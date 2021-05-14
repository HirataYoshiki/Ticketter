<template>
<b-container>
  <b-card :title="ticket.name" :sub-title="createdAt" class="shadow" @click="gotoInteraction" style="max-width: 800px">
    <b-row>
      <b-col><b-avatar :src="creator.photoURL" @click="gotoProfile"/></b-col>
      <b-col>
        <b-row>
          <b-col>
            <small>作成者: {{creator.name}}</small>
          </b-col>
        </b-row>
        <b-row>
          <b-col>
            <small class="text-muted">発行数: {{ticket.volumemax}}枚</small>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <b-card-text class="bg-light">
      <p>{{ticket.text}}</p>
    </b-card-text>
  </b-card>
  </b-container>
</template>
<script>
import firebase from 'firebase'
export default {
  name: 'ticket',
  props: {
    ticket: Object
  },
  data () {
    return {
      creator: {
      }
    }
  },
  computed: {
    createdAt () {
      const dates = new Date(Date.parse(this.ticket.timestamp))
      const date = dates.getDate()
      const month = dates.getMonth() + 1
      const year = dates.getFullYear()
      return `作成日 ${year}/${month}/${date}`
    }
  },
  methods: {
    gotoProfile () {
      this.$router.push({name: 'profile', params: {uid: this.ticket.uid}})
    },
    gotoInteraction () {
      this.$router.push({name: 'interactions', params: {ticket: this.ticket}})
    }
  },
  created () {
    firebase.database().ref(`users/${this.ticket.uid}`).once('value').then((snap) => {
      this.creator = snap.val()
    })
  }
}
</script>