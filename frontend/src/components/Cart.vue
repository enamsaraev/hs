<template>
	<div class="container">
		<div class="row">
			<div class="page_title">
				<h2>Корзина</h2>
			</div>
			<div
				class="col-lg-4 product"
				v-for="prod in getAllCart.data.items"
				:key="prod.id"
			>
				<img :src="prod.img" alt="" class="cart_img" />
				<button
					class="btn_del btn"
					@click="delt(prod.slug, prod.size, prod.color)"
				></button>
				<h3 class="title mt">{{ prod.name }} ({{ prod.quantity }})</h3>
				<div class="size mt">{{ prod.size }}/{{ prod.color }}</div>
				<div class="mt btnsforq">
					<button
						@click="plusOne(prod.slug, prod.quantity, prod.size, prod.color)"
						class="btnsq"
					>
						+
					</button>
					<button
						@click="minusOne(prod.slug, prod.quantity, prod.size, prod.color)"
						class="btnsq"
					>
						-
					</button>
				</div>
				<div v-if="prod.total_item_price_with_dsc != null" class="price mt">
					{{ parseInt(prod.total_item_price_with_dsc * 100) / 100 }} ₽
				</div>
				<div class="price mt" v-else>
					{{ parseInt(prod.total_item_price * 100) / 100 }} ₽
				</div>
			</div>
			<div class="col-lg-12 total_block">
				<div class="col-lg-6 col-md-6 col-sm-6 col-12 total_price">
					TOTAL: {{ parseInt(this.getAllCart.data.total * 100) / 100 }} ₽
				</div>
				<div class="col-lg-2 col-md-4 col-sm-6 col-12 promo_block">
					<input
						v-if="promoIsRightCeck"
						class="in"
						placeholder="Промокод"
						v-model.lazy="promo.code"
						@change="test()"
					/>
					<div v-else class="in">Промокод применен</div>
				</div>
			</div>
			<button
				type="button"
				class="col-12 btn btn-dark btn-offer"
				@click="this.$router.push({name: 'checkout'})"
				:class="{disabled: makeOrder}"
			>
				Оформить заказ
			</button>
		</div>
	</div>
</template>

<script>
import {mapGetters, mapActions} from "vuex";
import axios from "axios";

export default {
	data() {
		return {
			promo: {
				code: "",
			},
		};
	},
	computed: {
		...mapGetters(["getAllCart", "getCartLenght"]),
		makeOrder() {
			if (this.getCartLenght == 0) {
				return true;
			}
			return false;
		},
		promoIsRightCeck() {
			if (this.getAllCart.data.discount.code == null) {
				return true;
			}
			return false;
		},
	},
	methods: {
		...mapActions("cart", ["setCnt"]),
		delt(slug, size, color) {
			let st = `${slug}-${size}-${color}`;

			let csrf = document.cookie.split("=");

			let header = {
				"Content-Type": "application/json;charset=utf-8",
				"X-CSRFToken": `${csrf[1]}`,
			};

			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				header["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}
			console.log(header);
			axios
				.delete(`${this.$store.state.BaseUrl}api/cart/delete/${st}/`, {
					headers:{header}
				}
				)
				.then((response) => this.$store.commit("load", response))
				.catch((error) => console.log(error));
		},
		test() {
			let csrf = document.cookie.split("=");
			let headers = {
				"Content-Type": "application/json;charset=utf-8",
				"X-CSRFToken": `${csrf[1]}`,
			};
			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}
			axios
				.post(`${this.$store.state.BaseUrl}api/coupon/check/`, this.promo, {
					headers,
				})
				.then((response) => this.$store.dispatch("loadCart"))
				.catch((error) => alert("Промокод не действителен"));
		},
		plusOne(slug, quantity, size, color) {
			let newquantity = quantity + 1;
			let addDate = {
				product_slug: slug,
				quantity: newquantity,
				size: size,
				color: color,
				update: "True",
			};

			/*Headers */
			let csrf = document.cookie.split("=");
			let headers = {
				"Content-Type": "application/json;charset=utf-8",
				"X-CSRFToken": `${csrf[1]}`,
			};
			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}
			axios
				.post(`${this.$store.state.BaseUrl}api/cart/add/`, addDate, {headers})
				.then((response) => this.$store.commit("load", response))
				.catch((error) => console.log(error));
		},
		minusOne(slug, quantity, size, color) {
			let newquantity = quantity - 1;
			if (newquantity >= 1) {
				let addDate = {
					product_slug: slug,
					quantity: newquantity,
					size: size,
					color: color,
					update: "True",
				};

				/*Headers */
				let csrf = document.cookie.split("=");
				let headers = {
					"Content-Type": "application/json;charset=utf-8",
					"X-CSRFToken": `${csrf[1]}`,
				};
				if (localStorage.getItem("HTTP_TOKEN") !== "") {
					headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
				}
				axios
					.post(`${this.$store.state.BaseUrl}api/cart/add/`, addDate, {headers})
					.then((response) => this.$store.commit("load", response))
					.catch((error) => console.log(error));
			}
		},
	},
};
</script>

<style scoped>
.page_title {
	height: 80px;
}

.title {
	font-weight: 700;
}
.product {
	display: flex;
	flex-direction: column;
	align-items: center;
	position: relative;
	margin-top: 50px;
}
.cart_img {
	height: 170px;
}
.btn_del {
	background: no-repeat url("@/assets/icons/del.png");
	background-size: contain;
	background-position: center;
	position: absolute;
	border: white;
	top: 0;
	right: 60px;
	width: 15px;
	height: 15px;
}
.mt {
	margin-top: 10px;
}
.total_block {
	margin-top: 30px;
	align-items: baseline;
	display: flex;
	justify-content: space-between;
	height: 30px;
}
.total_price {
	font-weight: 700;
	font-size: 15px;
	line-height: 18px;
}
.promo_block {
	display: flex;
	align-items: center;
	flex-wrap: nowrap;
}
.in {
	text-align: center;
	width: 100%;
}
.btn-offer {
	margin: 10px 0 40px 0;
}
.btnsq {
	color: #000000;
	--c: #000000; /* the color*/
	background: var(--_g) calc(var(--_p, 0%) - 100%) 0%,
		var(--_g) calc(200% - var(--_p, 0%)) 0%,
		var(--_g) calc(var(--_p, 0%) - 100%) 100%,
		var(--_g) calc(200% - var(--_p, 0%)) 100%;
	background-size: 50.5% calc(var(--_p, 0%) / 2 + 0.5%);
}

.btnsq:active {
	background-color: var(--c);
	color: #fff;
}

.btnsforq {
	display: flex;
	width: 35%;
	justify-content: space-around;
}

@media (min-width: 1400px) {
	.container,
	.container-lg,
	.container-md,
	.container-sm {
		max-width: 960px;
	}
}
@media (max-width: 576px) {
	.total_block {
		height: 100%;
		flex-wrap: wrap;
	}
	.in {
		margin-top: 15px;
	}
}
</style>
