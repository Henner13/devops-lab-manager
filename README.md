# DevOps Lab Manager

Laboratorio DevOps creado para practicar automatización, administración de sistemas e infraestructura como código utilizando Docker, Python y Ansible.

## Objetivos

- Automatizar la gestión de servidores Linux.
- Practicar Infraestructura como Código (IaC).
- Configurar servidores mediante Ansible.
- Utilizar autenticación SSH por claves.
- Crear herramientas propias de automatización.
- Preparar una base para CI/CD con GitHub Actions.
- Incorporar observabilidad y monitorización en futuras fases.

---

## Arquitectura

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
```

---

## Tecnologías utilizadas

- Linux
- Docker
- Docker Compose
- SSH
- Python
- Ansible
- Git
- GitHub
- YAML

---

## Estructura del proyecto

```text
devops-lab-manager/
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
│   └── site.yml
│
├── docker/
│   └── Dockerfile
│
├── inventory/
│   └── hosts.ini
│
├── scripts/
│   ├── generate_inventory.py
│   └── labctl.py
│
├── tests/
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## Requisitos

- Linux Mint o cualquier distribución Linux moderna.
- Docker.
- Docker Compose.
- Python 3.
- Ansible.
- Git.

---

## Despliegue inicial

### Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/devops-lab-manager.git

cd devops-lab-manager
```

### Levantar los servidores

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
```

---

## Generar inventario dinámico

```bash
python3 scripts/generate_inventory.py
```

Se generará:

```text
inventory/hosts.ini
```

---

## Bootstrap inicial

La primera vez es necesario utilizar autenticación mediante contraseña para configurar el entorno.

### Configurar claves SSH

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

Parámetros:

```text
-k = Solicitar contraseña SSH
-K = Solicitar contraseña sudo
```

---

### Aplicar configuración inicial

```bash
ansible-playbook \
-i inventory/hosts.ini \
ansible/site.yml \
-K
```

Esta configuración:

- Instala herramientas básicas.
- Configura Nginx.
- Configura sudo sin contraseña para el usuario devops.
- Aplica la configuración común del laboratorio.

---

### Verificar sudo sin contraseña

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

## Operación normal

Una vez completado el bootstrap inicial ya no es necesario usar:

```bash
-k
```

ni:

```bash
-K
```

Los despliegues posteriores pueden ejecutarse directamente:

```bash
ansible-playbook \
-i inventory/hosts.ini \
ansible/site.yml
```

o mediante:

```bash
python3 scripts/labctl.py deploy
```

---

## Uso de labctl

### Estado de los contenedores

```bash
python3 scripts/labctl.py status
```

### Regenerar inventario

```bash
python3 scripts/labctl.py inventory
```

### Probar conectividad Ansible

```bash
python3 scripts/labctl.py ping
```

### Ejecutar despliegue completo

```bash
python3 scripts/labctl.py deploy
```

---

## Acceso a servidores

### Server 1

```bash
ssh devops@localhost -p 2221
```

### Server 2

```bash
ssh devops@localhost -p 2222
```

### Server 3

```bash
ssh devops@localhost -p 2223
```

---

## Roles de Ansible

### common

Configura:

- Herramientas básicas.
- Directorios de trabajo.
- Configuración común.
- Sudo sin contraseña.

### nginx

Configura:

- Instalación de Nginx.

### setup_ssh_keys

Configura:

- Directorio `.ssh`.
- Claves públicas autorizadas.
- Acceso SSH por claves.

---

## Seguridad

Actualmente el laboratorio utiliza:

- Claves SSH Ed25519.
- Usuario dedicado `devops`.
- Sudo sin contraseña para facilitar la automatización.

En un entorno productivo se recomienda:

- Ansible Vault.
- Gestión centralizada de secretos.
- MFA.
- Control de acceso basado en roles.
- Principio de mínimo privilegio.

---

## Limitaciones actuales

Los contenedores Docker son efímeros.

Si se ejecuta:

```bash
docker compose down
docker compose up -d --build
```

los contenedores serán recreados y se perderán:

- Claves SSH configuradas manualmente.
- Configuración de sudo aplicada mediante Ansible.

Será necesario ejecutar nuevamente el proceso de bootstrap.

---

## Roadmap

### Completado

- [x] Laboratorio Docker.
- [x] Servidores SSH.
- [x] Inventario dinámico con Python.
- [x] Roles Ansible.
- [x] Despliegue de Nginx.
- [x] SSH por claves.
- [x] CLI de administración labctl.

### Próximamente

- [ ] GitHub Actions.
- [ ] CI/CD.
- [ ] Tests automáticos.
- [ ] Linting.
- [ ] Prometheus.
- [ ] Grafana.
- [ ] Traefik.
- [ ] DevSecOps.
- [ ] Monitoreo centralizado.
- [ ] Gestión de secretos con Ansible Vault.

---

## Autor

Proyecto desarrollado como laboratorio práctico de aprendizaje DevOps para demostrar habilidades en:

- Linux
- Docker
- Python
- SSH
- Ansible
- Automatización
- Infraestructura como Código
- CI/CD