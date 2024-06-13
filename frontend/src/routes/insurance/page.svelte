<script>
    import { getInsuranceRate } from '../../lib/fetch.js'; // named import 사용
  
    export let params = {};
    let rate_id = params.rate_id;
    let rate_list = {}
    
    // 페이지가 로드될 때 데이터를 가져오기 위해 비동기 함수 사용
    async function loadInsuranceRate() {
      try {
        rate_list = await getInsuranceRate(rate_id);
      } catch (error) {
        console.error('보험요율 목록을 불러오는 중 오류가 발생했습니다:', error);
      }
    }
  
    // 컴포넌트가 마운트될 때 loadInsuranceRate 함수 호출
    loadInsuranceRate();

</script>
  
<ul>
    <li>국민연금 요율 : {rate_list.national_pension}</li>
    <li>건강보험 요율 : {rate_list.health_insurance}</li>
    <li>장기요양보험 요율 : {rate_list.medical_insurance}</li>
    <li>고용보험 요율 : {rate_list.employment_insurance}</li>
</ul>
  