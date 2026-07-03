import docker
from app.notifier import send_discord_alert

def start_event_monitoring():
    try:
        client = docker.from_env()
        print("📡 Conectado al Socket de Docker de forma segura. Escuchando eventos...")
        
        send_discord_alert(
            title="🛡️ DockerGuard-SecOps Iniciado",
            message="El agente de seguridad está activo y monitoreando el Homelab.",
            color=3066993
        )

        for event in client.events(decode=True, filters={"type": "container"}):
            action = event.get("Action")
            attributes = event.get("Actor", {}).get("Attributes", {})
            container_name = attributes.get("name", "Desconocido")

            if action in ["die", "stop", "kill"]:
                exit_code = event.get("Actor", {}).get("Attributes", {}).get("exitCode", "N/A")
                
                # Modificamos el mensaje para agregar una alerta de texto al inicio que despierte al celular
                alert_message = f"⚠️ **ATENCIÓN @everyone**\nEl contenedor **{container_name}** ha cambiado a estado: `{action}`."
                
                send_discord_alert(
                    title="🚨 Contenedor Detenido / Caído",
                    message=alert_message,
                    color=15158332,
                    fields=[
                        {"name": "Contenedor", "value": container_name, "inline": True},
                        {"name": "Acción Evento", "value": action, "inline": True},
                        {"name": "Exit Code", "value": str(exit_code), "inline": True}
                    ]
                )
            
            elif action == "start":
                send_discord_alert(
                    title="🆕 Nuevo Contenedor Desplegado",
                    message=f"Se ha detectado el arranque del contenedor **{container_name}**.",
                    color=3066993,
                    fields=[
                        {"name": "Contenedor", "value": container_name, "inline": True},
                        {"name": "Estado", "value": "Running", "inline": True}
                    ]
                )

    except docker.errors.DockerException as de:
        print(f"❌ Error de conexión al Socket de Docker: {de}")
    except KeyboardInterrupt:
        print("\n👋 Monitoreo detenido por el usuario.")