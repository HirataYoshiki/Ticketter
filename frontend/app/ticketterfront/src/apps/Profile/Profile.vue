<template>
  <div>
    <ProfileCard :uid="UID"/>
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
      uid: {
        type: String,
        default: ''
      },
      me: {
        type: Boolean,
        default: false
      }
    },
    components: {ProfileCard, Outer},
    data () {
      return {
        myTickets: [],
        gaves: [],
        givens: []
      }
    },
    computed: {
      UID () {
        if (this.me) {
          return firebase.auth().currentUser.uid
        }
        return this.uid
      }
    },
    created: async function () {
      if (this.me) {
        var myticketsnap = this.requestMethods.tickets.get_all_tickets()
        var gavesnap = this.requestMethods.interactions.get_ones_interactions({from_: firebase.auth().currentUser.uid})
        var givensnap = this.requestMethods.interactions.get_ones_interactions({to_: firebase.auth().currentUser.uid})
      } else {
        myticketsnap = this.requestMethods.tickets.get_all_tickets()
        gavesnap = this.requestMethods.interactions.get_ones_interactions({from_: this.uid})
        givensnap = this.requestMethods.interactions.get_ones_interactions({to_: this.uid})
      }
      [this.myTickets, this.gaves, this.givens] = await Promise.all([myticketsnap, gavesnap, givensnap])
    }
  }
</script>