<script>

</script>


<footer>
    <div class="container">
        <div class="block">
            <div class="title">Creators:</div>
            <div class="subblock">
                <div class="subtitle">Frontend:</div>
                <p>Рудых Роман</p>
                <p>Тильт Николай</p>
            </div>
            <div class="subblock">
                <div class="subtitle">Backend:</div>
                <p>Обухов Илья</p>
            </div>
        </div>
        <div class="block">
            <div class="title">Stack:</div>
            <div class="subblock">
                <div class="subtitle">Frontend:</div>
                <p>Svelte</p>
                <p>SCSS</p>
            </div>
            <div class="subblock">
                <div class="subtitle">Backend:</div>
                <p>Flask</p>
                <p>MySQL</p>
                <p>Web3</p>
            </div>
        </div>
    </div>
</footer>


<style>
    footer {
        border-top: 1px solid var(--color-neutral-2);
        /* background-color: var(--color-neutral-5); */
    }

    .container {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        max-width: 1280px;
        margin: 0 auto;
        padding: 30px 0px 20px 0px;
    }

    .block {
        display: flex;
        flex-direction: column;
    }

    .subblock {
        padding-bottom: 12px;
    }

    .title {
        color: var(--color-neutral-3);
        font-size: 16px;
        font-weight: 600;
        padding-bottom: 14px;
    }
    
    .subtitle {
        color: var(--color-neutral-3);
        font-size: 14px;
        font-weight: 500;
        padding-bottom: 6px;
    }
    
    p {
        color: var(--color-neutral-3);
        font-size: 13px;
        font-weight: 400;
        padding-bottom: 2px;
    }
</style>