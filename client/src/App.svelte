<script>
	import { Router, Route } from 'svelte-navigator';
	import Landing from './routes/landing/+page.svelte';
	import Login from './routes/Login/+page.svelte';
</script>

<main>
	<Router>
		<!-- Define your routes using Route components -->
		<Route path="/" component={Landing} /> <!-- Example route for the home page -->
		<Route path="/login" component={Login} /> <!-- Route for the login page -->
	</Router>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>