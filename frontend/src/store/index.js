import {
	createStore
} from 'vuex'

import products from './products'
import cart from './cart'

import axios from 'axios'
import {
	parse
} from '@fortawesome/fontawesome-svg-core'

const store = {
	modules: {
		products,
		cart
	},
	state: {
		categorieItems: [],
		prodIncart: [],
		allcart: [],
		cartLenght: 0,
		BaseUrl: window.location.origin + '/'

	},
	getters: {
		categorieItems: state => state.categorieItems,
		getCart: state => state.prodIncart,
		getAllCart: state => state.allcart,
		getCartLenght: state => state.cartLenght,

	},
	mutations: {
		setCategorieItems(state, prod) {
			state.categorieItems = prod;
		},
		setCart(state, prod) {

		},
		load(state, carts) {
			state.allcart = carts;
			for (let item in carts) {
				let i = 0;
				for (let some in carts[item]['items']) {
					i +=
						carts[item]['items'][some].quantity

				}
				state.cartLenght = i;
				return state.prodIncart = carts[item]
			}
		},
	},
	actions: {
		async categorieItems({
			commit,
			state
		}, ) {
			console.log(`${state.BaseUrl}api/shop/clothes/`)
			let res = await fetch(`${state.BaseUrl}api/shop/clothes/`);
			let prod = await res.json();
			commit('setCategorieItems', prod);
		},
		async loadCart({
			commit,
			state
		}) {
			/*TOKEN */


			let oldToken = localStorage.getItem('HTTP_TOKEN');
			if (oldToken === null || oldToken == "undefined") {
				let tkn = await axios.get(`${state.BaseUrl}api/cart/tnk/`,);
				let tokencart = tkn.data.token;
				localStorage.setItem('HTTP_TOKEN', tokencart);
			}


			let headers = {
				"Content-Type": "application/json;charset=utf-8",

			};
			if (localStorage.getItem("HTTP_TOKEN") !== "") {
				headers["TOKEN"] = localStorage.getItem("HTTP_TOKEN");
			}
			let products = await axios.get(`${state.BaseUrl}api/cart/`, {
				headers
			});
			commit('load', products);
		}
	},
	strict: process.env.NODE_ENV !== 'production'
}

export default createStore(store);