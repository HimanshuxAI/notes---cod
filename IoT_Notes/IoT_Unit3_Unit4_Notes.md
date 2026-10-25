# IoT Study Notes — Unit 3 & Unit 4

**Course:** 23CSE3013 — Internet of Things  
**Instructor:** Prof. Ujjwala N. Salunkhe, Asst. Professor, Dept. of CSE (core), MIT ADT University, Pune  
**Source:** `Unit_3_IoT.pptx` (IoT Communication Protocols) & `Unit_4_IoT.pptx` (End Nodes & Gateways for IoT)

---

## UNIT 3 — IoT Communication Protocols

### Outline / Classification
Communication protocols are technologies responsible for establishing communication between IoT devices, networks, and remote infrastructures. They map to the top 3 layers of the OSI model (Application, Presentation, Session). They are classified into **6 groups**:

| # | Protocol Group | Examples |
|---|----------------|----------|
| 1 | Infrastructure protocols | IPv6, LOADng, RPL, 6LoWPAN, QUIC, uIP, nanoIP, CCN |
| 2 | Discovery protocols | Physical web, mDNS, UPnP |
| 3 | Data protocols | MQTT, MQTT-SN, CoAP, AMQP, XMPP, REST, WebSocket |
| 4 | Identification protocols | EPC, µCode, URIs |
| 5 | Device management protocols | TR-069, OMA-DM |
| 6 | Semantic protocols | JSON-LD, Web of Things (WoT) |

---

### 1. Infrastructure Protocols

#### IPv6
- Developed by IETF to address IPv4's scalability and IoT resource limitations.
- **128-bit address** (vs IPv4's 32-bit ~4.3 billion addresses).
- **Key features:**
  - Larger addressing range (~4× more addressable bits than IPv4)
  - Simplified header structure
  - End-to-end connectivity (globally unique addresses, no NAT)
  - Auto-configuration (stateless & stateful; works without DHCP)
  - Faster packet forwarding (optional fields moved to end of header)
  - Inbuilt security (IPSec)
  - Anycast support (packet sent to nearest available destination)
  - Mobility support (mobile nodes retain IP while changing location)
  - Enhanced priority support (traffic classes & flow labels)
  - Extensible headers
- **Not backward compatible** with IPv4.

#### RPL (Routing Protocol for Low-Power and Lossy Networks)
- IPv6 routing protocol using distance-vector mechanism.
- Builds a **Destination-Oriented Directed Acyclic Graph (DODAG)** — logical routing topology over a physical network.
- Best path calculated via objective function, metrics (ETX, path latency), and constraints (link encryption, battery-operated nodes).
- A node can join multiple RPL instances (graphs) and take multiple roles (leaf node, router).
- **Global vs Local instances:** global = coordinated, multiple DODAGs, long lifetime; local = single DODAG.

#### 6LoWPAN (IPv6 over Low-Power Wireless Personal Area Networks)
- IPv6 adaptation for WPAN (IEEE 802.15.4, 2.4 GHz).
- Makes small devices IP-enabled; low cost, short-range, low memory, low bit rate.
- **Specs:** ~200 m outdoor range, 200 kbps max data rate, ~100 max nodes, mesh network (self-healing).
- Uses **AES-128 link-layer security** (128-bit block cipher).
- Supports sleep mode for leaf nodes (battery saving), one-to-many and many-to-one routing.
- **Disadvantages:** less secure than Zigbee, lower interference immunity than Wi-Fi/Bluetooth, short range without mesh.
- **Applications:** home automation, smart agriculture, industrial monitoring, LED streetlights.

#### Content-Centric Networking (CCN / ICN / NDN)
- Communication based on **uniquely named data** rather than location/address.
- Anchorless, supports mobility, in-network caching → efficiency, scalability, robustness in constrained networks.
- Forwarder uses **Forwarding Information Base (FIB)** with longest-prefix hierarchical matching to route named requests.
- Security of data (not just the communication channel).
- Users access cached content from trusted content servers.

---

### 2. Discovery Protocols

#### Physical Web (Google)
- Tags real-world objects by broadcasting a list of **URLs** within short range (BLE beacons).
- Built on **Bluetooth Low Energy (BLE)** using the **Eddystone** protocol spec.
- Chosen for ubiquity, efficiency, multi-year battery life.
- Users interact passively (notifications when beacon nearby) or actively (search apps like Google Search).
- Extends web security model (HTTPS, secure login, domain obfuscation).
- Examples: smart buses (route info), smart appliances (usage tutorials), self-diagnostic robots, smart pet tags.

#### Multicast DNS (mDNS)
- IETF Zeroconf effort; DNS-like operation within local networks **without a traditional DNS server**.
- Operates on **UDP port 5353**; used with **DNS-SD** (Service Discovery).
- Each client maintains its own name↔IP list; unknown addresses trigger a multicast query; best answer is cached by all.
- Works at **link-local level** (routers do not forward mDNS packets).
- Reserved top-level domain: **`.local`** (e.g., `Mycomputer.local.`, `c.printing.local.`).
- Implementations: Apple Bonjour, Windows 10 networked printer discovery.
- **Drawback:** hostname resolution limited to top-level domain.

#### Universal Plug and Play (UPnP)
- Devices on the same LAN discover each other and auto-connect via TCP/IP, HTTP, UDP, XML, DHCP.
- Zero-configuration; ports auto-forwarded; OS/language/network independent.
- Targets home, proximity, and small-business networks.
- Device can dynamically join a network, obtain IP, announce name, convey capabilities, learn about others, and leave cleanly.
- **Security risk:** malware-infected devices can establish connections → enables DDoS attacks.

---

### 3. Data Protocols

#### MQTT (Message Queue Telemetry Transport)
- Open-standard, application-layer, **publish/subscribe** messaging transport over TCP/IP (or WebSocket).
- Asynchronous, small transport overhead, payload-agnostic, abnormal-disconnection notification.
- **Core terms:**
  - **Broker (Server):** accepts messages from clients, delivers to interested clients by topic.
  - **Client:** publishes to / subscribes to topics.
  - **Topic:** namespace for messages; supports wildcard filters.
  - **Publish / Subscribe / Unsubscribe.**
- **QoS levels:**
  1. **At most once** (best effort; message loss OK — e.g., ambient sensor data)
  2. **At least once** (assured delivery; duplicates possible)
  3. **Exactly once** (assured exactly-once delivery — e.g., billing systems)
- **Keep Alive:** max interval between control packets (client's responsibility).
- Broker persists messages for offline subscribers (in some configs).

#### CoAP (Constrained Application Protocol)
- Specialized web transfer protocol for **constrained nodes** (low-power sensors/actuators) and **constrained networks** (low-power, lossy).
- RFC 7252; based on **RESTful architecture** (request/response; GET, PUT, POST, DELETE over URLs).
- Runs over **UDP** with optional reliability (retransmission), unicast + multicast.
- Features: M2M communication, DTLS security, async exchange, low header overhead, URL/content-type support, resource discovery at `/.well-known/core`.
- **Observe flag:** server streams state changes to clients (no polling).
- **MQTT vs CoAP:** MQTT = one-to-many pub/sub (multiple interested nodes); CoAP = commands among nodes (request/response). CoAP prioritized when QoS with confirmable messages, multicast support, or very low overhead/simplicity is needed.

#### AMQP (Advanced Message Queuing Protocol)
- Publish/subscribe from the financial services sector; robust, supports transactions.
- **Heavy protocol** meant for backend IT systems, not the network edge.
- Components: **Exchange** (routes publisher messages), **Message Queue** (stores messages), **Binding** (connects queue to exchange).

#### XMPP (Extensible Messaging and Presence Protocol)
- Originally Jabber; XML-based message-oriented middleware for IM, presence, VOIP, file transfer, smart grid, social networks, IoT.
- **Client-server** (peers cannot talk directly; routed through XMPP server).
- Decentralized (anyone can host a server).
- Every user has a **JID** (`user@domain.com/resource`); resources prioritized by numerical ID.
- **vs MQTT:** XMPP defines message format (structured data, validation), builds device identity (JID), supports federation, scales easily; MQTT is lighter for memory-constrained M2M, has flexible QoS levels.

#### HTTP (REST/JSON)
- Connectionless client/server protocol; focus in IoT is **REST** (stateless, scalable).
- Resource = device + its data; RESTful services enable interoperability.
- Data formats: HTML, JS, JSON, XML (IoT standardizes around **JSON over HTTP** — lighter than XML).
- **Methods:** GET (read), POST (create), PUT (update/create), DELETE (remove).
- **Six REST constraints:** Statelessness, Uniform Interface, Cacheability, Client–server, Layered System, Code on Demand.

#### WebSocket
- IETF-standardized **full-duplex** OSI Layer 7 protocol over a single TCP connection (ports 80/443, HTTP-compatible).
- After an HTTP upgrade handshake, client/server exchange messages freely over a persistent open connection (server can push without client request).
- No continuous polling; message-based (frames, binary or text).

---

### 4. Identification Protocols

#### EPC (Electronic Product Code)
- Universal identifier for all physical objects; defined by EPCglobal Tag Data Standard.
- Official representation = **pure identity URI** (a URI).
- Supports tag-encoding URI formats, binary EPC storage, encoding/decoding rules, barcode coding schemes.
- Supports EPC identifiers, general identifiers, and 7 GS1 Application Identifier keys.
- Technology-agnostic (works with passive RFID, barcodes, etc.).

#### µCode
- Japanese µID Center system; uniquely tags real-world objects/things.
- **128-bit codes** → 3.4 × 10³⁸ unique codes.
- Application & technology independent (RFID, barcodes, matrix codes, print tags, acoustic tags, active RF tags, active IR tags, passive RFID tags).
- Architecture: µCode, µCode tags, ubiquitous communicators, µCode resolution server, µCode information server.
- Reading process: tag read (e.g., phone camera) → inquiry to resolution server → server returns source info → communicator acquires content/service info.
- Identifies **individual objects** (not product types); avoids identifier reuse; µTRON security framework adds privacy protection.

---

### 5. Device Management Protocols

#### TR-069 / CWMP
- Broadband Forum technical report for remote management of Customer Premises Equipment (CPE) over IP.
- Auto-configuration via **Auto Configuration Servers (ACS)**.
- SOAP/HTTP-based, bi-directional, text-based.
- Functions: software/firmware management, status & performance reports, diagnostics, auto-configuration.
- CPE = routers, gateways, set-top boxes, VoIP devices.
- Session initiated by CPE via "Inform" message; ACS replies "Inform response"; commands via HTTP/HTTPS; authentication via shared secret key + HTTPS certificate verification.

#### OMA-DM (Open Mobile Alliance Device Management)
- Remote management of mobile devices (phones, tablets); for constrained devices (limited bandwidth/memory/storage/processing).
- Functions: provisioning, configuration, software upgrades, fault management.
- Data exchange via **SyncML** (XML subset); transports: USB, RS-232, GSM, CDMA, Bluetooth over WAP/HTTP/OBEX.
- Server initiates asynchronously (WAP push/SMS notification); client executes and replies; built-in authentication.

---

### 6. Semantic Protocols

#### JSON-LD (JSON for Linked Data)
- Lightweight JSON-based encoding of linked data; converts legacy JSON to linked data.
- Human-readable, REST-friendly, unstructured-data suitable.
- Adds an **RDF** layer over JSON; built to be contextual (ontology-based tagging, language tags, predefined groups).
- Context embeddings direct or via HTTP link headers.
- Enables a network of machine-readable, standardized data over the Web.

#### Web of Things (WoT)
- W3C-driven interoperability initiative to unify "Web of pages" into "Web of Things."
- Gives IoT devices URLs over the Web; common syntactic vocabulary & API.
- **Sub-components:**
  - **Integration Patterns:** direct connectivity, gateway-based connectivity, cloud-based connectivity.
  - **Web Things (WT) Requirements:** guidelines for constraints & protocol implementation (a compliant web server = a Web Thing).
  - **Web Thing Model:** RESTful web protocol with defined payload syntax, data models, resources; fully compliant = Extended WoT model.

---

## UNIT 4 — End Nodes & Gateways for IoT

### Contents
1. ESP32 & ESP8266
2. NodeMCU Modes (STA / AP / STA+AP)
3. Introduction to Raspberry Pi
4. Raspberry Pi GPIO pins
5. Programming (Python / WiringPi)
6. Communication Channels on RPi (SPI, I2C, UART)
7. Sensors & Actuators (Ultrasonic, DS18B20, IR, PIR, ADXL345, MPU6050, Servo, LCD)

---

### 1. ESP32 & ESP8266

#### ESP32 (Espressif Systems)
- Low-cost, low-power SoC with **Wi-Fi + dual-mode Bluetooth**.
- Dual-core or single-core **Tensilica Xtensa LX6** up to **240 MHz**.
- Built-in: antenna switches, RF balun, power amplifier, LNA, filters, power management, touch pins, hall effect sensor, temperature sensor.
- Popular module: **ESP32-WROOM-32** (ESP32-D0WDQ6 chip).
- **Price:** ~₹300 / $6–$12.
- Two cores controllable separately; variable frequency 80–240 MHz; ultra-low-power co-processor monitors peripherals while main cores are off.

#### ESP32 Pinouts
- **Supply pins:** two 5V and 3.3V pins; **GND:** 3 pins.
- **ADC:** 16 pins (some with internal amplifier for precision small-voltage measurement).
- **DAC:** two 8-bit DACs.
- **Touchpads:** 10 capacitive-touch-sensitive pins.
- **SPI:** two interfaces (displays, SD/microSD, external flash).
- **I2C:** SDA + SCL pins.
- **UART:** two interfaces, up to 5 Mbps; UART0 has CTS/RTS.
- **EN pin:** HIGH = enable, LOW = disable.
- **GPIO:** 32 pins (GPIO6–11 reserved for internal flash SPI — not recommended for use); almost all support PWM.
- Pull-up/pull-down configurable internally.

#### ESP32 Power Modes
| Mode | Active Parts | Current Consumption |
|------|-------------|---------------------|
| Active | Wi-Fi + Bluetooth TX/RX | 80–260 mA |
| Processor only (Wi-Fi/BT off) | CPU | 3–20 mA |
| Deep sleep (RTC + ULP on) | RTC unit + ULP processor | ~0.8 mA |
| RTC only | RTC unit (Wi-Fi/BT data stored in RTC memory) | 10–150 µA |
| Hibernation (RTC timer + some I/O) | RTC timer only | ~2.5 µA |

#### ESP32 Advantages / Disadvantages
- **Pros:** successor to ESP8266, low cost, ultra-low power (clock gating, multiple power modes, dynamic power scaling), more GPIOs than ESP8266.
- **Cons:** slightly more expensive than ESP8266 ($6–$12 vs $4–$6).
- **Projects:** smart home, sensor-based projects, ESP32 weather station shield, barometric sensor, data logging (temp → MicroSD), ESP32 Access Point web server.

#### ESP8266 (ESP-12E / NodeMCU)
- **Tensilica Xtensa 32-bit LX106 RISC** at 80–160 MHz, RTOS support.
- **128 KB RAM, 4 MB Flash.**
- 802.11b/g/n HT40 Wi-Fi transceiver; can join a network OR create its own (AP mode).
- **Power:** 3V–3.6V operating range; onboard LDO regulator → steady 3.3V, up to 600 mA (ESP pulls ~80 mA during RF); powered via Micro-B USB or VIN (regulated 5V).
- **17 GPIO pins** with: 10-bit ADC, UART (serial flashing), PWM, SPI, I2C, I2S (sound).
- **Buttons:** RST (reset) and FLASH (firmware download); programmable LED on D0.
- **Serial:** CP2102 USB-to-UART bridge (Silicon Labs).
- **Pros:** low cost, reliable, easily available.
- **Cons:** early documentation was in Mandarin (community translations now available).
- **Projects:** geolocation tracking, wireless web server, railway-track pressure sensors (animal alarm), smart plugs, humidity/temp monitoring, personal assistant (Siri/Alexa-style).

#### Comparison: ESP32 vs ESP8266
| Feature | ESP32 | ESP8266 |
|---------|-------|---------|
| Cores | Dual/single core (up to 240 MHz) | Single core (80–160 MHz) |
| Connectivity | Wi-Fi + Bluetooth (dual-mode) | Wi-Fi only |
| GPIOs | More (32) | Fewer (17) |
| Power | Ultra-low power modes | Higher consumption |
| Price | $6–$12 | $4–$6 |

---

### 2. NodeMCU Modes (ESP Wi-Fi Modes)

ESP devices can operate as:
- **STA (Station) mode:** connects to existing Wi-Fi as a client (like phone/laptop); accesses internet & local devices.
- **AP (Access Point) mode:** creates its own Wi-Fi network; other devices connect directly to ESP; ESP not connected to internet (local subnet only).
- **STA + AP mode:** ESP connects to an existing network as client while simultaneously hosting its own network; acts as intermediary between networks.

#### Station Mode (Arduino)
```cpp
#include <ESP8266WiFi.h>
const char* ssid = "SSID";
const char* password = "PASSWORD";
void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(1000); Serial.print("."); }
  Serial.println("Connection established!");
  Serial.print("IP address: "); Serial.println(WiFi.localIP());
}
void loop() {}
```
- Serial Monitor shows IP (e.g., `192.168.1.3`); can be pinged if local network is online.

#### Access Point Mode
```cpp
#include <ESP8266WiFi.h>
const char *ssid = "Voyager31";
const char *password = "DivideByZero";
void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  Serial.print("IP address: "); Serial.println(WiFi.softAPIP());
}
```
- Default AP IP: `192.168.4.1`. Devices can ping each other on the same AP subnet but cannot reach the internet unless ESP also has STA connection.

#### AP + STA Mode
```cpp
WiFi.mode(WIFI_AP_STA);
WiFi.softAP(AP_SSID, AP_PASS);
WiFi.begin(WIFI_SSID, WIFI_PASS);
```
- Prints both IPs (station network IP and AP IP).

---

### 3. Introduction to Raspberry Pi

- **Raspberry Pi** = most popular SBC (Single Board Computer); runs an **OS** (unlike Arduino IDE-programmed platforms).
- Raspberry Pi 3 supports OS programming; does nearly everything a desktop can do.
- OS = bridge between user and hardware; manages CPU, memory, disks, printers, UI, application services.
- Official OS: **Raspbian** (Raspberry Pi OS); alternatives available.
- Models covered: Pi 3 Model B (40-pin header J8, 28 GPIOs) and Pi 4.

---

### 4. GPIO Pins

- GPIO = General Purpose Input/Output; connect RPi to general-purpose I/O devices via 40-pin male header.
- **Two numbering systems:**
  - **GPIO (BCM) numbering:** refers to Broadcom SoC pin numbers (requires pin mapping).
  - **Physical (BOARD) numbering:** refers to physical pin position on the 40-pin P1 header.
- **GPIO capabilities:**
  - **PWM:** software PWM on all pins; hardware PWM on GPIO12, 13, 18, 19.
  - **SPI:** SPI0 (MOSI GPIO10, MISO GPIO9, SCLK GPIO11, CE0 GPIO8, CE1 GPIO7); SPI1 (MOSI GPIO20, MISO GPIO19, SCLK GPIO21, CE0 GPIO18, CE1 GPIO17, CE2 GPIO16).
  - **I2C:** Data GPIO2, Clock GPIO3; EEPROM Data GPIO0, EEPROM Clock GPIO1.
  - **Serial:** TX GPIO14, RX GPIO15.

---

### 5. Programming (RPi.GPIO & WiringPi)

#### RPi.GPIO (Python)
- Already installed on Raspbian; `pip install RPi.GPIO` for manual install.
- `GPIO.setmode(GPIO.BCM)` or `GPIO.setmode(GPIO.BOARD)`
- `GPIO.setup(channel, GPIO.OUT / GPIO.IN [, initial=...] [, pull_up_down=GPIO.PUD_UP])`
- `GPIO.output(channel, GPIO.HIGH / GPIO.LOW)`
- `GPIO.input(channel)`

**Example — LED controlled by switch (Python):**
```python
import RPi.GPIO as GPIO
LED = 32          # BOARD pin (GPIO18 BCM)
Switch_input = 29 # BOARD pin (GPIO27 BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(Switch_input):
        GPIO.output(LED, GPIO.LOW)
    else:
        GPIO.output(LED, GPIO.HIGH)
```

#### WiringPi (C library)
- Easy GPIO access; similar to Arduino Wiring; supports UART, SPI, I2C, PWM.
- **Example — LED with switch (C):**
```c
#include <wiringPi.h>
#include <stdio.h>
int LED = 26;          // WiringPi GPIO26 = BCM GPIO12 = pin 32
int switch_input = 21; // WiringPi GPIO21 = BCM GPIO5 = pin 29
int main() {
  wiringPiSetup();
  pinMode(LED, OUTPUT);
  pullUpDnControl(switch_input, PUD_UP);
  while (1) {
    if (digitalRead(switch_input))
      digitalWrite(LED, LOW);
    else
      digitalWrite(LED, HIGH);
  }
}
```
- **Blinking LED (Python + WiringPi):**
```python
import wiringpi, time
ledPin = 6
wiringpi.wiringPiSetup()
wiringpi.pinMode(ledPin, 1)
while True:
    wiringpi.digitalWrite(ledPin, 1); time.sleep(1)
    wiringpi.digitalWrite(ledPin, 0); time.sleep(1)
```

---

### 6. Communication Channels on RPi

RPi communicates externally via: **GPIO (digital), SPI, I2C, UART.**

#### SPI (Serial Peripheral Interface)
- Developed by Motorola (1979); synchronous, short-distance, 1 bit at a time, full-duplex.
- **Master** dictates clock; **Slave** follows. Pi 4 has **7 SPI buses**.
- Lines: MOSI, MISO, SCLK, CS/SS (active low).
- **4 modes** from clock polarity (CPOL: 0=LOW idle, 1=HIGH idle) and clock phase (CPHA).
- **Pros:** full-duplex, high speed, good signal integrity, simple hardware.
- **Cons:** more pins than I2C, no formal standard, typically one master, no hardware slave acknowledgment.
- Enable: `sudo raspi-config`; install: `sudo apt-get install python3-spidev`.

#### I2C (Inter-Integrated Circuit / TWI)
- 2-wire serial bus: **SDA** (data) + **SCL** (clock).
- Acknowledgment-based; master/slave modes; 7-bit or 10-bit device addresses.
- Open-drain configuration → needs **pull-up resistors** on SDA/SCL.
- Used for: RTC, external EEPROM, gyro, magnetometer, sensor modules.
- **I2C vs SPI:**
  - Use **I2C** when: many low-speed sensors, few GPIOs, devices support I2C only.
  - Use **SPI** when: high-speed needed, full-duplex, precise timing important.

#### UART (Universal Asynchronous Receiver/Transmitter)
- Hardware for serial communication between **two** devices (TX + RX wires).
- Converts bytes to bits; packets = start bit + data frame + parity bit + stop bit(s).
- Receiver checks parity for errors, strips start/stop/parity bits, rebuilds byte in UART buffer.
- Bit errors caused by distance, magnetic radiation, baud-rate mismatch.

#### Analog Read (RPi has no native ADC)
- RPi GPIOs read only digital (HIGH 3.3V / LOW 0V).
- Need external ADC via **I2C or SPI**:
  - **MCP3008:** 8-channel, 10-bit, SPI (precision similar to Arduino Uno).
  - **ADS1115:** 4-channel, 16-bit, I2C.
- Reference 3.3V / 1024 units → each unit ≈ 3.22 mV.

**MCP3008 SPI Python example:**
```python
import spidev, time
spi = spidev.SpiDev(); spi.open(0, 0)
def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((r[1] & 3) << 8) + r[2]
while True:
    reading = analog_read(0)
    voltage = reading * 3.3 / 1024
    print("Reading=%d\tVoltage=%f" % (reading, voltage))
    time.sleep(1)
```

---

### 7. Sensors & Interfacing (with Python code examples)

#### Ultrasonic Sensor (HC-SR04 style)
- Trig pin sends 10 µS pulse; measures echo duration; `distance = pulse_duration × 34300 / 2` (cm) or `× 17150`.
- GPIO BCM: TRIG 11, ECHO 18 (example).

#### DS18B20 Temperature Sensor (1-Wire)
- Install: `sudo pip3 install w1thermsensor`, `sudo apt install libgpiod2`.
- Enable **1-Wire interface** via Raspberry Pi Configuration → Interfaces; reboot.
- Code:
```python
import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
while True:
    temperature = sensor.get_temperature()
    print("The temperature is %s celsius" % temperature)
    time.sleep(1)
```

#### IoT-based Temperature Monitor (Dataplicity)
1. Get code from Dataplicity website; paste into Pi terminal to activate remote shell.
2. Click "Done" on website; log in with Pi credentials.
3. Run: `sudo python temperature.py`
- Stack: Raspberry Pi + DS18B20 + Dataplicity remote access.

#### IR Sensor
- Sensor on GPIO 16, buzzer on GPIO 18 (BOARD); beep + "Object Detected" when IR triggered.

#### PIR Motion Sensor
- PIR input GPIO 29, LED GPIO 32 (BOARD); LED on when motion detected.

#### ADXL345 Accelerometer (I2C)
- Enable I2C; install `python3-dev python3-pip python3-smbus i2c-tools`; `sudo i2cdetect -y 1`.
- Adafruit ADXL345 library over I2C (board SCL/SDA); prints acceleration x, y, z.

#### MPU6050 (Accelerometer + Gyro + Temp)
- I2C address `0x68`.
- **Method A (mpu6050 library):** `sensor.get_accel_data()`, `get_gyro_data()`, `get_temp()`.
- **Method B (smbus direct registers):** init registers (PWR_MGMT_1 0x6B, SMPLRT_DIV 0x19, CONFIG 0x1A, GYRO_CONFIG 0x1B, INT_ENABLE 0x38); read 16-bit raw values from ACCEL/GYRO X/Y/Z OUT H (0x3B, 0x3D, 0x3F, 0x43, 0x45, 0x47); scale: accel /16384.0, gyro /131.0.

#### Servo Motor (PWM)
- Converts electrical → mechanical energy; rotates to a **specified angle** (not continuous 360°); position controlled via PWM.
- Range typically 0–180°.
- **SG90 (Tower Pro):** small, lightweight, 180° (90° each direction), 3 wires (GND, signal, power).
- **MG996R:** high-torque digital, 120° (60° each direction); similar duty cycle/PWM period.
- **Pi control (50 Hz PWM on GPIO 11 / BOARD):**
```python
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm = GPIO.PWM(11, 50)   # 50 Hz
pwm.start(0)
pwm.ChangeDutyCycle(5)   # left -90°
sleep(1)
pwm.ChangeDutyCycle(7.5) # neutral
sleep(1)
pwm.ChangeDutyCycle(10)  # right +90°
sleep(1)
pwm.stop(); GPIO.cleanup()
```

#### LCD (16×2 Character LCD)
- 16 columns × 2 rows; each char 5×10 pixels (50 pixels); Hitachi HD44780 driver-compatible.
- Variants: 16×1, 16×4.
- **Direct GPIO wiring** (RS D26, EN D19, D7 D27, D6 D22, D5 D24, D4 D25, backlight D4) using `adafruit-circuitpython-charlcd`.
- **I2C interface:** VCC→5V (pin 4), GND→GND (pin 6), SDA→GPIO2 (pin 3), SCL→GPIO3 (pin 5).
- Enable I2C modules: add `i2c-bcm2835`, `i2c-bcm2708`, `i2c-dev` to `/etc/modules`; `sudo reboot`; `sudo i2cdetect -y 1` (backpack usually at `0x27` or `0x3F`).

---

### Exam/Study Tips
- **Unit 3:** Memorize the 6 protocol groups with examples; MQTT pub/sub model, QoS levels, broker/client/topic; CoAP REST methods + observe; differences MQTT vs CoAP vs XMPP vs HTTP; IPv6 features; RPL/DODAG; 6LoWPAN specs; mDNS `.local`; TR-069 CWMP; OMA-DM SyncML; JSON-LD & WoT.
- **Unit 4:** ESP32 vs ESP8266 specs; STA/AP/AP+STA modes and code; RPi GPIO numbering (BCM vs BOARD) and pin functions; SPI/I2C/UART characteristics; RPi.GPIO functions; each sensor's interfacing steps and key code; servo duty-cycle angles (5% = -90°, 7.5% = neutral, 10% = +90°).

---

**Source files:** `Unit_3_IoT.pptx` (99 slides) & `Unit_4_IoT.pptx` (119 slides), extracted text compiled into these notes.
