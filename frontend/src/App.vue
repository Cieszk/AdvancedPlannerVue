<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
  import Navbar from "./components/Navbar";

  export default {
    name: 'App',
    components: {
      Navbar
    }
  }
</script>

<style>
    html, body {
        height: 100%;
        font-family: 'Roboto', sans-serif;
        background-color: #222;
        color: whitesmoke;
    }
  .jumbotron {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
    background-color: #303030;
    border-radius: 0.3rem;
}
</style>
