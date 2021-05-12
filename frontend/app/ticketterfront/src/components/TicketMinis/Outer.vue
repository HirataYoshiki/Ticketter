<template>
<b-card
  style="width: 300px;"
  class="m-2 p-0"
  header-tag="header"
  >
  <template #header>
    <b-row>
      <b-col>
        <strong>{{title}}</strong>
      </b-col>
      <b-col>
        <b-nav v-if="showAll">
          show all
        </b-nav>
      </b-col>
    </b-row>
  </template>
  <b-list-group flush>
    <div  v-if="interaction">
      <InteractionInner :interaction="interaction" v-for="interaction in Objects" :key="interaction.interactionid" :give="give"/>
    </div>
    <div v-else>
      <TicketInner :ticket="ticket" v-for="ticket in Objects" :key="ticket.ticketid"/>
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
    Objects: Array
  }
}
</script>