const BASEURL = 'http://127.0.0.1:8000/api/shop/';

export default {
	namespaced: true,
	state: {
		items: [],
		categories: [],
		itemsAll: [],
		itemSlug:[],

	},
	getters: {
		all: state => state.items,
		one: state => id => state.items.find(item => item.id === id),
		categoriesList: state => state.categories,
		getItemsAll: state => state.itemsAll,
		getItemSlug: state => state.itemSlug
	},
	mutations: {
		setItems(state, products) {
			state.items = products;
			for (let prod in products) {
				state.itemSlug.push(products[prod]);
				for (let prodId in products[prod].product_inventory) {
					state.itemsAll.push(products[prod].product_inventory[prodId]);
				}
			}

		},
		setCategories(state, prod) {
			state.categories = prod;
		},
		setCategorieItems(state, prod) {
			state.categorieItems = prod;
		},
	},
	actions: {
		async load({
			commit
		}) {
			let response = await fetch('http://127.0.0.1:8000/api/shop/clothes/');
			let products = await response.json();
			commit('setItems', products);

			let res = await fetch('http://127.0.0.1:8000/api/shop/catalog/');
			let prod = await res.json();
			commit('setCategories', prod);
		},
	},
};