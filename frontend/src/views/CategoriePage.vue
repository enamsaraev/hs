<template>
	<div class="container" v-for="prod in productList" :key="prod.id">
		<div class="row h-100" v-if="prod.slug == this.$route.params.id">
			<router-link
				v-for="prs in prod.product_inventory"
				:key="prs.id"
				:to="{
					name: 'product',
					params: {slug: this.$route.params.id, id: prs.slug},
				}"
				class="col-lg-4 col-md-6 col-12 vhlink"
			>
				<div class="product" v-if="prs.parent_slug == this.$route.params.id">
					<div class="product_photo_wrapper">
						<img :src=prs.medias[0].img alt="" class="product_photo" />
					</div>
					<div class="product_txt">
						<div class="product_title">
							<p>{{ prs.name }}</p>
						</div>
						<div class="product_price">
							<p class="price">{{ parseInt(prs.retail_price) }} ₽</p>
						</div>
					</div>
				</div>
				<app-e-404 v-else />
			</router-link>
		</div>
	</div>
</template>

<script>
import {mapGetters, mapActions} from "vuex";
export default {
	/*data() {
    return {
      productByCategorie: [],
  }
  },*/
	computed: {
		...mapGetters("products", {productList: "getItemSlug"}),
	},
	methods: {
		...mapActions("products", ["categorieItems"]),
	},

	/* beforeUpdate() {
    this.$store.dispatch('categorieItems', this.$route.params.id);
  },*/

	/**
   * async categorieItems({ commit }, slug) {
			let res = await fetch(`http://127.0.0.1:8000/api/shop/clothes/?product__slug=${slug}`);
			let prod = await res.json();
			console.log('dada');
			commit('setCategorieItems', prod);
		}
     */
};
</script>

<style scoped>
.vhlink {
	height: 90vh;
}
.product_wrapper {
	height: 100%;
	width: 100%;
}
.product {
	display: flex;
	flex-direction: column;
	align-items: center;
	height: 100%;
	justify-content: center;
}
.product_title {
	font-family: "Inter";
	font-style: normal;
	font-weight: 700;
	font-size: 17px;
	line-height: 21px;
}
.product_photo_wrapper {
	width: 100%;
	margin: 0 auto;
	text-align: center;
}
.product_photo {
	max-width: 100%;
}
.product_txt {
	width: 100%;
	text-align: center;
	height: 15%;
	display: flex;
	flex-direction: column;
	justify-content: flex-end;
}
.product_title {
	text-transform: uppercase;
	font-family: "Inter";
	font-weight: 700;
	font-size: 17px;
	line-height: 21px;
}
.price {
	font-family: "Inter";
	font-style: normal;
	font-weight: 300;
	font-size: 15px;
	line-height: 18px;
}
@media screen and (max-width: 960px) {
	.vhlink {
		height: 50vh;
	}
}
@media screen and (max-width: 540px) {
	.vhlink {
		height: 75vh;
	}
}
</style>
