
# DevOps Lab Manager

[![CI](https://github.com/Henner13/devops-lab-manager/actions/workflows/ci.yml/badge.svg)]((https://github.com/Henner13/devops-lab-manager/actions/workflows/ci.yml))

Laboratorio DevOps desarrollado para practicar automatización, administración de sistemas, Infraestructura como Código (IaC), observabilidad, monitorización, gestión de alertas, DevSecOps y CI/CD utilizando tecnologías ampliamente empleadas en entornos profesionales.

---

# Objetivos

- Automatizar la gestión de servidores Linux.
- Practicar Infraestructura como Código (IaC).
- Configurar sistemas mediante Ansible.
- Utilizar autenticación SSH basada en claves.
- Crear herramientas propias de automatización.
- Implementar integración continua mediante GitHub Actions.
- Incorporar observabilidad y monitorización.
- Gestionar alertas de forma centralizada.
- Aplicar buenas prácticas DevOps y DevSecOps.
- Aprender gestión segura de secretos.

---

# Arquitectura

```text
Linux
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
 GitHub Actions
        │
        ├── Flake8
        ├── yamllint
        ├── ansible-lint
        ├── Trivy
        └── Gitleaks
        │
        ▼
 Monitoring Stack
 ├── Node Exporter
 ├── Prometheus
 ├── Alertmanager
 └── Grafana
        │
        ▼
     Telegram
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
- Alertmanager
- Grafana
- Node Exporter
- Trivy
- Gitleaks
- YAML

---

# Funcionalidades

## Infraestructura

- Laboratorio reproducible mediante Docker Compose.
- Tres servidores Linux accesibles por SSH.
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
- Dashboards mediante Grafana.
- Health Checks.
- Alertas automáticas.
- Notificaciones automáticas mediante Telegram.

## DevSecOps

- Escaneo de vulnerabilidades mediante Trivy.
- Detección de secretos mediante Gitleaks.
- Gestión segura de secretos mediante Ansible Vault.
- Validaciones automáticas en GitHub Actions.

## Integración Continua

- Validación automática mediante GitHub Actions.
- Flake8.
- yamllint.
- ansible-lint.
- Validación de scripts Python.
- Validación de Docker Compose.
- Comprobación de la CLI personalizada.

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
│   │   ├── all.yml
│   │   └── vault.yml
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
│   │   ├── node_exporter/
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
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── alerts.yml
│   │
│   └── alertmanager/
│       └── alertmanager.yml
│
├── scripts/
│   ├── generate_inventory.py
│   └── labctl.py
│
├── tests/
│
├── requirements-dev.txt
├── .flake8
├── .yamllint.yml
├── ansible.cfg
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Arquitectura visual

![Architecture](https://github.com/Henner13/devops-lab-manager/blob/main/docs/images/architecture.png)

---

# Requisitos

- Linux Mint o cualquier distribución Linux moderna.
- Docker.
- Docker Compose.
- Python 3.
- Ansible.
- Git.

---

# Entorno virtual Python

Crear entorno virtual:

```bash
python3 -m venv .venv
```

Activar:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements-dev.txt
```

---

# Despliegue inicial

## Clonar repositorio

```bash
git clone https://github.com/Henner13/devops-lab-manager.git

cd devops-lab-manager
```

---

## Levantar infraestructura

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
alertmanager
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

## Configurar claves SSH

```bash
ansible-playbook -i inventory/hosts.ini ansible/setup_ssh_keys.yml -k -K
```

Contraseña por defecto:

```text
devops123
```

---

## Aplicar configuración base

```bash
ansible-playbook -i inventory/hosts.ini ansible/site.yml -K
```

Esta configuración:

- Instala herramientas base.
- Configura Nginx.
- Configura Node Exporter.
- Configura sudo sin contraseña.
- Despliega los roles del laboratorio.

---

# Operación normal

Una vez completado el bootstrap:

```bash
ansible-playbook -i inventory/hosts.ini ansible/site.yml
```

o:

```bash
labctl deploy
```

---

# Uso de labctl

Se recomienda crear un alias:

```bash
alias labctl="python3 scripts/labctl.py"
```

Aplicar cambios:

```bash
source ~/.bashrc
```

---

## Mostrar ayuda

```bash
labctl help
```

## Levantar entorno

```bash
labctl up
```

## Apagar entorno

```bash
labctl down
```

## Reconstruir entorno

```bash
labctl rebuild
```

## Estado de contenedores

```bash
labctl status
```

## Inventario dinámico

```bash
labctl inventory
```

## Ansible Ping

```bash
labctl ping
```

## Ejecutar despliegue

```bash
labctl deploy
```

## Health Check

```bash
labctl health
```

## Logs

```bash
labctl logs server1
```

## URLs de monitorización

```bash
labctl monitor
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

- Claves SSH.
- Directorio `.ssh`.
- Authorized Keys.

## node_exporter

Configura:

- Instalación de Node Exporter.
- Configuración para monitorización.

---

# Monitorización

## Prometheus

Disponible en:

```text
http://localhost:9090
```

### Reglas

```text
http://localhost:9090/rules
```

### Alertas

```text
http://localhost:9090/alerts
```
## Prometheus-Alerts

![Prometheus-Alerts](https://github.com/Henner13/devops-lab-manager/blob/main/docs/images/prometheus-alerts.png)

---

## Grafana

Disponible en:

```text
http://localhost:3000
```

### Credenciales iniciales

```text
Usuario: admin
Contraseña: admin
```

Tras el primer acceso Grafana solicitará cambiar la contraseña.

### Data Source

Prometheus:

```text
http://prometheus:9090
```

### Dashboard

Dashboard utilizado:

```text
1860
```

Node Exporter Full Dashboard.

### Métricas monitorizadas

- CPU
- Memoria
- Disco
- Red
- Procesos
- Uptime
- Load Average

## Grafana Dashboard

![Grafana-Dashboard](https://github.com/Henner13/devops-lab-manager/blob/main/docs/images/grafana-dashboard.png)

---

# Alertmanager

Alertmanager centraliza y gestiona las alertas generadas por Prometheus.

Disponible en:

```text
http://localhost:9093
```

Arquitectura:

```text
Node Exporter
      │
      ▼
 Prometheus
      │
      ▼
 Alertmanager
      │
      ▼
   Telegram
```
![Alertmanager](https://github.com/Henner13/devops-lab-manager/blob/main/docs/images/alertmanager.png)

---

# Telegram Notifications

El laboratorio permite enviar alertas directamente a Telegram.

Ejemplo:

```text
🚨 DevOps Lab

Alerta:
HostDown

Estado:
firing
```
![Telegram-Alerts](https://github.com/Henner13/devops-lab-manager/blob/main/docs/images/telegram-alert.png)

## Estado actual

Actualmente la configuración utiliza un fichero local:

```text
monitoring/alertmanager/alertmanager.yml
```

que contiene:

- Bot Token.
- Chat ID.

Esto simplifica el aprendizaje inicial y facilita las pruebas.

## Mejora planificada

En futuras versiones se migrará a una solución más profesional basada en:

- Ansible Vault.
- Templates.
- Gestión centralizada de secretos.

Objetivos:

- No almacenar secretos en texto plano.
- Evitar exponer credenciales en GitHub.
- Aplicar buenas prácticas DevSecOps.

---

# Calidad del código

## Flake8

```bash
flake8 scripts
```

## yamllint

```bash
yamllint .
```

## ansible-lint

```bash
ansible-lint ansible/site.yml
```

---

# GitHub Actions

Workflow:

```text
.github/workflows/ci.yml
```

Validaciones automáticas:

- Python Compile.
- Docker Compose Validation.
- Flake8.
- yamllint.
- ansible-lint.
- Trivy Security Scan.
- Gitleaks Secret Detection.
- Validación de labctl.


![Github-Actions](https://github.com/Henner13/devops-lab-manager/blob/main/docs/images/github-actions.png)

---

# Seguridad

Actualmente el laboratorio utiliza:

- Claves SSH Ed25519.
- Usuario dedicado `devops`.
- Sudo sin contraseña para automatización.
- Alertas centralizadas mediante Alertmanager.
- Notificaciones automáticas mediante Telegram.
- Trivy para escaneo de vulnerabilidades.
- Gitleaks para detección de secretos.
- Ansible Vault para gestión segura de secretos.
- Validaciones automáticas en GitHub Actions.

En producción se recomienda:

- MFA.
- Rotación de credenciales.
- Gestión centralizada de secretos.
- RBAC.
- Principio de mínimo privilegio.

---

# Trivy

Trivy permite analizar vulnerabilidades en imágenes Docker.

### Instalación

```bash
sudo apt install wget apt-transport-https gnupg -y

wget -qO - https://get.trivy.dev/deb/public.key \
| gpg --dearmor \
| sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://get.trivy.dev/deb generic main" \
| sudo tee /etc/apt/sources.list.d/trivy.list

sudo apt update
sudo apt install trivy -y
```

### Comprobar instalación

```bash
trivy --version
```

### Escanear imágenes

```bash
trivy image grafana/grafana:latest
```

```bash
trivy image prom/prometheus:latest
```

```bash
trivy image prom/alertmanager:latest
```

### Niveles de severidad

- CRITICAL
- HIGH
- MEDIUM
- LOW
- UNKNOWN

### Estado actual

Trivy se ejecuta localmente y también forma parte de la pipeline de GitHub Actions.

---

# Gitleaks

Gitleaks detecta secretos expuestos accidentalmente en el repositorio.

Permite identificar:

- Tokens.
- API Keys.
- Contraseñas.
- Credenciales.
- Secretos en commits históricos.

### Instalación

```bash
curl -sSfL https://raw.githubusercontent.com/gitleaks/gitleaks/master/install.sh | bash
```

### Ejecutar análisis

```bash
gitleaks detect
```

### Estado actual

Integrado en GitHub Actions para validación automática de código.

---

# Gestión de secretos

## Ansible Vault

El laboratorio utiliza Ansible Vault para cifrar información sensible.

Ejemplos:

- Tokens Telegram.
- API Keys.
- Contraseñas.
- Secretos de despliegue.

### Crear fichero cifrado

```bash
ansible-vault create ansible/group_vars/vault.yml
```

### Ver contenido

```bash
ansible-vault view ansible/group_vars/vault.yml
```

### Editar contenido

```bash
ansible-vault edit ansible/group_vars/vault.yml
```

### Ejecutar playbooks

```bash
ansible-playbook -i inventory/hosts.ini ansible/site.yml \
  --ask-vault-pass
```

### Objetivo

Evitar almacenar información sensible en texto plano dentro del repositorio.

---

# Limitaciones actuales

Los contenedores Docker son efímeros.

Tras ejecutar:

```bash
docker compose down
docker compose up -d --build
```

puede ser necesario repetir parte del bootstrap debido a la pérdida de configuraciones internas.

---

# Roadmap

## Completado

- [x] Laboratorio Docker
- [x] Servidores SSH
- [x] Inventario dinámico
- [x] Roles Ansible
- [x] SSH Keys
- [x] Nginx
- [x] Node Exporter
- [x] Prometheus
- [x] Grafana
- [x] Alertas Prometheus
- [x] Alertmanager
- [x] Notificaciones Telegram
- [x] Trivy
- [x] Integración de Trivy en GitHub Actions
- [x] Gitleaks
- [x] GitHub Actions
- [x] Flake8
- [x] yamllint
- [x] ansible-lint
- [x] CLI labctl
- [x] Health Check
- [x] Gestión segura de secretos con Ansible Vault

## Próximamente

- [ ] Migrar Telegram a Ansible Vault
- [ ] Dashboard Grafana personalizado
- [ ] PostgreSQL
- [ ] Traefik Reverse Proxy
- [ ] Despliegue automático mediante GitHub Actions
- [ ] Multi-host deployment
- [ ] Gestión avanzada de secretos

---

# Autor

Proyecto desarrollado como laboratorio práctico para reforzar conocimientos de:

- Linux
- Docker
- Docker Compose
- SSH
- Python
- Ansible
- GitHub Actions
- Observabilidad
- Monitorización
- Automatización
- Infraestructura como Código
- CI/CD
- DevOps
- DevSecOps