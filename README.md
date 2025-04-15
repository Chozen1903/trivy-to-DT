# trivy-to-DT

## 환경세팅
### trivy 설치방법
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

### DT 사용
curl -LO https://dependencytrack.org/docker-compose.yml
sudo docker compose up -d

