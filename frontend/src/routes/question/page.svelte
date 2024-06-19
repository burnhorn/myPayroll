<script>
    import { getQuestionDetail } from '../../lib/fetch.js'; // named import 사용
    import AnswerCreate from "../../routes/create/answer-create.svelte";

    export let params = {};
    let question_id = params.question_id;
    let question_detail = {};

    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
    async function loadQuestionDetail() {
      try {
        question_detail = await getQuestionDetail(question_id);
        console.log("svelte 내에서 데이터를 성공적으로 불러왔습니다:", question_detail);
      } catch (error) {
        console.error('질문 목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }
  
    // 컴포넌트가 마운트될 때 loadQuestionDetail 함수 호출
    loadQuestionDetail();

</script>
  
 <h1>질문 : {question_detail.title}</h1>
  <div class = "question-details">
    <div class = "question-content">
    질문 내용 : {question_detail.content} <br>
    질문 작성일 : {question_detail.create_date}
  </div>
  <!--답변 내용 (question 안의 answer, user 객체를 모두 반복해야 오류가 나지 않는다) -->
  <div class = "answers-list">  
    {#if question_detail.answers && question_detail.answers.length >0}
        <ul>
          {#each question_detail.answers as answer}
          <li class = "answer-item">
            <div class= "answer-content">
            <p>답변 내용 : {answer.content}</p>
            <p>답변 작성일시 : {answer.create_date}</p>
            </div>
            {#if answer.answer_user}
            <div class="answer-user">
              <p>답변자 : {answer.answer_user.user_name}</p>
            </div> 
            {/if}  
          </li>
          {/each}
        </ul>
      {/if} 
  </div> 
  <AnswerCreate {question_id}  /> <!-- 자식 컴포넌트 AnswerCreate로 quesiton_id 값 전달하기-->
  </div> 
  

<style>
 
  h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .question-details {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
  }
  
  .question-content {
    margin-bottom: 20px;
    padding: 10px;
    border-bottom: 3px solid #666;
  }
  
  /* Answers styles */
  .answers-list {
    margin-top: 20px;
  }
  
  .answer-item {
    margin-bottom: 15px;
    border-bottom: 1px solid #eee;
    padding-bottom: 10px;
  }
  
  .answer-content {
    margin-bottom: 5px;
  }
  
  .answer-user {
    font-style: italic;
    color: #666;
  }

</style>