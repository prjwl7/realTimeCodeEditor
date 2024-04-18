<script>
	import { Router, Route } from 'svelte-navigator';
	import Landing from './routes/landing/+page.svelte';
	import Login from './routes/Login/+page.svelte';
	import Editor from './routes/editor/+page.svelte';
	import FileExplorer from './routes/fileExplorer/+page.svelte';
</script>

<main>
	<Router>
		<Route path="/" component={Landing} primary = {true}/> 
		<Route path="/login" component={Login}  primary = {false}/> 
		<Route path="/editor" component={Editor}  primary = {false} /> 
		<Route path="/fileExplorer" component={FileExplorer}  primary = {false} />
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