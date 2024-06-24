<script>
    import { getInsuranceCal } from '../../lib/fetch.js'; // named import 사용
  
    let salary = '';
    let salary_cal = {
        national_pension: 0,
        health_insurance: 0,
        medical_insurance: 0,
        employment_insurance: 0
    };
  
    async function loadInsuranceCal(event) {
        event.preventDefault(); // 폼 제출 기본 동작 방지
      try {
        salary_cal = await getInsuranceCal(salary);
        console.log('Fetched salary calculation data:', salary_cal);
      } catch (error) {
        console.error('보험 요율 계산 중 오류가 발생했습니다:', error);
      }
    }

</script>

<form method="post" class="form-container" on:submit={loadInsuranceCal}>
    <div class="form-group">
        <label for="salary">월 급여</label>
        <input type="number" class="form-control" bind:value={salary} id="salary">
    </div>
    <button class="btn" type="submit">계산하기</button>
</form>


{#if salary_cal}
  <div class="results-container">
    <ul>
      <li><strong>국민연금:</strong> {salary_cal.national_pension} 원</li>
      <li><strong>건강보험료 :</strong> {salary_cal.health_insurance} 원</li>
      <li><strong>장기요양료:</strong> {salary_cal.medical_insurance} 원</li>
      <li><strong>고용보험료:</strong> {salary_cal.employment_insurance} 원</li>
    </ul>
  </div>
{/if}

<style>
  .form-container {
    display: flex;
    flex-direction: column;
    align-items: center; /* 중앙 정렬 */
  }

  .form-group {
    display: flex;
    align-items: center; /* 수직 가운데 정렬 */
    justify-content: center; /* 수평 가운데 정렬 */
    width: 100%;
    max-width: 500px; /* 최대 너비 설정 */
    margin-bottom: 1rem;
  }

  .form-group label {
    margin-right: 1rem; /* 레이블과 입력 필드 사이의 간격 */
    white-space: nowrap; /* 텍스트 줄바꿈 방지 */
  }

  .form-control {
    flex: 1; /* 입력 필드가 남은 공간을 차지하게 함 */
    padding: 0.5rem;
    font-size: 1rem;
  }

  .btn {
    background-color: #999898;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 0.25rem;
    cursor: pointer;
    font-size: 1rem;
  }
  .btn:hover {
    background-color: #000000;
  }
  .results-container {
    margin-top: 2rem;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 0.25rem;
    background-color: #f9f9f9;
    max-width: 300px; /* 크기 조절 */
    margin-left: auto;
    margin-right: auto;
  }

  .results-container ul {
    list-style-type: none;
    padding: 0;
  }
  .results-container ul li {
    margin-bottom: 0.5rem;
    border-bottom: 1px solid #ddd; /* 아래쪽 선 추가 */
    font-size: 1.1rem;
  }
  .results-container ul li strong {
    margin-right: 0.5rem;
  }
</style>