<template>
	<div class="container">
		<div class="row">
			<div class="col-lg-12 title"><p>SHIPPING INFO</p></div>
			<div class="col-lg-12 body_form">
				<div class="col-lg-7 txt">
					<p class="subtitle">Контактные данные</p>
				</div>
				<div class="col-lg-7 in">
					<input
						placeholder="ФИО"
						v-model="purch_info.name"
						class="col-lg-10"
					/>
				</div>
				<div class="col-lg-7 in">
					<input
						placeholder="Контактный телефон"
						v-model.number="purch_info.phone"
						class="col-lg-10"
					/>
				</div>
				<div class="col-lg-7 in">
					<input
						placeholder="Email"
						v-model="purch_info.email"
						class="col-lg-10"
					/>
				</div>
				<div class="col-lg-7 txt"><p class="subtitle">Доставка (CDEK)</p></div>
				<div class="col-lg-6">
					<div class="col-lg-12">
						<input
							placeholder="Введите Ваш город"
							v-model="city.to_location"
							class="col-lg-5"
						/>
						<button @click="chekSity()" class="btn btn-dark col-lg-3">Применить</button>
					</div>
					<div class="" v-if="adderssesfromcdek.length == 0">
						<select v-model="addressName">
							<option disabled value="">Выберите один из пунктов выдачи</option>
							<option
								v-for="adderssesincity in adderssesfromcdek"
								v-bind:value="adderssesincity"
								:key="adderssesincity"
							>
								{{ adderssesincity }}
							</option>
						</select>
					</div>
					<div class="" v-else>
						{{ cdeknocity }}
					</div>
					<div class="">
						<p class="font-weight-bold" v-if="cdekprice > 0">DELIVERY: {{ cdekprice }} ₽</p>
						<p class="font-weight-bold">TOTAL: {{ getAllCart.data.total}} ₽</p>
					</div>
				</div>
			</div>
			<div class="col-lg-12 body_footer">
				<router-link :to="{path: 'cart'}"
					><button class="col-lg-1 btn_brdr btn-p w-100">
						<p>Назад</p>
					</button></router-link
				>
				<button
					type="button"
					class="col-lg-4 btn btn_black btn-p"
					:class="{disabled: activeBtn}"
					@click="order()"
				>
					<p>Подтвердить заказ</p>
				</button>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";
import router from "@/router";

export default {
	data() {
		return {
			purch_info: {
				name: "",
				email: "",
				phone: "",
				address: "" /* Тут должен быть город и адресс пункта выдачи */,
				delivery_price: "" /* Цена от сдека */,
				total_price: "0",
			},
			city: {
				to_location: "",
			},
			addressName: "",
			adderssesfromcdek: [],
			cdekreq: {},
			cdeknocity: "",
			cdekprice: 0,
		};
	},
	computed: {
		...mapGetters(["getAllCart"]),
		activeBtn() {
			if (
				this.purch_info.name == "" ||
				this.purch_info.email == "" ||
				this.purch_info.phone == "" ||
				this.addressName == ""
			) {
				return true;
			}
			return false;
		},
	},
	methods: {
		async chekSity() {
			/* headers */
			let csrf = document.cookie.split("=");
			let headers = {
				"Content-Type": "application/json;charset=utf-8",
				"X-CSRFToken": `${csrf[1]}`,
			};
			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}

			await axios
				.post(`${this.$store.state.BaseUrl}api/cdek/prices/`, this.city, {
					headers,
				})
				.then((response) => (this.cdekreq = response.data))
				.catch((error) => console.log(error));

			if (this.cdekreq.result == "Такого города нет") {
				this.cdeknocity = this.cdekreq.result;
				this.adderssesfromcdek = [];
				this.cdekprice = 0;
			} else {
				for (let adress in this.cdekreq.result) {
					if (adress == "addresses") {
						this.adderssesfromcdek = this.cdekreq.result[adress];
					} else if (adress == "amount") {
						this.cdekprice = this.cdekreq.result[adress].total_sum;
					}
				}
			}
		},

		order() {
			this.purch_info.total_price =
				parseInt(this.getAllCart.data.total * 100) / 100;

			/* headers */
			let csrf = document.cookie.split("=");
			let headers = {
				"Content-Type": "application/json;charset=utf-8",
				"X-CSRFToken": `${csrf[1]}`,
			};
			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}

			if (this.getAllCart.data.discount.code != null) {
				this.purch_info.code = `${this.getAllCart.data.discount.code}`;
			}

			if (this.addressName != null) {
				this.purch_info.address = `${this.addressName}, ${this.city.to_location}`;
				this.purch_info.delivery_price = this.cdekprice;
				this.purch_info.total_price =
					parseInt(this.getAllCart.data.total * 100) / 100 +
					parseInt(this.cdekprice * 100) / 100;
			}
			axios
				.post(
					`${this.$store.state.BaseUrl}api/orders/create_order/`,
					this.purch_info,
					{headers},
				)
				.then((response) => (window.location.href = `${response.data.url}`))
				.catch((error) => console.log(error));
		},
	},
};
</script>

<style scoped>
p {
	display: block;
	margin-block-start: 1em;
	margin-block-end: 1em;
	margin-inline-start: 0px;
	margin-inline-end: 0px;
}
.container {
	height: 100vh;
}

.txt p {
	font-weight: 700;
	font-size: 15px;
	line-height: 18px;
	position: relative;
	display: inline-block;
}

.txt p::before {
	content: "";
	position: absolute;
	bottom: -5px;
	right: 0;
	width: 100%;
	height: 2px;
	background-color: #000;
}

.title {
	border: 2px solid black;
	text-align: center;
	font-weight: 700;
	font-size: 15px;
	line-height: 18px;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-top: 50px;
}
.title p {
	margin: 10px;
}

.body_form {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	border: 2px solid black;
}
.body_footer {
	display: flex;
	justify-content: space-between;
	padding: 0px;
	margin-top: 50px;
}
.btn_brdr {
	border: 1px solid black;
	background-color: #fff;
}
.btn_black {
	background-color: #000;
	color: #fff;
}
.in {
	display: flex;
	align-items: flex-start;
	justify-content: flex-start;
	margin-bottom: 15px;
}

button p {
	margin: 0;
}

.btn-p {
	padding: 10px;
}

.btn.disabled {
	opacity: 1;
	color: white;
	background-color: #49484a;
}
.btn:hover {
	background-color: #000;
	color: #fff;
}

@media (min-width: 1400px) {
	.container,
	.container-lg,
	.container-md,
	.container-sm {
		max-width: 960px;
	}
}
@media (min-width: 1200px) {
	.container,
	.container-lg,
	.container-md,
	.container-sm {
		max-width: 960px;
	}
}
</style>
