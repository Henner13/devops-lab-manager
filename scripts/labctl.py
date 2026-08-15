#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path


def status():
    subprocess.run(["docker", "ps"])


def inventory():
    subprocess.run([
        "python3",
        "scripts/generate_inventory.py"
    ])


def ping():
    subprocess.run([
        "ansible",
        "all",
        "-i",
        "inventory/hosts.ini",
        "-m",
        "ping"
    ])


def deploy():
    subprocess.run([
        "ansible-playbook",
        "-i",
        "inventory/hosts.ini",
        "ansible/site.yml"
    ])


def up():
    subprocess.run([
        "docker",
        "compose",
        "up",
        "-d",
        "--build"
    ])


def down():
    subprocess.run([
        "docker",
        "compose",
        "down"
    ])


def rebuild():
    subprocess.run([
        "docker",
        "compose",
        "down"
    ])

    subprocess.run([
        "docker",
        "compose",
        "up",
        "-d",
        "--build"
    ])


def logs():
    if len(sys.argv) < 3:
        print("Uso: python3 scripts/labctl.py logs <contenedor>")
        return

    container = sys.argv[2]

    subprocess.run([
        "docker",
        "logs",
        container
    ])


def health():

    print("\n=== HEALTH CHECK ===\n")

    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    )

    containers = result.stdout.splitlines()

    for server in ["server1", "server2", "server3"]:
        if server in containers:
            print(f"[OK] {server}")
        else:
            print(f"[ERROR] {server}")

    inventory = Path("inventory/hosts.ini")

    if inventory.exists():
        print("\n[OK] inventory/hosts.ini encontrado")
    else:
        print("\n[ERROR] inventory/hosts.ini no encontrado")


def monitor():

    print("""
Prometheus:
http://localhost:9090

Grafana:
http://localhost:3000
""")


def help_menu():
    print("""
Comandos disponibles:

  up          Levantar infraestructura
  down        Apagar infraestructura
  rebuild     Reconstruir infraestructura
  status      Mostrar contenedores
  inventory   Generar inventario
  ping        Ansible ping
  deploy      Ejecutar site.yml
  logs        Ver logs de un contenedor
  health      Estado del laboratorio
  monitor     Mostrar URLs de monitorización
  help        Mostrar ayuda


Ejemplos:

  python3 scripts/labctl.py up
  python3 scripts/labctl.py ping
  python3 scripts/labctl.py deploy
  python3 scripts/labctl.py logs server1

""")


commands = {
    "up": up,
    "down": down,
    "rebuild": rebuild,
    "status": status,
    "inventory": inventory,
    "ping": ping,
    "deploy": deploy,
    "logs": logs,
    "health": health,
    "monitor": monitor,
    "help": help_menu
}


if len(sys.argv) < 2:
    help_menu()
    sys.exit(0)

command = sys.argv[1]

if command in commands:
    commands[command]()
else:
    print(f"Comando no conocido: {command}")
    help_menu()
    sys.exit(1)
