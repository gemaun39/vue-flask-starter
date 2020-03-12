<template>
  <div class="about">
    <h1>Custom Text Generator</h1>
    <br>
    <form action="/Generator.vue">
        <label for="input_txt">Input text below</label>
        <br>
        <textarea rows="10" cols="90" name="input_txt" id="input_txt">
        </textarea>
    </form>
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
  name: "Custom",
  data(){
    return {
      message: ""
    }
  },

  methods: {
    get: function () {
      axios
      .get(URL + "/api/v1.0/custom")
      .then(response => {
        this.message = response.data.message
        console.log(response);
      })
    }
  }
};
</script>