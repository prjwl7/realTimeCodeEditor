<script>
    import {navigate} from 'svelte-navigator'
    function exploreButton() {
    console.log('Navigating to Login');
    navigate('login');
    }

</script>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background-color: #f2f2f2;
        color: black;
    }

    h1 {
        font-size: 2rem;
        margin-bottom: 1rem;
    }

    p {
        font-size: 1.2rem;
        color: #666;
    }
</style>

<main>
    <h1>Welcome to the Code Editor!</h1>
    <p>Start coding and unleash your creativity.</p>
    <button on:click={exploreButton}>EXPLORE</button>
</main>
