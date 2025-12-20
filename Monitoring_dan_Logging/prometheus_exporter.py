import time
import random
from prometheus_client import start_http_server, Counter, Gauge, Histogram, Summary

REQUEST_COUNT = Counter('model_requests_total', 'Total model requests')
ERROR_COUNT = Counter('model_errors_total', 'Total model errors')
LATENCY = Histogram('model_inference_latency_seconds', 'Inference latency')
ACCURACY = Gauge('model_accuracy_score', 'Current model accuracy')
PRECISION = Gauge('model_precision_score', 'Current model precision')
RECALL = Gauge('model_recall_score', 'Current model recall')
CONFIDENCE = Summary('model_prediction_confidence', 'Prediction confidence')
CPU_USAGE = Gauge('system_cpu_usage_percent', 'System CPU usage')
MEMORY_USAGE = Gauge('system_memory_usage_bytes', 'System Memory usage')
ACTIVE_USERS = Gauge('model_active_users', 'Current active users')


def update_metrics():
    while True:
        REQUEST_COUNT.inc()
        if random.random() < 0.05:
            ERROR_COUNT.inc()

        LATENCY.observe(random.uniform(0.1, 0.5))
        ACCURACY.set(random.uniform(0.85, 0.98))
        PRECISION.set(random.uniform(0.80, 0.95))
        RECALL.set(random.uniform(0.82, 0.96))
        CONFIDENCE.observe(random.uniform(0.7, 0.99))
        CPU_USAGE.set(random.uniform(20, 80))
        MEMORY_USAGE.set(random.uniform(1024 ** 3, 4 * 1024 ** 3))
        ACTIVE_USERS.set(random.randint(1, 50))

        time.sleep(5)


if __name__ == '__main__':
    start_http_server(8000)
    print("Exporter running on port 8000")
    update_metrics()