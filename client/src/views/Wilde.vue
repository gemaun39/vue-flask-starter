<template>
  <div class="about">
    <h1>Oscar Wilde Text Generator</h1>
    <br>
    <b-button v-on:click="get()">Get Generated Text</b-button>
    <br>
    <br>
    <br>
    <h5>{{ message }}</h5>
  </div>
</template>
<script>
// @ is an alias to /src
import axios from "axios"

const URL = "http://127.0.0.1:5000"

export default {
  name: "Wilde",
  data(){
    return {
      message: ""
    }
  },

  methods: {
    get: function () {
      axios
      .get(URL + "/api/v1.0/wilde")
      .then(response => {
        this.message = response.data.message
        console.log(response);
      })
    }
  }
};
</script>