<script>
  import { getQuestionList } from '../../lib/fetch.js'; // named import 사용
  import { link } from 'svelte-spa-router'

  let question_list = [];
  
  // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
  async function loadQuestions() {
    try {
      question_list = await getQuestionList();
    } catch (error) {
      console.error('질문 목록을 불러오는 중 오류가 발생했습니다:', error);
    }
  }

  // 컴포넌트가 마운트될 때 loadQuestions 함수 호출
  loadQuestions();
</script>

<div>
  <ul>
    {#each question_list as question, i}
    <li><a use:link href="/question/{question.id}">{question.title}</a></li>
    {/each}
  </ul>
</div>

<a use:link href="/question-create" class="btn">질문 등록하기</a>


<style>
  li {
    list-style:none;
  }

  .btn {
    display: inline-block;
    padding: 5px 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    font-size: 16px;
  }

  .btn:hover {
    background-color: #0056b3;
  }

</style>
