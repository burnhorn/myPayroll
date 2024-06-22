<script>
    import { deleteQuestion } from '../../lib/fetch.js'; // named import 사용
    import { push } from 'svelte-spa-router'

    export let question_id // 부모 question page에서 값 받기

    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
    async function loadDeleteQuestion(event) {
        event.preventDefault();
      try {
        await deleteQuestion(question_id);
        console.log("삭제 요청했습니다:");
        push('/');
      } catch (error) {
        console.error('삭제 중 오류가 발생했습니다:', error);
      }
    }

</script>

    <form class="my-3" on:submit={loadDeleteQuestion}>
        <button type="submit" class="btn btn-primary">삭제하기</button>
    </form>

<style>

    .my-3 {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .btn-primary {
        color: #fff;
        background-color: #007bff;
        border-color: #007bff;
    }

    .btn-primary:hover {
        color: #fff;
        background-color: #0056b3;
        border-color: #004085;
    }
</style>