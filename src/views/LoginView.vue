<template>
  <form class="box login-box">
    <div class="field">
      <label class="label">Email</label>
      <div class="control">
        <input
          class="input"
          placeholder="e.g.alex@example.com"
          v-model="email"
        />
      </div>
    </div>
    <div class="field">
      <label class="label">Password</label>
      <div class="control">
        <input
          class="input"
          type="password"
          placeholder="********"
          v-model="password"
        />
      </div>
    </div>
    <button class="button is-primary" @click="login">Sign in</button>
  </form>
</template>
<script>
export default {
  name: "HomeView",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login() {
      if (this.email === "admin" && this.password === "1234") {
        this.$router.push("/home");
      }
    },
  },
};
</script>

<style>
.login-box {
  width: 300px;
  height: 250px;
  position: fixed;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
</style>
