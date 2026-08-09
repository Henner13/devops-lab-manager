# DevOps Lab Manager

Laboratorio DevOps creado para practicar automatización, administración de sistemas e infraestructura como código.

## Objetivos

- Gestionar servidores Linux mediante Ansible.
- Automatizar tareas de administración.
- Utilizar Docker como laboratorio reproducible.
- Implementar CI/CD con GitHub Actions.
- Integrar monitorización y observabilidad.
- Aplicar buenas prácticas DevOps.

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
```

---

## Tecnologías

- Linux
- Docker
- Docker Compose
- Python
- SSH
- Ansible
- Git
- GitHub

---

## Estructura del proyecto

```text
devops-lab-manager/
│
├── ansible/
│   ├── common.yml
│   ├── install_nginx.yml
│   └── setup_ssh_keys.yml
│
├── inventory/
│   └── hosts.ini
│
├── scripts/
│   └── generate_inventory.py
│
├── docker/
│   └── Dockerfile
│
├── tests/
│
├── .github/
│
├── docker-compose.yml
└── README.md
```

---

## Despliegue del laboratorio

Construir la infraestructura:

```bash
docker compose up -d --build
```

Verificar contenedores:

```bash
docker ps
```

---

## Generar inventario Ansible

```bash
python3 scripts/generate_inventory.py
```

Resultado:

```text
inventory/hosts.ini
```

---

## Ejecutar configuración base

```bash
ansible-playbook -i inventory/hosts.ini ansible/common.yml
```

---

## Instalar Nginx

```bash
ansible-playbook -i inventory/hosts.ini ansible/install_nginx.yml
```

---

## Estado del proyecto

### Fase 1
- [x] Infraestructura Docker
- [x] Servidores SSH

### Fase 2
- [x] Inventario dinámico con Python

### Fase 3
- [x] Automatización con Ansible

### Fase 4
- [x] Configuración base de servidores

### Próximamente
- [ ] Autenticación SSH mediante claves
- [ ] GitHub Actions
- [ ] CI/CD
- [ ] Prometheus
- [ ] Grafana
- [ ] Traefik
- [ ] DevSecOps