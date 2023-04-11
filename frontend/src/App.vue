<template>
    <app-preloader></app-preloader>
		<app-header></app-header>
		<router-view />
		<app-footer></app-footer>
</template>

<style>
body {
	overflow-x: hidden;
}
.bd {
	border: 1px solid black;
}

#app {
	width: 100%;
	min-height: 100vh;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}
.bd {
	border: 1px solid black;
}
a:hover {
	color: black !important;
}
a:-webkit-any-link {
	color: black;
	cursor: pointer;
	text-decoration: none;
}
.app {
	margin-top: 3em;
	margin-bottom: 4em;
}
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap");
* {
	font-family: "Inter";
}
</style>

<script>
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import AppPreloader from "@/components/AppPreloader.vue";

export default {
	components: {
		AppHeader,
		AppFooter,
		AppPreloader,
	},
};
/**
<nav>
  <router-link to="/">Home</router-link> |
  <router-link to="/about">About</router-link>
</nav>
*/
</script>
