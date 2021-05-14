<template>
  <div>
    <b-form-group label="Pre-View">
      <Ticket :ticket="pre_ticket"/>
    </b-form-group>
    <b-form-group>
      <b-form-group label="チケット名" >
        <b-form-input placeholder="チケットの名前" v-model="name"></b-form-input>
      </b-form-group>
      <b-form-group>
        <label for="content">チケットの内容 {{text.length}}/255?</label>
        <b-form-textarea id="content" placeholder="チケットに記載する文章を記入してください" v-model="text"></b-form-textarea>
      </b-form-group>
      <b-form-group>
        <label for="volume">
          <p>チケット発行枚数: {{volume}}枚<small>(最大100枚)</small></p>
        </label>
        <b-form-input id="volume" min="1" max="100" type="range" v-model="volume"/>
      </b-form-group>
      <b-button @click="createTicket">チケットを発行する</b-button>
    </b-form-group>
  </div>
</template>
<script>
import firebase from 'firebase'
import Ticket from '../../components/Ticket.vue'
export default {
  name: 'create',
  components: {
    Ticket
  },
  inject: [
    'requestMethods'
  ],
  data () {
    return {
      name: '',
      text: '',
      volume: 100
    }
  },
  computed: {
    pre_ticket () {
      const uid = firebase.auth().currentUser.uid
      return {
        name: this.name,
        text: this.text,
        volumemax: this.volume,
        timestamp: Date(),
        uid: uid
      }
    }
  },
  methods: {
    createTicket () {
      this.requestMethods.tickets.post_ticket(this.name, this.text, this.volume).then(() => {
        alert("successfully complete creating ticket")
        this.name = ''
        this.text = ''
        this.volume = 100
      })
    }
  }
}
</script>