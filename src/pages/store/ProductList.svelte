<script>
    import ProductCard from "./ProductCard.svelte";

    export let pageNumber = 0;

    let products = [
        { id: 0, productName: "BEER", productImage: "", authorName: "Pedro", price: 75.7},
        { id: 1, productName: "VODKA", productImage: "", authorName: "Pedro", price: 34.2},
        { id: 2, productName: "GAYBOY", productImage: "", authorName: "Roma", price: 332.99},
        { id: 3, productName: "ILIYA", productImage: "", authorName: "Roma", price: 0.02},
        { id: 4, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 5, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 6, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 7, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 1, productName: "VODKA", productImage: "", authorName: "Pedro", price: 34.2},
        { id: 2, productName: "GAYBOY", productImage: "", authorName: "Roma", price: 332.99},
        { id: 3, productName: "ILIYA", productImage: "", authorName: "Roma", price: 0.02},
        { id: 4, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 5, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 6, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},  
        { id: 7, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 1, productName: "VODKA", productImage: "", authorName: "Pedro", price: 34.2},
        { id: 2, productName: "GAYBOY", productImage: "", authorName: "Roma", price: 332.99},
        { id: 3, productName: "ILIYA", productImage: "", authorName: "Roma", price: 0.02},
        { id: 4, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 5, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 6, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 7, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 1, productName: "VODKA", productImage: "", authorName: "Pedro", price: 34.2},
        { id: 2, productName: "GAYBOY", productImage: "", authorName: "Roma", price: 332.99},
        { id: 3, productName: "ILIYA", productImage: "", authorName: "Roma", price: 0.02},
        { id: 4, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 5, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 6, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 7, productName: "ABODBUHOV", productImage: "", authorName: "Roma", price: 0.13},
        { id: 1, productName: "VODKA", productImage: "", authorName: "Pedro", price: 34.2},
        { id: 2, productName: "GAYBOY", productImage: "", authorName: "Roma", price: 332.99},
        { id: 3, productName: "ILIYA", productImage: "", authorName: "Roma", price: 0.02},
    ];
</script>


<div class="product-list">
    {#each products as { id, productName, productImage, authorName, price }}
        <ProductCard {id} {productName} {productImage} {authorName} {price}/>
    {/each}
</div>


<style>
    .product-list {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
    }
</style>