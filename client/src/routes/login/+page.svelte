<script>
    import { navigate } from 'svelte-navigator';
    let email = '';
    let password = '';

    async function sendData(event) {
        try {
        const response = await fetch('http://localhost:5000/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
        console.log('Success');
        navigate('/fileExplorer');
    } else {
        console.error('Failed:', response.status);
    }
    } catch (error) {
    console.error('Error:', error);
    }
    }
</script>

<main>
    <h1>Login</h1>

    <form on:submit|preventDefault={sendData} method="post" action="http://localhost:5000/api/data">
        <label for="email">Email:</label>
        <input type="email" id="email" bind:value={email} required />

        <label for="password">Password:</label>
        <input type="password" id="password" bind:value={password} required />

        <button type="submit">Login</button>
    </form>
</main>

<style>
    main {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
    }

    h1 {
        text-align: center;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    label {
        font-weight: bold;
    }

    input {
        padding: 0.5rem;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    button {
        padding: 0.5rem 1rem;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
</style>