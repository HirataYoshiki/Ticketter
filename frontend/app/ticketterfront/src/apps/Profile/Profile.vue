<template>
  <div>
    <ProfileCard :uid="uid"/>
    <div>
      <Outer :addNew="false" :objects="myTickets" :showAll="false" :title="'作ったチケット'"/>
      <Outer :addNew="false" :objects="givens" :showAll="true" :interaction="true" :title="'もらったチケット'"/>
      <Outer :addNew="false" :objects="gaves" :showAll="true" :give="true" :interaction="true" :title="'あげたチケット'"/>
    </div>
  </div>
</template>

<script>
import Outer from '../../components/TicketMinis/Outer.vue'
import ProfileCard from './ProfileCard.vue'
import firebase from 'firebase'
  export default {
    name: 'profile',
    inject: [ 'requestMethods' ],
    props: {
      uid: String
    },
    components: {ProfileCard, Outer},
    data () {
      return {
        myTickets: [],
        gaves: [],
        givens: []
      }
    },
    created: async function () {
      const myticketsnap = this.requestMethods.tickets.get_all_tickets()
      const gavesnap = this.requestMethods.interactions.get_ones_interactions({from_: firebase.auth().currentUser.uid})
      const givensnap = this.requestMethods.interactions.get_ones_interactions({to_: firebase.auth().currentUser.uid});
      [this.myTickets, this.gaves, this.givens] = await Promise.all([myticketsnap, gavesnap, givensnap])
    }
  }
</script>