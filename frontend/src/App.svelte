<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/home/page.svelte"
    import Question from "./routes/question/page.svelte"
    import Insurance from "./routes/insurance/page.svelte"
    import InsuranceCal from "./routes/insurance/cal_page.svelte" 
    import User from "./routes/user/page.svelte" 
    import DashBoard from "./routes/dashboard/page.svelte" 
    import QuestionCreate from "./routes/create/question-create.svelte"

    import Layout from './components/Layout.svelte'

    const routes = {
        '/': Home,
        '/question/:question_id' : Question,
        '/insurance/calculate' : InsuranceCal,
        '/insurance/:rate_id' : Insurance,
        '/user_login' : User,
        '/dashboard' : DashBoard,
        '/question-create' : QuestionCreate,
    }
</script>

<Layout>
    <Router {routes} />
</Layout>