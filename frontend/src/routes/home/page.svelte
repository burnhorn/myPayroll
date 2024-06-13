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

<ul>
  {#each question_list as question}
  <li><a use:link href="/question/{question.id}">{question.title}</a></li>
  {/each}
</ul>
