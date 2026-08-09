#!/usr/bin/env python3

import subprocess
import sys


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


def help_menu():
    print("""
Comandos disponibles:

  status
  inventory
  ping
  deploy
  help
""")


commands = {
    "status": status,
    "inventory": inventory,
    "ping": ping,
    "deploy": deploy,
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