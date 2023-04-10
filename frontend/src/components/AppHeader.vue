<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<header class="">
		<div class="header__body">
			<div class="row cntr">
					<app-burger></app-burger>
				<div class="col-lg-6 col-md-6 col-sm-6 col-4 logo">
					<p class="text-center w-100 logo_txt">
						<router-link to="/"> EVE </router-link>
					</p>
				</div>
				<div class="col-lg-3 col-md-3 col-sm-3 col-4">
					<div class="cart">
						<router-link to="/cart" @click="loadCart()"
							>CART ({{ getCartLenght }})</router-link
						>
					</div>
				</div>
			</div>
		</div>
	</header>
</template>
<style scoped>
.cntr {
	align-items: center;
	justify-content: end;
}
.burger {
}

header {
	position: sticky;
	top: 0;
	left: 0;
	width: 100%;
	z-index: 1000;
	background-color: #fff;
}
.header__body {
	padding-top: 2em;
	position: relative;
	width: 100%;
}
.logo {
	align-self: center;
}
.logo_txt {
	font-family: "Inter";
	font-style: normal;
	font-weight: 900;
	font-size: 30px;
	margin: 0;
}

.cart {
	text-align: right;
	font-family: "Inter";
	font-style: normal;
	font-weight: 700;
}


@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap");
</style>

<script>
import AppBurger from "@/components/AppBurger.vue";
import {mapGetters, mapActions} from "vuex";

export default {
	components: {
		AppBurger,
	},
	computed: {
		...mapGetters("cart", ["length"]),
		...mapGetters(["getAllCart"]),
		...mapGetters(["getCartLenght"]),
	},
	methods: {
		...mapActions(["loadCart"]),
		/*count() {
			let i = 0;
			for (let item in this.getCart.items) {
				i++;
			}
			return i;
		},*/
	},
};
</script>
