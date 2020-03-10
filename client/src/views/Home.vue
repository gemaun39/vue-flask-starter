<template>
  <div class="home">
    <h2>Welcome to Text Generator</h2>
    <br>
    <img alt="Vue logo" src="../assets/book.jpg" class="center"/>
    <br>
    <h2>What does this program do?</h2>
    <h4 class="alt_text">This program takes a passage of text and generates sentences <br>based on the passage's word choice.</h4>
    <br>
    <h2>Which text would you like to generate from?</h2>
    <!-- <b-button v-on:click="get()">Click Me to Send API Request</b-button> -->
    <br>
    <router-link to="/shakespeare" class="link_text">Shakespeare Text Generator</router-link>
    <br>
    <router-link to="/sherlock" class="link_text">Sherlock Holmes Text Generator</router-link>
    <br>
    <router-link to="/wilde" class="link_text">Oscar Wilde Text Generator</router-link>
    <br>
    <router-link to="/austen" class="link_text">Jane Austen Text Generator</router-link>
    <br>
    <br>
    <br>
    <h2>Or, <router-link to="/generator" class="alt_text">create a generator here</router-link> by inputing your own text</h2>
    <h5 class="alt_text">Note: Larger word count = more accurate</h5>
    <br>
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

.alt_text {
  color: #577c85;
}

.link_text {
  font-size: 25px;
  font-weight: bold;
  color: #577c85;
}

</style>
