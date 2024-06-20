<script>
    import { postAnswer } from '../../lib/fetch.js'; // named import 사용
    import { createEventDispatcher } from 'svelte';

    export let question_id // 부모 question page에서 값 받기

    let answer_params = {
        content : "",
    };
    let answer_detail = {};

    // Create an event dispatcher
    const dispatch = createEventDispatcher();

    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
    async function loadPostAnswer(event) {
        event.preventDefault();
      try {
        answer_detail = await postAnswer(question_id, answer_params);
        console.log("svelte 내에서 데이터를 성공적으로 불러왔습니다:", answer_detail);
        // Dispatch a custom event to notify the parent component
        dispatch('answerPostSuccess');
      } catch (error) {
        console.error('답변 데이터를 불러오는 중 오류가 발생했습니다:', error);
      }
    }

</script>





<div class="container">
    <h5 class="my-3 border-bottom pb-2">답변 등록</h5>
    <form class="my-3" on:submit={loadPostAnswer}>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea id="content" class="form-control" rows="10" bind:value={answer_params.content}></textarea>
        </div>
        <button type="submit" class="btn btn-primary">저장하기</button>
    </form>
</div>

<style>
    .container {
        max-width: 600px;
        margin: 0;
    }

    .border-bottom {
        border-bottom: 1px solid #dee2e6;
    }

    .pb-2 {
        padding-bottom: .5rem;
    }

    .my-3 {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .form-control {
        width: 100%;
        padding: .375rem .75rem;
        font-size: 1rem;
        line-height: 1.5;
        color: #495057;
        background-color: #fff;
        background-clip: padding-box;
        border: 1px solid #ced4da;
        border-radius: .25rem;
        transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
        margin-left: 0;
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