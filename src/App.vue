<template>
  <div id="app">
    <Navbar />
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
</style>
