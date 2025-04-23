import subprocess
from locust import HttpUser, task, between


class VideoStreamingUser(HttpUser):
    @task
    def video_streaming_test(self):
        # GET 요청으로 비디오 스트리밍 엔드포인트에 요청
        self.client.get(
            "/api-test/video-streaming",
            params={"videoHeight": "H720"},
            headers={"Accept": "application/octet-stream"}
        )


if __name__ == "__main__":
    subprocess.run([
        "locust",
        "-f", "stress_test_locusts/locust_case1.py",  # locust 파일 경로
        "--host", "http://localhost:12006",  # 테스트 대상 호스트
        "--web-port", "12345",  # 다른 포트로 웹 UI를 실행
        "--headless",  # CLI 모드로 실행 (브라우저 UI 없이)
        "-u", "500",  # 사용자 수
        "-r", "30",  # 초당 몇 명씩 증가할지
        "--run-time", "1m",  # 총 실행 시간
    ])
