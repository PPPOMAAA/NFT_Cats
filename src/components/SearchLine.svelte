<script>
    let searchString = "";
</script>


<input type="search" placeholder="Search" bind:value={searchString}>


<style>
    input {
        width: 256px;
        font-size: 12px;
        padding: 10px 18px;
        border: 2px solid var(--color-neutral-2);
        border-radius: 8px;
        margin-right: 30px;
    }
    
    input:focus {
        border: 2px solid var(--color-primary);
    }
</style>