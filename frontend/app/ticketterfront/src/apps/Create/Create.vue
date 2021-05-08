<template>
  <div>
    <b-form>
      <b-form-group label="チケット名" >
        <b-form-input placeholder="チケットの名前" v-model="name"></b-form-input>
      </b-form-group>
      <b-form-group label="チケットの内容" >
        <b-form-input placeholder="チケットに記載する文章を記入してください" v-model="text"></b-form-input>
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
      text: ''
    }
  },
  methods: {
    createTicket: async function () {
      const result = await this.requestMethods.tickets.post_ticket(this.name, this.text)
      alert(result)
    }
  }
}
</script>