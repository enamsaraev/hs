import { createRouter, createWebHistory } from 'vue-router'

import AppProductsList from '@/views/HomeView.vue';
import ProductPage from '@/views/ProductPage.vue';
import CategoriePage from '@/views/CategoriePage.vue';
import AboutPage from '@/views/AboutPage';

import AppCart from '@/components/Cart';
import AppCheckout from '@/components/Checkout';
import AppE404 from '@/components/E404';


const routes = [
	{
		name: 'catalog',
		path: '/',
		component: AppProductsList
	},
	{
		name: 'cart',
		path: '/cart',
		component: AppCart
	},
	{
		name: 'checkout',
		path: '/order',
		component: AppCheckout
	},
	{
		name: 'product',
		path: '/:slug/:id',
		component: ProductPage
	},
	{
		name: 'category',
		path: '/:id',
		component: CategoriePage
	},
	{
		name: 'about',
		path: '/about',
		component: AboutPage
	},
	{
		path: '/:any(.*)', // .*
		component: AppE404
	}
	
];

export default createRouter({
	routes,
	history: createWebHistory()
});
