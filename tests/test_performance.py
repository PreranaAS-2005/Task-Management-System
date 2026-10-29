
import time
from app import app


def test_dashboard_response_performance():
    client = app.test_client()

    number_of_requests = 100
    start_time = time.perf_counter()

    for _ in range(number_of_requests):
        response = client.get("/dashboard")
        assert response.status_code == 200

    end_time = time.perf_counter()

    total_time = end_time - start_time
    average_time = total_time / number_of_requests
    throughput = number_of_requests / total_time

    print(f"\nRequests tested: {number_of_requests}")
    print(f"Total time: {total_time:.4f} seconds")
    print(f"Average response time: {average_time * 1000:.2f} ms")
    print(f"Throughput: {throughput:.2f} requests/second")
