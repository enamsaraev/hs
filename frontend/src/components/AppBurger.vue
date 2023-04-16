<template>
	<div class="hamburger-menu col-lg-3 col-md-3 col-sm-3 ">
		<input id="menu__toggle" type="checkbox" />
		<label class="menu__btn" for="menu__toggle">
			<span></span>
		</label>

		<div class="menu__box">
			<div class="menu__body">
				<ul class="menu__list">
					<li v-for="cat in categoriesList" :key="cat.slug">
						<router-link
							:to="{name: 'category', params: {id: cat.slug}}"
							class="menu__item"
							href="#"
							>{{ cat.name }}</router-link
						>
					</li>
				</ul>	
				<div class="icon_container">
					<a class="icon" href="https://t.me/itbabyeve">
						<img src="@/assets/icons/tgpng.png" alt="" />
					</a>
					<a class="icon" href="https://vk.com/eve.clothes">
						<img src="@/assets/icons/vk.png" alt="" />
					</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
	computed: {
		...mapGetters("products", ["categoriesList"]),
	},
};
</script>

<style scoped>
#menu__toggle {
	opacity: 0;
	display: none;
}

#menu__toggle:checked ~ .menu__btn > span {
	transform: rotate(45deg);
}
#menu__toggle:checked ~ .menu__btn > span::before {
	top: 0;
	transform: rotate(0);
}
#menu__toggle:checked ~ .menu__btn > span::after {
	top: 0;
	transform: rotate(90deg);
}
#menu__toggle:checked ~ .menu__box {
	visibility: visible;
	left: 0;
}

.menu__btn {
	display: flex;
	align-items: center;
	position: fixed;
	left: 40px;

	width: 26px;
	height: 26px;

	cursor: pointer;
	z-index: 100;
}

.menu__btn > span,
.menu__btn > span::before,
.menu__btn > span::after {
	display: block;
	position: absolute;

	width: 100%;
	height: 3px;

	background-color: #000;
	border-radius: 20px;

	transition-duration: 0.25s;
}
.menu__btn > span::before {
	content: "";
	top: -8px;
}
.menu__btn > span::after {
	content: "";
	top: 8px;
}

.menu__box {
	display: block;
	position: fixed;
	visibility: hidden;
	top: 0;
	left: -100%;

	width: 100%;
	height: 100%;

	margin: 0;
	padding-top: 0;

	background-color: rgba(15, 14, 14, 0.23);
	box-shadow: 1px 0px 6px rgba(0, 0, 0, 0.2);

	transition-duration: 0.25s;
	text-align: center;

	z-index: 99;
}

.menu__box ul {
	list-style: none;
}
.menu__body {
	padding-top: 4em;
	display: flex;
	flex-direction: column;
	align-items: center;
	height: 100%;
	width: 180px;
	background-color: #fff;
	padding-top: 100px;
	justify-content: space-between;
}

.menu__item {
	display: block;
	padding: 12px 24px;

	color: #333;

	font-family: "Roboto", sans-serif;
	font-size: 20px;
	font-weight: 600;

	text-decoration: none;
	text-transform: uppercase;

	transition-duration: 0.25s;
}
.menu__list {
	padding-right: 7em;
	display: flex;
	flex-direction: column;
	align-items: center;
	margin: 0;
	padding: 0;
}

.icon_container {
	margin-bottom: 	2em;
	justify-self: flex-end;
	display: flex;
	width: 70%;
	justify-content: space-between;
}
.icon {
	width: 30px;
	height: 30px;
}

.hamburger-menu {
	position: relative;
	display: flex;
    align-items: center;
    justify-content: center;
}
@media screen and (max-width: 360px) {
	.cart {
		padding-right: 0px;
	}
	.menu__btn {
		left: 20px;
	}
	
}
@media screen and (max-width: 600px) {
	.menu__btn {
	left: calc(var(--bs-gutter-x) * 1);
}
}
</style>
