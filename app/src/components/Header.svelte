<script>
    import { Link } from "svelte-routing";
    import Button from "./Button.svelte";
    import SearchLine from "./SearchLine.svelte";
</script>


<header>
    <div class="container">
        <Link to="/">
            <div class="logo">NFT cats</div>
        </Link>
        <div class="right">
            <SearchLine/>
            <Link>
                <Button type="accent" size="medium" text="Upload"/>
            </Link>
            <Link>
                <Button type="light" size="medium" text="Account"/>
            </Link>
        </div>
    </div>
</header>


<style> 
    header {
        border-bottom: 1px solid var(--color-neutral-2);
    }

    .container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        max-width: 1280px;
        margin: 0 auto;
        padding: 14px 0px;
    }
    
    .right {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 16px;
    }
    
    .logo {
        justify-self: flex-start;
        font-size: 28px;
        font-weight: 700;
        color: var(--color-neutral-6);
    }
</style>