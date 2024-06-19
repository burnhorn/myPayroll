<script>
    import { postQuestion } from '../../lib/fetch.js'; // named import 사용
    import { push } from 'svelte-spa-router'

    let params = {
        title : "",
        content : "",
    };
    let question_detail = {};

    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
    async function loadPostQuestion(event) {
        event.preventDefault();
      try {
        question_detail = await postQuestion(params);
        console.log("svelte 내에서 데이터를 성공적으로 불러왔습니다:", question_detail);
        push('/');
      } catch (error) {
        console.error('질문 목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }

</script>





<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 등록</h5>
    <form class="my-3" on:submit={loadPostQuestion}>
        <div class="mb-3">
            <label for="title">제목</label>
            <input type="text" id="title" class="form-control" bind:value={params.title}>
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea id="content" class="form-control" rows="10" bind:value={params.content}></textarea>
        </div>
        <button type="submit" class="btn btn-primary">저장하기</button>
    </form>
</div>

<style>
    .container {
        max-width: 600px;
        margin: 0 auto;
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