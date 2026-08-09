#!/usr/bin/env python3

import subprocess
from pathlib import Path

# Obtener los contenedores activos
result = subprocess.run(
    ["docker", "ps", "--format", "{{.Names}}"],
    capture_output=True,
    text=True
)

containers = result.stdout.strip().splitlines()

# Filtrar únicamente los servidores
servers = sorted(
    [
        container
        for container in containers
        if container.startswith("server")
    ]
)

# Crear inventario Ansible
inventory_content = "[servers]\n\n"

port_base = 2221

for index, server in enumerate(servers):
    inventory_content += (
        f"{server} "
        f"ansible_host=localhost "
        f"ansible_port={port_base + index} "
        f"ansible_user=devops\n"
    )

# Guardar archivo
inventory_path = Path("inventory/hosts.ini")

inventory_path.write_text(inventory_content)

print("Inventario generado correctamente:")
print()
print(inventory_content)
