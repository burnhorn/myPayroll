<script>
    import Router from 'svelte-spa-router'
    import Home from "./routes/home/page.svelte"
    import Question from "./routes/question/page.svelte"
    import Insurance from "./routes/insurance/page.svelte"
    import InsuranceCal from "./routes/insurance/cal_page.svelte" 
    import Login from "./routes/user/login.svelte" 
    import SignUp from "./routes/user/signUp.svelte" 
    import DashBoard from "./routes/dashboard/page.svelte" 
    import QuestionCreate from "./routes/create/question-create.svelte"
    import AnswerCreate from "./routes/create/answer-create.svelte"
    import UpdateQuestion from "./routes/question/update-question.svelte"
    import Layout from './components/Layout.svelte'
    import Board from "./routes/board/qna.svelte"

    const routes = {
        '/': Home,
        '/qna': Board,
        '/question/:question_id' : Question,
        '/insurance/calculate' : InsuranceCal,
        '/insurance/:rate_id' : Insurance,
        '/user-login' : Login,
        '/user-singup' : SignUp,
        '/dashboard' : DashBoard,
        '/question-create' : QuestionCreate,
        '/answer-create' : AnswerCreate,
        '/update-question/:question_id' : UpdateQuestion,
    }

</script>

<Layout>
    <Router {routes} />
</Layout>