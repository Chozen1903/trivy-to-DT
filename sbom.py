import subprocess
import requests

# --- 설정값 ---
project_name = "nginx"
project_version = "latest"
api_key = <API_KEY>  # <API_KEY>에 본인의 API 키를 넣으세요
dtrack_url = "http://localhost:8081/api/v1/bom"

# --- 1. Trivy 명령 실행 ---
cmd = [
    "trivy",
    "image",
    "--format", "cyclonedx",
    "--output", "sbom.json",
    f"{project_name}:{project_version}"
]

print("Trivy running...")
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    print("Trivy success: sbom.json created")

    # --- 2. Dependency-Track에 업로드 ---
    print("DT uploading...")
    with open("sbom.json", "rb") as sbom_file:
        files = {
            "bom": sbom_file,
        }
        data = {
            "projectName": project_name,
            "projectVersion": project_version,
            "autoCreate" : "true"
        }
        headers = {
            "X-Api-Key": api_key
        }

        response = requests.post(dtrack_url, headers=headers, files=files, data=data)

        if response.status_code in [200, 202]:
            print("success!")
        else:
            print(f"failed: {response.status_code}")
            print(response.text)

else:
    print("trivy failed")
    print(result.stderr)
