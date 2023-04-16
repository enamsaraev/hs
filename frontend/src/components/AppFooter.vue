<template>
  <div class="footer_container container">
    <div class="footer_block">
      <a src="@/assets/media/docks/About.pdf">About &nbsp;</a>
      <a src="@/assets/media/docks/Privacy_Policy.pdf">Privacy Policy&nbsp;</a>
      <a src="@/assets/media/docks/Dock_of.pdf">Terms of Service&nbsp;</a>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.footer_container {
  max-width: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  padding-bottom: 10px;
  bottom: 0;
}
.footer_block {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
a {
  text-decoration: none;
  color: #000;
  font-family: "Inter";
  font-style: normal;
  font-weight: 300;
  font-size: 0.6em;
  line-height: 10px;
}
</style>
