<script>
    import { getQuestionDetail, updateQuestion } from '../../lib/fetch.js'; // named import 사용
    import { push } from 'svelte-spa-router'

    export let params = {};
    let question_id = params.question_id;
    let question_detail = {};

    async function loadQuestionDetail() {
      try {
        question_detail = await getQuestionDetail(question_id);
        console.log("svelte 내에서 데이터를 성공적으로 불러왔습니다:", question_detail);
      } catch (error) {
        console.error('목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }

    async function loadUpdateQuestion(event) {
      event.preventDefault()

      let update_detail = []
      let update_detail_parmas = {
        "title" : question_detail.title,
        "content" :  question_detail.content
      }
      try {
        update_detail = await updateQuestion(question_id, update_detail_parmas);
        console.log("svelte 내에서 데이터를 성공적으로 불러왔습니다:", update_detail);
        push(`/question/${question_id}`);
      } catch (error) {
        console.error('질문 목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }
  
    // 컴포넌트가 마운트될 때 loadQuestionDetail 함수 호출
    loadQuestionDetail();
</script>
  

<div class="container">
    <h5 class="my-3 border-bottom pb-2">질문 수정</h5>
    <form class="my-3" on:submit={loadUpdateQuestion}>
        <div class="mb-3">
            <label for="title">제목</label>
            <input type="text" id="title" class="form-control" bind:value={question_detail.title}>
        </div>
        <div class="mb-3">
            <label for="content">내용</label>
            <textarea id="content" class="form-control" rows="10" bind:value={question_detail.content}></textarea>
        </div>
        <button type="submit" class="btn btn-primary">수정하기</button>
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