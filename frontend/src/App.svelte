<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/home/page.svelte"
    import Question from "./routes/question/page.svelte"
    const routes = {
        '/': Home,
        '/question/:question_id' : Question
    }
</script>

<Router {routes} />