<script>
    import { getQuestionList } from '../../lib/fetch.js'; // named import 사용
    import { link } from 'svelte-spa-router'
    import { writable } from 'svelte/store';
    import moment from 'moment/min/moment-with-locales' // 날짜 표시 포멧 변환
  
    moment.locale('ko')
  
    let question_list = [];
    let question_listAndpage = [];
    let size = 10
    let question_page_total = 0
    $: web_total_page = Math.ceil(question_page_total/size)
  
    let currentPage = writable(0); // 초기값 0, loadQuestions에 의해서 업데이트
  
    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용(페이지 버튼 누를 때마다 호출)
    async function loadQuestions(_page) {
      try {
        question_listAndpage = await getQuestionList(_page, size);
        question_list = question_listAndpage.question_list
        question_page_total = question_listAndpage.question_total
        currentPage.set(_page);  // 현재 페이지 업데이트(페이지 버튼 누를 때마다 호출)
      } catch (error) {
        console.error('질문 목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }
  
    // 컴포넌트가 마운트될 때 loadQuestions 함수 호출
    loadQuestions(0);
  </script>
  
  <div class="question-container">
    <div class="header">
      <span class="header-item">번호</span>
      <span class="header-item">게시물 제목</span>
      <span class="header-item">작성일</span>
      <span class="header-item">작성자</span>
    </div>
    {#each question_list as question, i}
    <div class="question-row">
      <span class="row-item">{i + 1}</span>
      <span class="row-item"><a use:link href="/question/{question.id}">{question.title}</a></span>
      <span class="row-item">{moment(question.create_date).format("YYYY년 MM월 DD일 a hh:mm")}</span>
      {#if question.user_name}
      <span class="row-item">{question.user_name}</span>
      {:else}
      <span class="row-item">Null</span>
      {/if}
    </div>
    {/each}
    <div class="pagination-container">
      <ul class="pagination">
        {#each Array(web_total_page) as _, pageNum} <!--현재 페이지 값이 인자로 전달-->
          <li class="page-item { $currentPage === pageNum ? 'active' : '' }">
            <button on:click={() => loadQuestions(pageNum)} class="page-link">{pageNum + 1}</button>
          </li>
        {/each}
      </ul>
    </div>
  </div>
  
  <div class="button-container">
    <a use:link href="/question-create" class="btn">질문 등록하기</a>
  </div>
  
  <style>
  
    .question-container {
      display: flex;
      flex-direction: column;
      margin: 20px;
    }
  
    .header, .question-row {
      background-color: #fff;
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid #ddd;
    }
  
    .header {
      font-weight: bold;
    }
  
    .header-item, .row-item {
      flex: 1;
      text-align: center;
    }
  
    .row-item a {
      text-decoration: none;
      color: #007BFF;
    }
  
    .row-item a:hover {
      text-decoration: underline;
    }
    .pagination-container {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }
  
    .pagination {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(40px, 1fr)); /* 반응형 그리드 설정 */
      gap: 10px;
      list-style-type: none;
      padding: 0;
      width: 100%; /* 컨테이너 너비에 맞춤 */
      max-width: 1000px; /* 최대 너비 설정 (필요에 따라 조정 가능) */
    }
  
    .page-item {
      margin: 0 5px;
    }
  
    .page-item.active button {
      background-color: #007bff;
      color: white;
    }
  
    .page-link {
      border: 1px solid #dee2e6;
      padding: 5px 10px;
      background-color: white;
      color: #007bff;
      cursor: pointer;
    }
  
    .page-link:hover, .page-item.active .page-link {
      background-color: #007bff;
      color: white;
    }
    
    .button-container {
      display: flex;
      justify-content: flex-end;
    }
    
    .btn {
      display: inline-block;
      padding: 5px 10px;
      background-color: #000000;
      color: white;
      border: none;
      border-radius: 5px;
      text-align: center;
      text-decoration: none;
      cursor: pointer;
      font-size: 16px;
      margin: 20px 0;
    }
  
    .btn:hover {
      background-color: #0056b3;
    }
  </style>