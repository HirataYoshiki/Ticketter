<template>
  <div>
    <ProfileCard :uid="uid"/>
    <b-card-group deck>
      <Outer :addNew="false" :Objects="myTickets" :showAll="false" :title="'作ったチケット'"/>
      <Outer :addNew="false" :Objects="givens" :showAll="true" :interaction="true" :title="'もらったチケット'"/>
      <Outer :addNew="false" :Objects="gaves" :showAll="true" :give="true" :interaction="true" :title="'あげたチケット'"/>
    </b-card-group>
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
      [this.myTickets, this.gave, this.given] = await Promise.all([myticketsnap, gavesnap, givensnap])
    }
  }
</script>