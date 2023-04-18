<template>
	<div class="footer_container container">
		<div class="row w-100 cntr">
			<div class="col-lg-6 col-md-6 col-sm-6 col-4">
				<div class="footer_block">
					<a href="@/assets/media/docks/About.pdf">About</a>
					<a href="@/assets/media/docks/Privacy_Policy.pdf"
						>Privacy Policy</a
					>
					<a href="@/assets/media/docks/Dock_of.pdf">Terms of Service</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {};
</script>

<style scoped>

.cntr{
	align-items: center;
	justify-content: center;
}
.footer_container {
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
