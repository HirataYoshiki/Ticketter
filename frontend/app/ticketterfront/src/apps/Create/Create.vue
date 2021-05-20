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
        <label for="content">チケットの内容 {{text.length}}/255文字</label>
        <b-form-textarea id="content" placeholder="チケットに記載する文章を記入してください" v-model="text" :state="text.length <= 255"></b-form-textarea>
      </b-form-group>
      <b-form-group>
        <label for="volume">
          <p>チケット発行枚数: {{volume}}枚<small>(最大100枚)</small></p>
        </label>
        <b-form-input id="volume" min="1" max="100" type="range" v-model="volume"/>
      </b-form-group>
      <b-button @click="modal=!modal">チケットを発行する</b-button>
    </b-form-group>
    <b-modal v-model="modal">
      <template #modal-header>
        <b-container>
          <b-row><b-col><small>チケット名: <strong>{{name}}</strong></small></b-col></b-row>
          <b-row><b-col><small>内容: <strong>{{text}}</strong></small></b-col></b-row>
          <b-row><b-col><small class="text-muted">発行数: {{volume}}</small></b-col></b-row>
        </b-container>
      </template>
      <p><strong>チケットを作成しますか？</strong></p>
      <p><small>チケットは1アカウントにつき最大3種類までしか発行できません。</small></p>
      <p><small>チケット発行後はチケットの削除、チケットの内容変更、チケット数の増刷はできません。</small></p>
      <template #modal-footer>
        <b-button variant="primary" @click="createTicket">OK</b-button>
        <b-button variant="secondary" @click="modal=!modal">Cancel</b-button>
      </template>
    </b-modal>
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
      volume: 100,
      modal: false
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
        this.modal = false
      })
    }
  }
}
</script>