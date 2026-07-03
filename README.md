# DockerGuard-SecOps

DockerGuard-SecOps es un agente de monitoreo ligero desarrollado en Python y diseñado para entornos Homelab. La aplicación se conecta directamente al Socket de Docker para escuchar eventos del ciclo de vida de los contenedores en tiempo real y despachar alertas visuales estilizadas hacia canales de Discord mediante Webhooks.

## Características

- Monitoreo en tiempo real del estado de los contenedores (Arranque, paradas, caídas accidentales).
- Extracción automática de códigos de salida (Exit Codes) ante fallos críticos.
- Despliegue en contenedor aislado mediante Docker de forma nativa.
- Consumo mínimo de recursos en la máquina host.

## Requisitos Previos

- Docker Engine instalado y en ejecución.
- Docker Compose.
- Un Webhook URL de un canal de Discord.

## Estructura del Proyecto

```text
dockerguard-secops/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── monitor.py
│   └── notifier.py
├── .gitignore
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md