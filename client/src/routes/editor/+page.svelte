<script>
    // import { responseStore } from '../fileExplorer/+page.svelte';

    let theme = 'light';
    export let fileContent = ''; // Local variable to store content from responseStore

    function changeTheme() {
        theme = theme === 'light' ? 'dark' : 'light';
        var editorColor = document.getElementById('editor');
        editorColor.style.setProperty('--editor-bg-color', theme === 'light' ? 'white' : '#0C0C0C');
        editorColor.style.setProperty('--editor-text-color', theme === 'light' ? '#0C0C0C' : 'white');

        var textEditorColor = document.getElementById('textEditor');
        textEditorColor.style.setProperty('--editor-bg-color', theme === 'light' ? 'white' : '#0C0C0C');
        textEditorColor.style.setProperty('--editor-text-color', theme === 'light' ? '#0C0C0C' : 'white');
    }

    // Listen for changes in responseStore
    // $: {
    //     $responseStore // reactive statement to listen to changes in responseStore
    //     fileContent = $responseStore; // Update fileContent when responseStore changes
    // }
</script>
<style>
    .editor {
        width: 100%;
        height: 300px;
        border: 1px solid #ccc;
        padding: 10px;
        font-family: monospace;
        background-color: var(--editor-bg-color);
        color: var(--editor-text-color, black);
    }

    /* .theme-button {
        margin-top: 10px;
        padding: 5px 10px;
        background-color: var(--button-bg-color, gray);
        color: var(--button-text-color, white);
        border: none;
        cursor: pointer;
    } */

    #textEditor {
        width: 100%;
        height: 100%;
        border: none;
        background-color: var(--editor-bg-color);
        color: var(--editor-text-color, black);
    }
</style>

<div class="editor" id="editor">
    <textarea bind:value={fileContent} placeholder="//Your Code" id="textEditor" ></textarea>
</div>
<!-- 
<button class="theme-button" on:click={changeTheme}>
    {theme === 'light' ? 'Dark Theme' : 'Light Theme'}
</button> -->