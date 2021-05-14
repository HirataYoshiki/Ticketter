<template>
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
          <b-nav-item @click="showAllObject">{{showalltext}}</b-nav-item>
        </b-nav>
      </div>
    </div>
  </template>
  <b-list-group flush>
    <div v-if="interaction">
      <b-overlay :show="showall">
        <InteractionInner
          :interaction="interaction"
          v-for="interaction in limitedObjects"
          :key="interaction.interactionid"
          :give="give"
          :area-hidden="showall ? 'true': null"/>
          <template #overlay>
            <b-card header-tag="header" no-body style="min-width: 600px;">
              <template #header>
                <b-row class="justify-content-md-between">
                  <b-col>
                    <h5><strong>{{title}}</strong></h5>
                  </b-col>
                  <b-col>
                    <b-row class="justify-content-md-center">
                      <b-icon icon="funnel-fill"/>
                      <small class="text-muted">{{sort}}</small>
                    </b-row>
                  </b-col>
                  <b-col>
                    <b-nav>
                      <b-nav-item @click="showAllObject">
                        close
                      </b-nav-item>
                    </b-nav>
                  </b-col>
                </b-row>
              </template>
              <b-list-group flush>
                <InteractionInner
                  :interaction="interaction"
                  v-for="interaction in objects"
                  :key="interaction.interactionid"
                  :give="give"/>
              </b-list-group>
            </b-card>
          </template>
      </b-overlay>
    </div>
    <div v-else>
      <TicketInner :ticket="ticket" v-for="ticket in objects" :key="ticket.ticketid"/>
      <b-list-group-item v-if="objects.length<3">
        <b-nav class="d-flex justify-content-md-center">
          <b-nav-item to='/create'>
            <b-icon icon="plus-square"/> Add New
          </b-nav-item>
        </b-nav>
      </b-list-group-item>
    </div>
  </b-list-group>
</b-card>
  
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