<template>
	<div v-for="pr in productList" :key="pr.id">
		<div v-if="pr.slug === this.$route.params.slug">
			<div v-for="prs in pr.product_inventory" :key="prs.id">
				<div v-if="prs.slug === this.$route.params.id">
					<div class="prod_cont container">
						<div class="row">
							<div class="col-lg-3 mt">
								<h3>{{ prs.name }}</h3>
								<div class="dscr_pc">
									<p>Описание товара:</p>
									<p>{{ prs.description }}</p>
								</div>
							</div>
							<div class="col-lg-6">
								<Carousel class="carousel_photo">
									<Slide v-for="slide in prs.medias" :key="slide">
										<div class="carousel__item">
											<img
												:src=slide.img
												alt=""
												class="carousel__img"
											/>
										</div>
									</Slide>

									<template #addons>
										<Navigation />
										<Pagination />
									</template>
								</Carousel>
							</div>
							<div class="col-lg-3 mt">
								
								<div class="variations">
									<p class="price">{{ parseInt(prs.retail_price) }} ₽</p>
									<div class="btns">
										<div
											v-for="variations in variationsProd"
											:key="variations.id"
											class="inline"
										>
											<input
												type="radio"
												class="btn-check"
												v-model="addDate.size"
												:value="variations.size[0]"
												:id="variations.size[0]"
											/>
											<label
												:for="variations.size[0]"
												class="btn btn-dark"
												name="btns"
											>
												{{ variations.size[0] }}
											</label>
										</div>
									</div>
									<button
										type="button"
										@click="add(this.id)"
										class="btn btn-dark"
										:class="{disabled: btnActive}"
									>
										Добавить в корзину
									</button>
								</div>
								
								<div class="dscr_mob">
									<p>Описание товара:</p>
									<p>{{ prs.description }}</p>
								</div>
							</div>
						</div>
					</div>
				</div>
				<app-e-404 v-else />
			</div>
		</div>
	</div>
  
  
</template>

<script>
import {Carousel, Slide, Pagination, Navigation} from "vue3-carousel";
import {mapGetters, mapActions} from "vuex";
import axios from "axios";
import AppE404 from "@/components/E404.vue";

export default {
	components: {
		Carousel,
		Slide,
		Pagination,
		Navigation,
		AppE404,
	},
	created() {
		this.variations(this.id);
	},

	data() {
		return {
			addDate: {
				product_slug: this.$route.params.id,
				quantity: "1",
				size: "",
				color: "Black",
				update: "False",
			},
			variationsProd: {},
		};
	},
	computed: {
		...mapGetters("products", {productList: "all"}),
		...mapGetters(["getCart"]),
		id() {
			for (const item in this.productList) {
				if (this.productList[item].slug === this.$route.params.slug) {
					for (const prod in this.productList[item].product_inventory) {
						if (
							this.productList[item].product_inventory[prod].slug ===
							this.$route.params.id
						) {
							return this.productList[item].product_inventory[prod].id;
						}
					}
				}
			}
		},
		btnActive() {
			if (this.addDate.size != "") {
				return false;
			}
			return true;
		},
	},
	methods: {
		add() {
			if (Object.keys(this.getCart.items).length !== 0) {
				for (let prod in this.getCart.items) {
					if (this.getCart.items[prod].slug == this.addDate.product_slug) {
						if (this.getCart.items[prod].size == this.addDate.size) {
							if (this.getCart.items[prod].color == this.addDate.color) {
								this.addDate.quantity = this.getCart.items[prod].quantity + 1;
								this.addDate.update = "True";
							}
						}
					}
				}
			}
			/*Headers */
			let csrf = document.cookie.split('=');
			let headers = {"Content-Type": "application/json;charset=utf-8","X-CSRFToken": `${csrf[1]}`};
			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}
			axios
				.post(`${this.$store.state.BaseUrl}api/cart/add/`, this.addDate, {headers})
				.then((response) => this.$store.commit("load", response))
				.catch((error) => console.log(error));
		},
		async variations(id) {
			let res = await fetch(`${this.$store.state.BaseUrl}api/shop/clothes/${id}`);
			let prod = await res.json();
			return (this.variationsProd = prod);
		},
		addSize(size) {
			this.addDate.size = size;
		},
	},
};
</script>

<style scoped>
.prod_cont {
	margin-bottom: 2em;
}

.mt {
	margin-top: 2em;
	padding: 0;
}
.mt h3{
	font-weight: 700;
}
.carousel__item {
	min-height: 150px;
	width: 100%;
	color: var(--vc-clr-white);
	font-size: 20px;
	border-radius: 8px;
	display: flex;
	justify-content: center;
	align-items: center;
}

.carousel__slide {
	padding: 10px;
}

.carousel__prev,
.carousel__next {
	box-sizing: content-box;
	color: #fff;
}

.carousel__pagination {
	display: none;
}

.carousel_photo {
	padding-top: -3.5em;
}

.carousel__img {
	width: 90%;
}

.price {
	font-weight: 700;
	font-size: calc(1.2rem + .3vw);	
	color: #000000;
}

.btns {
	width: 100%;
	display: flex;
	justify-content: space-around;
}

.btn-outline-dark {
	border-radius: 0% !important;
	border: 0;
	width: 24%;
}

.btn-dark {
	width: 100%;
	margin-top: 1em;
	border-radius: unset;
	font-weight: 700;
	font-size: 15px;
	line-height: 18px;
	padding-top: 10px;
	padding-bottom: 10px;
}
.btns input[type="radio"]:checked + label {
	background: #fff;
	color: #000;
}
.inline {
	display: flex;
	width: 100%;
}
.variations {
	display: flex;
	align-items: center;
	flex-direction: column;
}

@media screen and (max-width: 980px) {
	.dscr_pc{
		display: none;
	}
	.dscr_mob{
		display: block;
	}

}
@media screen and (min-width: 980px) {
	.dscr_pc{
		display: block;
	}
	.dscr_mob{
		display: none;
	}

}

</style>
