<template>
  <div>
    <ProfileCard :uid="UID"/>
    <div>
      <Outer :addNew="false" :objects="myTickets" :title="'作ったチケット'"/>
      <Outer :addNew="false" :objects="givens" :showAll="true" :interaction="true" :title="'もらったチケット'"/>
      <Outer :addNew="false" :objects="gaves" :showAll="true" :interaction="true" :title="'あげたチケット'" :give="true"/>
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
    methods: {
      init: async function () {
        if (this.me) {
          var myticketsnap = this.requestMethods.tickets.get_all_tickets({uid: firebase.auth().currentUser.uid})
          var gavesnap = this.requestMethods.interactions.get_ones_interactions({from_: firebase.auth().currentUser.uid})
          var givensnap = this.requestMethods.interactions.get_ones_interactions({to_: firebase.auth().currentUser.uid})
        } else {
          myticketsnap = this.requestMethods.tickets.get_all_tickets({uid: this.uid})
          gavesnap = this.requestMethods.interactions.get_ones_interactions({from_: this.uid})
          givensnap = this.requestMethods.interactions.get_ones_interactions({to_: this.uid})
        }
        [this.myTickets, this.gaves, this.givens] = await Promise.all([myticketsnap, gavesnap, givensnap])
      },
      profile_is_user () {
        if (this.uid === firebase.auth().currentUser.uid || this.me== true) {
          return true
        }
        return false
      },
      number_of_ticket_gave: function (ticketid) {
        return this.gaves.filter(n => n.ticketid===ticketid).length
      }
    },
    created: async function () {
      await this.init()
    },
    watch: {
      uid: async function (val) {
        await this.init()
        this.uid = val
      },
      me: function (val) {
        this.me = val
      }
    },
    provide () {
      return {
        profile_is_user: this.profile_is_user,
        number_of_ticket_gave: this.number_of_ticket_gave
      }
    }
  }
</script>