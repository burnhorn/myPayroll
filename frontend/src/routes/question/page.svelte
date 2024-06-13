<script>
    import { getQuestionDetail } from '../../lib/fetch.js'; // named import 사용
  
    export let params = {};
    let question_id = params.question_id;
    let question_detail = {};

    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
    async function loadQuestionDetail() {
      try {
        question_detail = await getQuestionDetail(question_id);
        console.log("데이터를 성공적으로 불러왔습니다:", question_detail);
      } catch (error) {
        console.error('질문 목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }
  
    // 컴포넌트가 마운트될 때 loadQuestionDetail 함수 호출
    loadQuestionDetail();

  </script>
  
  <h1>{question_detail.title}</h1>
  <div>
      {question_detail.content}
  </div>
  