<template>
  <div id="app">
    <Navbar v-if="this.$router.currentRoute.name !== 'login'" />
    <div class="app-inner">
      <router-view />
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
export default {
  components: {
    Navbar,
  },
};
</script>

<style>
.app-inner {
  padding: 10px 20px;
}
#app {
  background-color: rgba(19, 35, 47, 0.9);
  height: 2000px;
}
body {
  background-color: rgba(19, 35, 47, 0.9);
}
</style>
