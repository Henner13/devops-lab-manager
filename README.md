# DevOps Lab Manager

Laboratorio DevOps desarrollado para practicar automatización, administración de sistemas, Infraestructura como Código (IaC), observabilidad, monitorización y CI/CD utilizando tecnologías ampliamente empleadas en entornos profesionales.

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
- Visualización mediante Grafana.
- Alertas básicas mediante Prometheus Rules.

## Integración Continua

- Validación automática con GitHub Actions.
- Verificación de sintaxis Python.
- Verificación de Docker Compose.
- Verificación de Ansible.
- Validación de calidad del código.

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
│   │   ├── setup_ssh_keys/
│   │   │   └── tasks/
│   │   │       └── main.yml
│   │   │
│   │   └── node_exporter/
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
│       ├── prometheus.yml
│       └── alerts.yml
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

# Entorno virtual Python

Se recomienda utilizar un entorno virtual para el desarrollo:

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

## Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/devops-lab-manager.git

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
ansible-playbook -i inventory/hosts.ini ansible/setup_ssh_keys.yml -k -K
```

Contraseña por defecto:

```text
devops123
```

Parámetros:

```text
-k = Solicitar contraseña SSH
-K = Solicitar contraseña sudo
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

Una vez completado el bootstrap inicial:

- Ya no es necesario usar `-k`.
- Ya no es necesario usar `-K`.

Ejecutar despliegue:

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

Añadirlo a:

```bash
~/.bashrc
```

o:

```bash
~/.zshrc
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

## Levantar laboratorio

```bash
labctl up
```

## Apagar laboratorio

```bash
labctl down
```

## Reconstruir laboratorio

```bash
labctl rebuild
```

## Estado de contenedores

```bash
labctl status
```

## Generar inventario

```bash
labctl inventory
```

## Comprobar conectividad Ansible

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
- Configuración sudo.

## nginx

Configura:

- Instalación de Nginx.

## setup_ssh_keys

Configura:

- Directorio `.ssh`.
- Claves públicas autorizadas.
- Acceso SSH mediante claves.

## node_exporter

Configura:

- Descarga de Node Exporter.
- Instalación del binario.
- Configuración para monitorización.

---

# Monitorización

## Prometheus

Disponible en:

```text
http://localhost:9090
```

### Consultas útiles

```promql
up
```

```promql
node_cpu_seconds_total
```

```promql
node_memory_MemAvailable_bytes
```

### Reglas

```text
http://localhost:9090/rules
```

### Alertas

```text
http://localhost:9090/alerts
```

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

Grafana solicitará cambiar la contraseña en el primer acceso.

### Configurar Prometheus como Data Source

URL:

```text
http://prometheus:9090
```

### Dashboard utilizado

```text
1860
```

Node Exporter Full Dashboard.

---

## Componentes monitorizados

- CPU
- Memoria
- Disco
- Red
- Load Average
- Procesos
- Uptime

---

# Alertas

Actualmente el laboratorio incluye alertas básicas mediante Prometheus.

## HostDown

Se dispara cuando un objetivo deja de responder durante más de un minuto.

Ver reglas:

```text
http://localhost:9090/rules
```

Ver alertas:

```text
http://localhost:9090/alerts
```

---

# Calidad del código

El proyecto incorpora herramientas de calidad para detectar errores automáticamente.

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

El proyecto utiliza integración continua mediante GitHub Actions.

Workflow:

```text
.github/workflows/ci.yml
```

## Validaciones realizadas

- Compilación de scripts Python.
- Validación de Docker Compose.
- Validación de playbooks Ansible.
- Flake8.
- yamllint.
- ansible-lint.
- Test básico de la CLI `labctl`.

---

# Seguridad

Actualmente el laboratorio utiliza:

- Claves SSH Ed25519.
- Usuario dedicado `devops`.
- Sudo sin contraseña para automatización.
- Inventario controlado mediante Ansible.

En producción se recomienda:

- Ansible Vault.
- Gestión centralizada de secretos.
- MFA.
- RBAC.
- Rotación de credenciales.
- Principio de mínimo privilegio.

---

# Limitaciones actuales

Los contenedores Docker son efímeros.

Si se ejecuta:

```bash
docker compose down
docker compose up -d --build
```

será necesario repetir parte del bootstrap ya que se perderá la configuración aplicada dentro de los contenedores.

Entre otros elementos:

- Claves SSH.
- Configuración sudo.
- Cambios realizados manualmente en los servidores.

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
- [x] Alertas básicas Prometheus
- [x] GitHub Actions
- [x] Flake8
- [x] yamllint
- [x] ansible-lint
- [x] CLI labctl
- [x] Health Check

## Próximamente

- [ ] Traefik Reverse Proxy
- [ ] Alertmanager
- [ ] Notificaciones Telegram
- [ ] Notificaciones Discord
- [ ] Dashboard Grafana personalizado
- [ ] PostgreSQL
- [ ] Ansible Vault
- [ ] DevSecOps
- [ ] Despliegue automático con GitHub Actions
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
- Automatización
- Infraestructura como Código
- CI/CD
- DevOps
- DevSecOps