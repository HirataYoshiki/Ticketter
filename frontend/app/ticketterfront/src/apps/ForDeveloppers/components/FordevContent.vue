<template>
  <b-card class="shadow-sm" :img-src="img" img-height="200px" style="width: 400px; height: 450px;" img-top :title="title">
    <b-card-text>
      {{text}}
    </b-card-text>
  </b-card>
</template>
<script>
export default {
  name: 'fordevcontent',
  props: {
    img: String,
    title: String,
    text: String
  }
}
</script>