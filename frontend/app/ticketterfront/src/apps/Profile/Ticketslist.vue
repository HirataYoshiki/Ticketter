<template>
  <b-card :title="title" no-body>
    <b-list-group flush>
      <b-list-group-item v-for="ins in displayList" :key="ins.interactionid">
        {{ins.ticketdata}}
      </b-list-group-item>
    </b-list-group>
  </b-card>
</template>
<script>
  import firebase from 'firebase'
  export default {
    name: 'ticketslist',
    props: {
      uid: String,
      interactions: {
        type: Boolean,
        default: false//false -> ticket given, true -> ticket gave
      }
    },
    inject: ['requestMethods'],
    data () {
      return {
        displayList: []
      }
    },
    methods: {
      getUserFromFirebase: async function (uid) {
        const snap = await firebase.database().ref(`users/${uid}`).once('value')
        return snap.val()
      },
      returnInteractionPromise: async function ({interactionid, ticketid, from_, to_, timestamp}) {
        const ticketdata = this.requestMethods.get_one_ticket(ticketid)
        const from_userdata = this.getUserFromFirebase(from_)
        const to_userdata = this.getUserFromFirebase(to_)
        return await Promise.all([
          interactionid,
          ticketdata,
          from_userdata,
          to_userdata,
          timestamp
        ])
      }
    },
    async created () {
      try {
        const interactionList = await this.requestMethods.interactions.get_ones_interactions(this.uid)
        const trimmedInteractionList = interactionList.filter(function (interaction) {
          if (this.interactions) {
            return interaction.from_ === this.uid
          }
          return interaction.to_ === this.uid
        })
        const Promises = []
        trimmedInteractionList.forEach((el) => {
          Promises = Promises.push(this.returnInteractionPromise(el))
        })
        const resolvedList = await Promise.all(Promises)
        this.displayList = resolvedList.map(el => {
          return {
            interactionid: el[0],
            ticketdata: el[1],
            from_userdata: el[2],
            to_userdata: el[3],
            timestamp: el[4]
          }
        })
        } catch(e) {
        this.displayList = []
        alert(e)
      }
    }
  }
</script>