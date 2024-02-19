<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
     <!--GET SINGLE-->

    <div>
      <label for="postId">Enter Post ID:</label>
      <input type="text" id="postId" v-model="postId" />
      <button @click="makeGetSingleRequest">Make GET Request</button>
      <h2>{{getSingleResponse}}</h2>
    </div>

     <!--GET COLLECTION-->
    <div>
      <button @click="makeGetCollectionRequest">Make GET Request</button>
      <h2>{{getCollectionResponse}}</h2>
    </div>

     <!--POST-->
    <div>
      <label for="name">Title:</label>
      <input type="text" id="name" v-model="postData.name" />
      <label for="bpm">BPM:</label>
      <input type="number" id="bpm" v-model="postData.bpm" />
      <button @click="makePostRequest">Make POST Request</button>
      <h2>{{ postResponse }}</h2>
    </div>

    <!--DELETE-->
    <div>
      <label for="postId">Enter Post ID:</label>
      <input type="text" id="postId" v-model="postId" />
      <button @click="makeDeleteRequest">Make Delete Request</button>
      <h2>{{deleteResponse}}</h2>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  data(){
    return{
      getSingleResponse:null,
      getCollectionResponse:null,
      postResponse:null,
      putResponse:null,
      deleteResponse:null,
      contents:null,
      url:"http://localhost:8080/api/v1.0/audios",

      postData: {
        name: "",         // Input for title
        bpm: "",   // Input for description
      },
    }
  },
  name: 'HelloWorld',
  props: {
    msg: String
  },

  methods:{
    makeGetCollectionRequest(){
      axios.get(this.url).then((res) => (
        this.getCollectionResponse=res.data
      ))
    },
    makeGetSingleRequest() {
      console.log("Making GET request to:", `${this.url}/${this.postId}`);
      axios.get(`${this.url}/${this.postId}`)
        .then((res) => {
          console.log("Response:", res.data);
          this.getSingleResponse = res.data;
        })
        .catch((error) => {
         console.error("Error making GET single request:", error);
        });
    },

    makePostRequest(){
      console.log("Making POST request to:", this.url);
      axios
        .post(this.url, this.postData) // Assuming postId is part of the payload
        .then((res) => {
          console.log("Response:", res.data);
          this.postResponse = res.data;
        })
        .catch((error) => {
          console.error("Error making POST request:", error);
        })
    },
    makePutRequest(){
      return 0;
    },
    makeDeleteRequest(){
      console.log("Making DELETE request to:", `${this.url}/${this.postId}`);
      axios.delete(`${this.url}/${this.postId}`)
        .then((res) => {
          console.log("Response:", res.data);
          this.getSingleResponse = res.data;
        })
        .catch((error) => {
         console.error("Error making GET single request:", error);
        });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
