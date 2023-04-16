<template>
	<transition name="fade">
		<div class="page-loader" v-if="isloaded">
			<img class="loader_img" src="@/assets/media/img/prewyv.png" />
		</div>
	</transition>
</template>

<script>
export default {
	data: () => {
		return {
			isloaded: true,
		};
	},
	mounted() {
		setTimeout(() => this.LGBT(), 2000);
	},
	methods: {
		LGBT() {
			return (this.isloaded = false);
		},
	},
};
</script>

<style scoped>
.page-loader {
	display: flex;
	justify-content: center;
	align-items: center;
	position: fixed;
	top: 0;
	left: 0;
	width: 100vw;
	height: 100vh;
	background-color: #fff;
	z-index: 9999;
}
.loader_img {
	height: 80vh;
	width: auto;
	background: #000;
}
.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
	opacity: 0;
}
@media (max-width: 600px) {
	.loader_img {
	max-width: 100vw;
}
}

</style>
