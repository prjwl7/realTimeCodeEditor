<script>
    import Editor from '../editor/+page.svelte';
    import { writable } from 'svelte/store';
    export const responseStore = writable('');

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
                const responseBody = await response.text();
                responseStore.set(responseBody);
            } else {
                console.log('Failed to upload file');
            }
        } catch (error) {
            console.error('An error occurred while uploading the file:', error);
        }
    }
</script>

<main>
    <div class="mainContainer">
        <div class="fileUploadContainer">
            <div class="fileUploadButtons">
                <button >New File</button>
                <button >New Folder</button>
            </div>
            <div class="fileUpload">
               <div class="folderStructure">
                <form >
                    <label for="fileInput">
                        Upload File or Folder
                    </label>
                    <input class="fileUploadInput" type="file" id="fileInput" style="display: none" on:change={uploadFile} />
                </form>
               </div>
            </div>
        </div>
        <Editor />
    </div>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
        background-color: #f2f2f2;
        color: black;
        border: #0C0C0C 1px solid;
        border-radius: 10px;
        padding-top: 1%;
    }
    .mainContainer{
        display: flex;
        width: 100%;
    }
    .fileUploadContainer{
        height: 100%;
        width: 15vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        gap: 5em;
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
</style>
