<template>
  <div>
    <b-form>
      <b-form-group label="チケット名" >
        <b-form-input placeholder="チケットの名前" v-model="name"></b-form-input>
      </b-form-group>
      <b-form-group label="チケットの内容" >
        <b-form-textarea placeholder="チケットに記載する文章を記入してください" v-model="text"></b-form-textarea>
      </b-form-group>
      <b-form-group>
        <label for="volume">
          <p>チケット発行枚数: {{volume}}枚<small>(最大100枚)</small></p>
        </label>
        <b-form-input id="volume" min="1" max="100" type="range" v-model="volume"/>
      </b-form-group>
      <b-button @click="createTicket">チケットを発行する</b-button>
    </b-form>
  </div>
</template>
<script>
export default {
  name: 'create',
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
  methods: {
    createTicket: async function () {
      const result = await this.requestMethods.tickets.post_ticket(this.name, this.text, this.volume)
      alert(result)
    }
  }
}
</script>