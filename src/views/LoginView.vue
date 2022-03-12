<template>
  <form class="box login-box">
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input class="input" type="email" placeholder="e.g. alex@example.com" />
      </div>
    </div>
    <div class="field">
      <label class="label">Password</label>
      <div class="control">
        <input class="input" type="password" placeholder="********" />
      </div>
    </div>
    <button class="button is-primary">Sign in</button>
  </form>
</template>
<script>
export default {
  name: "HomeView",
  components: {},
  data() {
    return {};
  },
};
</script>

<style>
.login-box {
  max-width: 300px;
  margin: 50px auto;
}
</style>
