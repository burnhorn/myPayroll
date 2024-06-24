<script>
	let main_subject = {
		id: 'HR Data Analysis',
		name:'HR Analysis with Excel',
		images:[
			'https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/basic.PNG',
			'https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/branch.PNG',
			'https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/department.PNG',
            'https://github.com/burnhorn/myPayroll/raw/main/frontend/src/assets/image/position.PNG',
		],
	};

    let contentSections = [
    { title: '1. Issue'},
    { title: '2. Approach Method'},
    { title: '3. Skills'},
    { title: '4. Result'},
  ]

	let sliderCenterIndex = 0;
	let sliderLeftIndex = main_subject.images.length -1;
	let sliderRightIndex = 1;

	function sliderMoveLeft() {
		const length = main_subject.images.length;
		sliderCenterIndex = (sliderCenterIndex - 1 + length) % length;
		sliderLeftIndex = (sliderCenterIndex - 1 + length) % length;
		sliderRightIndex = (sliderCenterIndex + 1) % length;
	}

	function sliderMoveRight(){
		const length = main_subject.images.length;
		sliderCenterIndex = (sliderCenterIndex + 1) % length;
		sliderLeftIndex = (sliderCenterIndex -1 + length) % length;
		sliderRightIndex = (sliderCenterIndex + 1) % length;
	}
	
</script>

<header class = "header">
	<h1 class ="header-title">HR Data Analysis with Excel</h1>
    <h4 class ="header-subtitle">**Notice | The dashboard utilized dummy data</h4>
</header>


<article class = "product">
	<div class="product_main">
		<div class ="image-container">
			<div class = "slider">
				<img src = {main_subject.images[sliderLeftIndex]} alt="sliderImage(left)" class="slider-item left" />
				<img src = {main_subject.images[sliderCenterIndex]} alt="sliderImage" class="slider-item" />
				<img src = {main_subject.images[sliderRightIndex]} alt="sliderImage(right)" class="slider-item right" />
				<button class="slider-left-button" on:click={sliderMoveLeft}>←</button>
				<button class="slider-right-button" on:click={sliderMoveRight}>→</button>
			</div>
		</div>

		<div class="topic-container">
            <h2 class="topic-title">Index</h2>
            <ul class="topic-list"> 
                <li class="topic-item">1. Issue</li>
                <li class="topic-item">2. Approach Method</li>
                <li class="topic-item">3. Skills</li>
                <li class="topic-item">4. Result</li>
            </ul>
		</div>
        <div class="content-container">
            <section id="1. Issue" class="content-section">
                <h3>1. Issue</h3>
                <div class="content-body">
                    <ul>
                        <li>
                            <strong>인적 자원 관리 및 분석 필요성</strong> : 분산된 계열사 HR 데이터를 체계적으로 통합하고 분석할 필요가 있었습니다.
                        </li>
                        <li>
                            <strong>데이터 기반 경영 인사이트 도출</strong> : 데이터 분석을 통해 경영에 유용한 인사이트를 도출해야 했습니다.
                        </li>
                    </ul>
                </div>
            </section>
            
            <section id="2. Approach Method" class="content-section">
                <h3>2. Approach Method</h3>
                <div class="content-body">
                    <ul>
                        <li>
                            <strong>데이터 통합</strong>: Pandas를 사용하여 파편화된 계열사 HR 데이터를 통합했습니다.
                        </li>
                        <li>
                            <strong>데이터 시각화</strong>: Excel을 활용하여 데이터를 시각적으로 효과적으로 표현했습니다.
                        </li>
                    </ul>
                </div>
            </section>

            <seciton id="3. Skills" class="content-section">
                <h3>3. Skills</h3>
                <div class="content-body">
                    <ul>
                        <li>
                            <strong>사용 기술 및 도구</strong>: Excel, Pandas, FastAPI, Svelte
                        </li>
                        <li>
                            <strong>도입 배경</strong>:
                            <ul>
                                <li>
                                    <strong>시간 효율성</strong>: 빠른 개발과 낮은 러닝 커브를 가진 도구를 선택했습니다.
                                </li>
                                <li>
                                    <strong>접근성</strong>: FastAPI와 Svelte를 사용하여 신속하게 웹 애플리케이션을 구축하고, 의사결정자들이 프로토타입 데이터를 쉽게 접근할 수 있도록 했습니다.
                                </li>
                                <li>
                                    <strong>데이터 처리</strong>: Pandas를 활용하여 파편화된 데이터를 효율적으로 정리했습니다.
                                </li>
                                <li>
                                    <strong>보안 및 사용성</strong>: 최종 결과물은 보안과 사용성을 고려하여 Excel로 완성했습니다.
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </seciton>

            <seciton id="4. Result" class="content-section">
                <h3>4. Result</h3>
                <div class="content-body">
                    <ul>
                        <li>
                            <strong>회사 차원의 성과</strong>:
                            <ul>
                                <li>
                                    <strong>빠른 데이터 이해</strong>: 의사결정자들이 다양한 시각적 요소를 통해 데이터를 신속하게 파악하고, 전략적 의사결정을 내릴 수 있었습니다. 
                                </li>
                                <li>
                                    <strong>효과적인 데이터 제시</strong>: 반응형 시각화를 통해 의사결정자들이 필요한 정보를 손쉽게 선택하고 접근할 수 있었습니다.
                                </li>
                            </ul>
                        </li>
                        <li>
                            <strong>개인적인 성과</strong>:
                            <ul>
                                <li>
                                    <strong>데이터 분석 역량 향상</strong>: Excel의 피벗 테이블과 슬라이서를 활용하여 반응형 대시보드를 개발함으로써 대량의 인적 데이터를 효율적으로 관리하고 보고하는 능력을 키웠습니다. 이를 통해 파편화된 데이터를 통합 관리하는 것의 중요성을 깨닫고, Python과 Pandas를 사용한 데이터 분석 역량을 강화했습니다.
                                </li>
                                <li>
                                    <strong>데이터 시각화 인사이트</strong>: 데이터의 유기적 관계를 이해하고, 정보를 결합하여 경영 관리자에게 유의미한 인사이트를 제공할 수 있는 방법을 배웠습니다. 이를 통해 경영에 실질적으로 도움이 되는 데이터를 제공할 수 있게 되었습니다.
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </seciton>
        </div>
	</div>
			<footer>
				<h2>Skills</h2>
				<ul>
                    <li class="skill-image">
                      <img src= "https://upload.wikimedia.org/wikipedia/commons/7/73/Microsoft_Excel_2013-2019_logo.svg" alt="excelImage" class="excel-icon" />
                      <img src= "https://pandas.pydata.org/static/img/pandas.svg" alt="pandasImage" class="pandas-icon" />
                      <img src= "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="fastapiImage" class="fastapi-icon" />
                      <img src= "https://github.com/sveltejs/svelte/raw/main/sites/svelte.dev/static/svelte-logo.svg" alt="svelteImage" class="svelte-icon" />
                    </li>
				</ul>
		</footer>
</article>

<style>
	:global(body) {
		margin:0;
		background-color : #eee;
		padding: 0;
	}

	.header {
		display:flex;        
        justify-content: space-between;
		align-items:center;
		margin:0 auto;
		background-color : #fff;
		padding : 0 15px;
		width: 100%;
		max-width: auto;
		height: 50px;
	}

	.header-title{
        font-weight: bold;
        text-align: center;
        width: 80%;
    }

    .header-subtitle{
		font-weight: bold;
        color: red; 
        text-decoration: underline;
        text-align: end;
	}

	.product{
		margin:0 auto;
		background-color: #fff;
		padding: 15px;
		width: 100%;
		max-width: auto;
	}

	.image-container {
		width: auto;
		max-width: auto;
		overflow: hidden;
	}

	.image-container img {
		width: 100%;
	}

	.slider {
		position: relative;
		width: 80%;
		margin: 0 10%;
	}

	.slider-item {
		width: 100%
	}

	.slider-item.left {
		position: absolute;
		top: 0;
		right: 100%
	}
	
	.slider-item.right {
		position: absolute;
		top: 0;
		left: 100%
	}

	.slider-left-button {
		position: absolute;
		top: 50%;
		right: 100%;
        width: 40px; 
        height: 40px; 
	}

	.slider-right-button {
		position: absolute;
		top: 50%;
		left: 100%;
        width: 40px; 
        height: 40px; 
	}

    .topic-container {
        width: 300px; /* Adjust width as needed */
        margin: 15px auto; /* Center the TOC container */
        padding: 20px;
        border: 1px solid #ccc; /* Add a subtle border */
        background-color: #f5f5f5; /* Light background for contrast */
    }

    .topic-title {
        text-align: center;
        margin-bottom: 15px;
    }

    .topic-list {
        list-style: none; /* Remove default list bullets */
        padding: 0;
    }

    .topic-item {
       margin-bottom: 10px;
    }

    .content-container {
        margin-top: 30px; /* Add spacing between TOC and content */
        border-bottom: 1px solid #ddd;
    }

    .content-section {
        margin-bottom: 20px;
    }

    .content-body {
        padding: 15px;
        border: 1px solid #ccc;
        background-color: #fff;
    }

    .skill-image {
        list-style-type: none;  /* Remove bullet points */
    }

    .excel-icon {
        width: 40px; 
        height: auto; 
        margin: 0 30px; 
        border: none; 
        display: inline-block; 
    }

    .pandas-icon {
        width: 110px; /* Adjust width for Pandas icon */
        height: auto; /* Maintain aspect ratio */
        margin: 0; /* Add spacing */
        border: none; /* Remove default border */
        display: inline-block; /* Display inline */
    }

    .fastapi-icon {
        width: 120px; 
        height: auto; 
        margin: 0 10px;
        border: none; 
        display: inline-block; 
    }
    
    .svelte-icon {
        width: 30px; 
        height: auto; 
        margin: 0;
        border: none; 
        display: inline-block; 
        padding-bottom: 5px; /* Add padding below the icon */
    }
</style>
