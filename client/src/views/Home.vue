<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/book.jpg" class="center"/>
    <br>
    <h2>Which text would you like to use?</h2>
    <br>
    <b-button v-on:click="get()">Click Me to Send API Request</b-button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios"

const URL = "http://127.0.0.1:5000"

export default {
  name: "Home",

  methods: {
    get: function () {
      axios
      .get(URL + "/api/v1.0/hello")
      .then(response => {
        console.log(response);
      })
    }
  }
};
</script>

<style scoped>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 20%;
}

</style>
