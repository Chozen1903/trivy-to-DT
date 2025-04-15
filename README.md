# trivy-to-DT

## 환경세팅
### trivy 설치방법
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

### DT 사용
curl -LO https://dependencytrack.org/docker-compose.yml

sudo docker compose up -d

### API 생성
http://localhost:8080 접속후 초기 아이디인 admin / admin 으로 접속 (첫 접속 시 비번변경)

경로 : Dashbboard -> Administration -> Access Management -> team -> Automation

첫 생성시 업로드 권한이 모자라므로 API_KEY 생성 아래에 Permmisions 에서 PORTFOLIO_MANAGEMENT 권한 추가

## 기능
1. trivy 를 통해 sbom.json 파일생성
2. json 파일생성이 성공했다면 그 파일을 DT에 업로드 (프로젝트 없을 시 자동 생성후 업로드)
