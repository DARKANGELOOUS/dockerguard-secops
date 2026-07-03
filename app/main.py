import time
from app.monitor import start_event_monitoring

if __name__ == "__main__":
    print("🚀 Arrancando DockerGuard-SecOps Core...")
    time.sleep(2)
    start_event_monitoring()