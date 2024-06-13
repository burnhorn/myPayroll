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

<form method="post" class="my-1" on:submit={loadInsuranceCal}>
    <div class="mb-3">
        <label for="salary">급여 입력</label>
        <input type="number" class="form-control" bind:value={salary} id="salary">
    </div>
    <button class="btn" type="submit">보험료 계산</button>
</form>


<ul>
{#if salary_cal}
    <li>국민연금 : {salary_cal.national_pension}</li>
    <li>건강보험료 : {salary_cal.health_insurance}</li>
    <li>장기요양료 : {salary_cal.medical_insurance}</li>
    <li>고용보험료 : {salary_cal.employment_insurance}</li>
{/if}
</ul>
  