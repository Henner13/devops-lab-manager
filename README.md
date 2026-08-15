# DevOps Lab Manager

Laboratorio DevOps desarrollado para practicar automatización, administración de sistemas, infraestructura como código (IaC), observabilidad y CI/CD utilizando tecnologías ampliamente empleadas en entornos profesionales.

---

# Objetivos

- Automatizar la gestión de servidores Linux.
- Practicar Infraestructura como Código (IaC).
- Configurar sistemas mediante Ansible.
- Utilizar autenticación SSH basada en claves.
- Crear herramientas propias de automatización.
- Implementar integración continua con GitHub Actions.
- Incorporar observabilidad y monitorización.
- Aplicar buenas prácticas DevOps y DevSecOps.

---

# Arquitectura

```text
Linux Mint
│
├── Docker Compose
│
├── server1
├── server2
└── server3
        │
        ▼
      Ansible
        │
        ▼
 Dynamic Inventory
        │
        ▼
       labctl
        │
        ▼
 GitHub Actions CI
        │
        ▼
 Monitoring Stack
 ├── Prometheus
 ├── Grafana
 └── Node Exporter
```

---

# Tecnologías utilizadas

- Linux
- Docker
- Docker Compose
- SSH
- Python
- Ansible
- Git
- GitHub
- GitHub Actions
- Prometheus
- Grafana
- Node Exporter
- YAML

---

# Funcionalidades

## Infraestructura

- Laboratorio reproducible mediante Docker Compose.
- Tres servidores Ubuntu accesibles por SSH.
- Red Docker dedicada.
- Configuración centralizada mediante Ansible.

## Automatización

- Inventario dinámico generado con Python.
- Roles de Ansible reutilizables.
- Despliegue automatizado de servicios.
- Gestión centralizada mediante la herramienta `labctl`.

## Observabilidad

- Recolección de métricas mediante Node Exporter.
- Almacenamiento de métricas en Prometheus.
- Visualización mediante Grafana.

## Integración Continua

- Validación automática con GitHub Actions.
- Verificación de sintaxis Python.
- Verificación de Docker Compose.
- Verificación de Ansible.
- Validación de la CLI personalizada.

---

# Estructura del proyecto

```text
devops-lab-manager/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── ansible/
│   ├── group_vars/
│   │   └── all.yml
│   │
│   ├── roles/
│   │   ├── common/
│   │   │   └── tasks/
│   │   │       └── main.yml
│   │   │
│   │   ├── nginx/
│   │   │   └── tasks/
│   │   │       └── main.yml
│   │   │
│   │   └── setup_ssh_keys/
│   │       └── tasks/
│   │           └── main.yml
│   │
│   ├── setup_ssh_keys.yml
│   └── site.yml
│
├── docker/
│   └── Dockerfile
│
├── inventory/
│   └── hosts.ini
│
├── monitoring/
│   └── prometheus/
│       └── prometheus.yml
│
├── scripts/
│   ├── generate_inventory.py
│   └── labctl.py
│
├── tests/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# Requisitos

- Linux Mint o cualquier distribución Linux moderna.
- Docker.
- Docker Compose.
- Python 3.
- Ansible.
- Git.

---

# Despliegue inicial

## Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/devops-lab-manager.git

cd devops-lab-manager
```

---

## Levantar la infraestructura

```bash
docker compose up -d --build
```

Verificar:

```bash
docker ps
```

Resultado esperado:

```text
server1
server2
server3
prometheus
grafana
node-exporter
```

---

# Generar inventario dinámico

```bash
python3 scripts/generate_inventory.py
```

Se generará:

```text
inventory/hosts.ini
```

---

# Bootstrap inicial

La primera vez es necesario utilizar autenticación mediante contraseña para configurar el laboratorio.

## Configurar claves SSH

```bash
ansible-playbook \
-i inventory/hosts.ini \
ansible/setup_ssh_keys.yml \
-k -K
```

Contraseña por defecto:

```text
devops123
```

Parámetros utilizados:

```text
-k = Solicitar contraseña SSH
-K = Solicitar contraseña sudo
```

---

## Aplicar configuración base

```bash
ansible-playbook \
-i inventory/hosts.ini \
ansible/site.yml \
-K
```

Esta configuración:

- Instala herramientas de administración.
- Configura Nginx.
- Configura sudo sin contraseña.
- Despliega los roles del laboratorio.

---

## Verificar sudo sin contraseña

```bash
ssh devops@localhost -p 2221
```

```bash
sudo whoami
```

Resultado esperado:

```text
root
```

---

# Operación normal

Una vez completado el bootstrap:

- Ya no es necesario usar `-k`.
- Ya no es necesario usar `-K`.

Despliegue normal:

```bash
ansible-playbook \
-i inventory/hosts.ini \
ansible/site.yml
```

O mediante:

```bash
python3 scripts/labctl.py deploy
```

---

# Uso de labctl

## Ver ayuda

```bash
python3 scripts/labctl.py help
```

## Levantar infraestructura

```bash
python3 scripts/labctl.py up
```

## Apagar infraestructura

```bash
python3 scripts/labctl.py down
```

## Reconstruir infraestructura

```bash
python3 scripts/labctl.py rebuild
```

## Mostrar contenedores

```bash
python3 scripts/labctl.py status
```

## Generar inventario

```bash
python3 scripts/labctl.py inventory
```

## Comprobar conectividad Ansible

```bash
python3 scripts/labctl.py ping
```

## Ejecutar despliegue

```bash
python3 scripts/labctl.py deploy
```

## Comprobar salud del laboratorio

```bash
python3 scripts/labctl.py health
```

## Ver logs

```bash
python3 scripts/labctl.py logs server1
```

## Mostrar URLs de monitorización

```bash
python3 scripts/labctl.py monitor
```

---

# Acceso a servidores

## Server 1

```bash
ssh devops@localhost -p 2221
```

## Server 2

```bash
ssh devops@localhost -p 2222
```

## Server 3

```bash
ssh devops@localhost -p 2223
```

---

# Roles de Ansible

## common

Configura:

- Herramientas básicas.
- Directorios de trabajo.
- Configuración común.
- Sudo sin contraseña.

## nginx

Configura:

- Instalación de Nginx.

## setup_ssh_keys

Configura:

- Directorio `.ssh`.
- Claves públicas autorizadas.
- Acceso SSH mediante claves.

---

# Monitorización

## Prometheus

Disponible en:

```text
http://localhost:9090
```

## Grafana

Disponible en:

```text
http://localhost:3000
```

Credenciales iniciales:

```text
Usuario: admin
Contraseña: admin
```

## Componentes monitorizados

- CPU
- Memoria
- Disco
- Red
- Procesos
- Uptime

---

# GitHub Actions

El proyecto utiliza integración continua mediante GitHub Actions.

Workflow:

```text
.github/workflows/ci.yml
```

## Validaciones realizadas

- Validación de sintaxis Python.
- Validación de Docker Compose.
- Validación de playbooks Ansible.
- Validación de la CLI `labctl`.

---

# Seguridad

Actualmente el laboratorio utiliza:

- Claves SSH Ed25519.
- Usuario dedicado `devops`.
- Sudo sin contraseña para automatización.
- Inventario controlado mediante Ansible.

En un entorno de producción se recomienda:

- Ansible Vault.
- Gestión centralizada de secretos.
- MFA.
- RBAC.
- Principio de mínimo privilegio.
- Rotación de credenciales.

---

# Limitaciones actuales

Los contenedores Docker son efímeros.

Si se ejecuta:

```bash
docker compose down
docker compose up -d --build
```

se perderá la configuración aplicada dentro de los contenedores, incluyendo:

- Claves SSH añadidas manualmente.
- Cambios realizados mediante Ansible.
- Configuración sudo.

Será necesario repetir el proceso de bootstrap.

---

# Roadmap

### Completado

- [x] Laboratorio Docker
- [x] Servidores SSH
- [x] Inventario dinámico
- [x] Roles Ansible
- [x] SSH Keys
- [x] Nginx
- [x] GitHub Actions
- [x] CLI labctl
- [x] Prometheus
- [x] Grafana
- [x] Health Check

### Próximamente

- [ ] Flake8
- [ ] ansible-lint
- [ ] yamllint
- [ ] Traefik
- [ ] PostgreSQL
- [ ] Dashboard personalizado Grafana
- [ ] Ansible Vault
- [ ] DevSecOps
- [ ] Despliegue automático