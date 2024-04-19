<script>
    import Editor from '../editor/+page.svelte';
    import { writable } from 'svelte/store';
    
    // Store for holding opened files
    export const openedFiles = writable([]);

    // Variable to track the index of the active tab
    let activeTabIndex = 0;

    // Function to set the active tab index
    function setActiveTabIndex(index) {
        activeTabIndex = index;
    }

    // Function to handle file upload
    async function uploadFile(event) {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', event.target.files[0]);

        try {
            const response = await fetch('http://127.0.0.1:5000/handleFiles', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const { filename, file_content } = await response.json(); // Parse JSON response
                openedFiles.update(files => [...files, { filename, content: file_content }]);
            } else {
                console.log('Failed to upload file');
            }
        } catch (error) {
            console.error('An error occurred while uploading the file:', error);
        }
    }

    // Function to remove a file from opened files
    function closeFile(event, index) {
        event.stopPropagation(); // Prevent event bubbling
        openedFiles.update(files => files.filter((file, i) => i !== index));
        // Adjust activeTabIndex if the closed file was the active tab
        if (activeTabIndex === index && openedFiles.length > 0) {
            setActiveTabIndex(Math.max(index - 1, 0));
        }
    }

    // Handle keyboard events for accessibility
    function handleKeyDown(event, index) {
        if (event.key === 'Enter' || event.key === ' ') {
            closeFile(event, index);
        }
    }
</script>

<main>
    <div class="mainContainer">
        <div class="fileUploadContainer">
            <div class="fileUploadButtons">
                <button>New File</button>
                <button>New Folder</button>
            </div>
            <div class="fileUpload">
               <div class="folderStructure">
                <form>
                    <label for="fileInput">
                        Upload File or Folder
                    </label>
                    <input class="fileUploadInput" type="file" id="fileInput" style="display: none" on:change={uploadFile} />
                </form>
               </div>
            </div>
        </div>
        <div class="editorContainer">
        <div class="editorTabs">
            {#each $openedFiles as file, index}
            <div class="tab {activeTabIndex === index ? 'active' : ''}" on:click={() => setActiveTabIndex(index)} on:keydown={(event) => handleKeyDown(event, index)} >
            {file.filename}
            <span class="close" 
            on:click={(event) => closeFile(event, index)} 
            on:keydown={(event) => handleKeyDown(event, index)}
            >×</span>
            </div>
            {/each}
        </div>
        
            {#each $openedFiles as file, index}
                {#if activeTabIndex === index}
                    <Editor fileContent={file.content} />
                {/if}
            {/each}
        </div>
    </div>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        width: 90vw;
        background-color: #f2f2f2;
        color: black;
        border: #0C0C0C 1px solid;
        border-radius: 10px;
        padding: 1%;
    }
    .mainContainer {
        display: flex;
        width: 100%;
        height: 100%;
        padding: 2%;
        gap: 2%;
    }
    .fileUploadContainer {
        height: 100%;
        width: 15vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        gap: 5em;
        border: 1px solid #0C0C0C;
        border-radius: 10px;
        padding: 0.5%;
    }
    .fileUpload {
        border: 1px solid #0C0C0C;
        border-radius: 10px;
        width: 70%;
        height: 5%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .fileUploadButtons > button {
        padding: 0.5rem 1rem;
        background-color: #0C0C0C;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .editorTabs {
        display: flex;
        gap: 5px;
        padding-bottom: 5px;
        border-bottom: 1px solid #ccc;
        margin-bottom: 1em;
    }
    .tab {
        padding: 8px 12px;
        background-color: #f2f2f2;
        color: #333;
        border: 1px solid #ccc;
        border-bottom: none;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        position: relative;
    }
    .tab.active {
        background-color: #fff;
        border-bottom: 1px solid #fff;
    }
    .tab:hover {
        background-color: #eaeaea;
    }
    .close {
        font-size: 14px;
        margin-left: 5px;
        cursor: pointer;
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        right: 8px;
    }
    .editorContainer {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        width: 100%;
    }
</style>
