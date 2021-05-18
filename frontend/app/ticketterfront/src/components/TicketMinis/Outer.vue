<template>
  <div>
    <b-card
      style="max-width: 600px;"
      class="m-2 p-0 shadow-lg"
      header-tag="header"
      no-body
      header-bg-variant="transparent"
      >
      <template #header>
        <div class="d-flex w-100 justify-content-between align-items-center">
          <div>
            <strong>{{title}}</strong>
          </div>
          <div>
            <b-nav v-if="showAll">
              <b-nav-item @click="showAllObject">show all</b-nav-item>
            </b-nav>
          </div>
        </div>
      </template>
      <b-list-group flush>
        <div v-if="interaction">
          <InteractionInner
            :interaction="interaction"
            v-for="interaction in limitedObjects"
            :key="interaction.interactionid"
            :give="give"
            :area-hidden="showall ? 'true': null"/>
            
        </div>
        <div v-else>
          <TicketInner :ticket="ticket" v-for="ticket in objects" :key="ticket.ticketid"/>
          <b-list-group-item v-if="objects.length<3">
            <b-nav class="d-flex justify-content-md-center">
              <b-nav-item to='/create'>
                <b-icon icon="plus-square"/> Create New
              </b-nav-item>
            </b-nav>
          </b-list-group-item>
        </div>
      </b-list-group>
    </b-card>
    <div v-if="showAll">
      <b-modal v-model="showall" scrollable centered>
        <template #modal-header>
          <b-row class="d-flex justify-content-md-between align-items-center">
            <b-col>
              <strong>{{title}}</strong>
            </b-col>
            <b-col>
              <b-row>
                <b-col><b-icon icon="funnel-fill"/></b-col>
                <b-col>{{sort}}</b-col>
              </b-row>
            </b-col>
          </b-row>
        </template>
        <b-list-group flush>
          <InteractionInner
            :interaction="interaction"
            v-for="interaction in objects"
            :key="interaction.interactionid"
            :give="give"
            :area-hidden="showall ? 'true': null"/>
        </b-list-group>
        <template #modal-footer>
          <b-button size="sm" variant="danger" @click="showAllObject">
            Cancel
          </b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>
<script>
import InteractionInner from './InteractionInner.vue'
import TicketInner from './TicketInner.vue'
export default {
  components: { TicketInner, InteractionInner },
  name: 'ticketminiouter',
  props: {
    title: String,
    showAll: Boolean,
    addNew: Boolean,
    interaction: {
      type: Boolean,
      default: false
    },
    give: {
      type: Boolean,
      default: false
    },
    objects: Array
  },
  data () {
    return {
      showall: false,
      sort: ''
    }
  },
  methods: {
    showAllObject () {
      this.showall = !this.showall
    }
  },
  computed: {
    limitedObjects () {
      if (this.objects.length > 3) {
        return this.objects.slice(0, 3)
      }
      return this.objects
    },
    showalltext () {
      if (this.showall) {
        return 'close'
      }
      return 'show all'
    }
  }
}
</script>