# EXPERIMENT No: 6 — Installing Docker Image on RPi

**Title:** Installing docker image on RPi  
**Course:** 23CSE3013 – Internet of Things (End Nodes & Gateways)  
**Experiment:** Install Docker on Raspberry Pi, pull & run Docker image, create Dockerfile, deploy containerized IoT service  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Professor:** Prof. Ujjwala N. Salunkhe  

---

## 📋 Aim of the Experiment

To install Docker on Raspberry Pi, pull and run a Docker image, create a custom Docker image using a Dockerfile, and deploy a simple containerized IoT service.

---

## ✅ Write-Up Question 1 — Explain the Procedure for Installing Docker on Raspberry Pi and Describe the Role of Docker in IoT Applications.

### Part A — Procedure for Installing Docker on Raspberry Pi

**Step 1: Update Raspberry Pi package repository**

```
sudo apt update
sudo apt upgrade -y
```

**Step 2: Download Docker installation script**

```
curl -fsSL https://get.docker.com -o get-docker.sh
ls
```

**Step 3: Install Docker**

```
sudo sh get-docker.sh
```

**Step 4: Verify Docker installation**

```
docker --version
```

Example output:

```
Docker version 28.x.x
```

```
sudo systemctl status docker
```

Look for: `Active: active (running)` → press `q` to exit.

**Step 5: Add user to Docker group (avoid sudo)**

```
sudo usermod -aG docker $USER
sudo reboot
```

**Step 6: Verify Docker works without sudo**

```
docker ps
```

Expected output (empty list is normal when no containers exist):

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS   PORTS     NAMES
```

---

### Role of Docker in IoT Applications

- **Containerization:** Packages IoT application code + dependencies into an isolated container.
- **Portability:** Runs identically on Raspberry Pi, laptop, or any Docker host.
- **Isolation:** IoT service runs in its own environment — no conflict with host OS or other services.
- **Reproducibility:** `Dockerfile` defines exact environment (base image, deps, commands).
- **Edge deployment:** Lightweight containers run IoT services (Python/Flask) on resource-constrained edge devices like RPi.
- **Scalability:** Multiple IoT microservices can run as separate containers.
- **Version control of infra:** Docker images can be versioned, pushed to registries (Docker Hub).

---

## ✅ Write-Up Question 2 — Write the Commands to Pull and Run the hello-world or nginx Docker Image on Raspberry Pi. Explain How to Verify that the Container is Running.

### Commands — Pull and Run hello-world

```
docker pull hello-world
docker images
docker run hello-world
```

Expected output:

```
Hello from Docker!
```

To check containers:

```
docker ps
docker ps -a
```

`hello-world` exits after printing the message, hence it appears under `Exited (0)` in `docker ps -a`.

### Commands — Run nginx

```
docker pull nginx
docker images
docker run -d --name mynginx -p 8080:80 nginx
docker ps
```

Command explanation:

| Flag | Meaning |
|------|---------|
| `docker run` | Create and start a container |
| `-d` | Run in detached/background mode |
| `--name mynginx` | Assign container name |
| `-p 8080:80` | Map RPi port 8080 → container port 80 |

**Verify nginx is running:**

```
docker ps
```

Expected:

```
IMAGE     STATUS          PORTS
nginx     Up ...          0.0.0.0:8080->80/tcp
```

**Access via browser:**

```
hostname -I   # e.g. 192.168.1.105
```

Open browser:

```
http://192.168.1.105:8080
```

Expected: `Welcome to nginx!` page.

**Alternative verification via curl:**

```
curl http://localhost:8080
```

**Stop / start / remove nginx container:**

```
docker stop mynginx
docker start mynginx
docker stop mynginx
docker rm mynginx
```

---

## ✅ Write-Up Question 3 — Develop a Dockerfile for a Simple Python Application. Explain the Purpose of the FROM, WORKDIR, COPY, RUN, and CMD Instructions.

### Python IoT App (`app.py`)

```python
import time
import random

print("IoT Sensor Service Started")

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)

    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("-------------------------")

    time.sleep(5)
```

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

### Purpose of Each Instruction

| Instruction | Purpose |
|-------------|---------|
| `FROM python:3.11-slim` | Specifies the base Docker image (Python 3.11 slim) for the container |
| `WORKDIR /app` | Sets the working directory inside the container where the app will run |
| `COPY app.py .` | Copies the application file (`app.py`) from the host into the container's working directory |
| `RUN` | (Optional) Runs commands during image build — here not needed since base image already has Python |
| `CMD ["python", "app.py"]` | Specifies the command to execute when the container starts |

### Build and Run the Custom Image

```
mkdir ~/iot-docker
cd ~/iot-docker
nano app.py
nano Dockerfile

docker build -t iot-python-app .
docker images
docker run -d --name iot-service iot-python-app
docker ps
docker logs iot-service
docker logs -f iot-service   # Ctrl+C to stop following
```

Expected output:

```
IoT Sensor Started
Temperature: 26.43 °C
Humidity: 62.31 %
-------------------------
Temperature: 28.12 °C
Humidity: 67.42 %
-------------------------
```

Stop container: `Ctrl + C` (if run in foreground) or:

```
docker stop iot-service
```

---

## ✅ Write-Up Question 4 — Explain How to Deploy a Containerized IoT Service on Raspberry Pi. Describe How to Verify its Operation and Analyze the Benefits of Using Docker for IoT Edge Computing.

### Deployment of Containerized IoT Service (Flask Web Service)

**Step 1: Stop/remove the previous Python container**

```
docker stop iot-service
docker rm iot-service
```

**Step 2: Create Flask-based IoT app (`app.py`)**

```python
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "Raspberry Pi IoT Docker Service"

@app.route("/sensor")
def sensor():
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)

    return {
        "temperature": temperature,
        "humidity": humidity,
        "temperature_unit": "C",
        "humidity_unit": "%"
    }

app.run(host="0.0.0.0", port=5000)
```

**Step 3: Update Dockerfile for Flask**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

**Step 4: Build and run the web service**

```
docker build -t iot-web-service .
docker images
docker run -d --name iot-web -p 5000:5000 iot-web-service
docker ps
docker logs iot-web
docker logs -f iot-web
```

**Step 5: Verify operation**

Find RPi IP:

```
hostname -I   # e.g. 192.168.1.105
```

Open browser:

```
http://192.168.1.105:5000
```

Expected:

```
Raspberry Pi IoT Docker Service
```

Sensor endpoint:

```
http://192.168.1.105:5000/sensor
```

Expected JSON response (values change on refresh):

```json
{
    "humidity": 63.25,
    "humidity_unit": "%",
    "temperature": 27.46,
    "temperature_unit": "C"
}
```

**Verification via curl:**

```
curl http://localhost:5000
curl http://localhost:5000/sensor
```

**Stop / start / remove the service:**

```
docker stop iot-web
docker start iot-web
docker rm iot-web
```

---

### Benefits of Using Docker for IoT Edge Computing

1. **Consistency:** The IoT service runs in the same environment on RPi as on developer machine → no "works on my machine" issues.
2. **Isolation & Security:** Container isolation limits blast radius; services run independently.
3. **Lightweight:** Docker containers are lightweight compared to full VMs — suitable for resource-constrained RPi.
4. **Fast deployment:** `docker build` + `docker run` → quick onboarding of IoT services.
5. **Scalability:** Multiple IoT microservices can be orchestrated (docker-compose, Swarm, Kubernetes).
6. **Port management:** `-p <host>:<container>` mapping exposes services (e.g., Flask on 5000) to local network/browser.
7. **Logging & monitoring:** `docker logs`, `docker inspect`, `docker system df` for operations.
8. **Reproducibility:** Dockerfile pins base image, dependencies, and commands.
9. **Future cloud integration:** Containers can later be deployed to cloud (AWS ECS, Azure Container Apps) with minimal changes.

---

## 📚 Quick Revision — Experiment 6

| Part | Command / Concept |
|------|------------------|
| Install Docker | `curl -fsSL https://get.docker.com -o get-docker.sh` → `sudo sh get-docker.sh` |
| Verify | `docker --version`, `sudo systemctl status docker` |
| Group add | `sudo usermod -aG docker $USER` → reboot |
| Pull | `docker pull hello-world` / `docker pull nginx` |
| Run hello-world | `docker run hello-world` → `Hello from Docker!` |
| Run nginx | `docker run -d --name mynginx -p 8080:80 nginx` |
| Access nginx | Browser → `http://<RPI-IP>:8080` → `Welcome to nginx!` |
| Custom image | `docker build -t iot-python-app .` |
| Dockerfile | `FROM python:3.11-slim`, `WORKDIR /app`, `COPY app.py .`, `CMD ["python","app.py"]` |
| Run custom | `docker run -d --name iot-service iot-python-app` |
| Logs | `docker logs iot-service`, `docker logs -f iot-service` |
| Flask service | `FROM python:3.11-slim`, `WORKDIR /app`, `RUN pip install flask`, `COPY app.py .`, `EXPOSE 5000`, `CMD ["python","app.py"]` |
| Run Flask | `docker build -t iot-web-service .` → `docker run -d --name iot-web -p 5000:5000 iot-web-service` |
| Access Flask | Browser → `http://<RPI-IP>:5000` → `Raspberry Pi IoT Docker Service` |
| Sensor API | Browser/curl → `http://<RPI-IP>:5000/sensor` → JSON |

---

## 🧠 Viva Questions — Quick Answers (Experiment 6)

| Q | Answer |
|---|--------|
| Q1. What is Docker? | Platform to package/run apps in isolated containers. |
| Q2. What is a Docker image? | Read-only template containing app + dependencies. |
| Q3. What is a Docker container? | Running instance of an image. |
| Q4. Why useful in IoT? | Isolated, reproducible, lightweight deployment on edge (RPi). |
| Q5. Purpose of Dockerfile? | Instructions to build custom image (FROM, WORKDIR, COPY, RUN, CMD, EXPOSE). |
| Q6. Command to download image? | `docker pull <image>` |
| Q7. Run container in background? | `docker run -d <image>` |
| Q8. Why port mapping needed? | Container port → host port mapping so external clients can access service (e.g., `-p 5000:5000`). |
| Q9. Verify container stopped? | `docker ps -a` + `docker logs <container>`. |
| Q10. Extend to real IoT? | Connect real sensor (DHT11/DHT22/BMP280) → RPi GPIO/I2C → Python → Dockerized service → API. |

---

## ✅ Conclusion

Docker was successfully installed on the Raspberry Pi, a hello-world and nginx image were pulled and run with verification, a custom Python Docker image was built using a Dockerfile (FROM, WORKDIR, COPY, RUN, CMD), and a containerized Flask-based IoT service was deployed and verified via browser/API. Docker enables lightweight, portable, reproducible IoT edge deployments.

---

**Good luck with your Experiment 6 viva & write-up!**

---

## ✅ Write-Up Question 5 (Experiment 10) — Git & GitHub Write-Up Solutions

### Q1. What is Git? What is GitHub? List any five commonly used Git commands.

**Answer:**

- **Git:** Distributed version control system that tracks changes in source code during software development. Each developer has a full copy of the repository locally; changes are committed locally and pushed to remote.
- **GitHub:** Cloud-based hosting service for Git repositories — provides remote storage, collaboration, pull requests, issues, and CI/CD integration.

**Five commonly used Git commands:**

| Command | Purpose |
|---------|---------|
| `git init` | Create a new local Git repository |
| `git add .` | Stage changes |
| `git commit -m "message"` | Commit staged changes locally |
| `git push` / `git push -u origin main` | Push commits to GitHub remote |
| `git pull` | Fetch and merge latest changes from remote |

---

### Q2. Explain the difference between a local Git repository and a remote GitHub repository. What is the purpose of committing changes?

**Answer:**

- **Local repository:** Stored on the local machine (e.g., Raspberry Pi or laptop). Commits exist only locally until pushed. Enables offline work, branching, history.
- **Remote repository:** Hosted on GitHub (e.g., `https://github.com/USERNAME/REPO.git`). Acts as central backup, enables collaboration via push/pull, pull requests, forks, issues.

- **Purpose of committing:** Records a snapshot of changes with a message; creates history; enables reverting, branching, and sharing via push to remote.

---

### Q3. Evaluate the advantages of using Git and GitHub for IoT projects compared with storing source-code files only on a local computer or Raspberry Pi.

**Answer:**

- **Version control history:** track every change, revert bugs, see who changed what.
- **Backup & recovery:** remote mirror on GitHub protects against local loss/corruption.
- **Collaboration:** multiple developers (student + team) can work in parallel via branches/PRs.
- **Portfolio:** GitHub serves as public showcase of IoT project code.
- **Automation:** CI/CD, GitHub Actions can build/test/deploy IoT services.
- **Documentation:** README, commit messages maintain project context.
- **Disadvantage of local-only:** no history backup, no collaboration, no remote backup, no code review workflow.

---

### Q4. Evaluate the advantages of using Git and GitHub for IoT projects compared with storing source-code files only on a local computer or Raspberry Pi.

**Answer:**

*(Same as Q3 — evaluation of advantages; key points: backup, history, collaboration, CI/CD, portfolio, reproducibility, team workflows, security/permissions via GitHub.)*

---

## ✅ Conclusion (Experiments 5, 6, 10)

- **Experiment 5:** RPi programmed via Python (GPIO, I2C BMP280/MPU6050, UART with ESP32) → RPi used as IoT Gateway.
- **Experiment 6:** Docker installed on RPi, images pulled/run, Dockerfile created, containerized IoT service deployed & verified.
- **Experiment 10:** Git/GitHub version control workflow for IoT projects implemented (init, add, commit, push, pull, branch, log).

**Good luck with your IoT lab exams and viva!**

---

*Solutions based on uploaded experiment write-ups from Prof. Ujjwala N. Salunkhe, MIT ADT, Pune.*
