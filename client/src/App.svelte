<script>
	import { Router, Route } from 'svelte-navigator';
	import Landing from './routes/landing/+page.svelte';
	import Login from './routes/Login/+page.svelte';
	import Editor from './routes/editor/+page.svelte';
</script>

<main>
	<Router>
		<Route path="/" component={Landing} /> 
		<Route path="/login" component={Login} /> 
		<Route path="/editor" component={Editor} /> 
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