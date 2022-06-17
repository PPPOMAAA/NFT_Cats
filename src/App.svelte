<script>
    import { Router, Route } from "svelte-routing";
    import StorePage from "./pages/store/StorePage.svelte";
    import Header from "./components/Header.svelte";
    import Footer from "./components/Footer.svelte";
</script>


<Router>
    <Header/>
    <main>
        <Route path="/">
            <StorePage/>
        </Route>
        <Route path="/profile">
            <StorePage/>
        </Route>
    </main>
    <Footer/>
</Router>


<style>
    main {
        max-width: 1280px;
        margin: 0 auto;
    }
</style>