# UNIT III — IoT COMMUNICATION PROTOCOLS

**Course:** 23CSE3013 – Internet of Things  
**Class:** T.Y. B.Tech CSE (AIEC), SEM-I  
**Institution:** MIT Art, Design and Technology University, MIT School of Computing, Pune  
**Professor:** Prof. Ujjwala N. Salunkhe  
**Academic Year:** 2025-2026 SEM-I  

---

# TABLE OF CONTENTS

1. [Introduction to IoT Communication Protocols](#1-introduction-to-iot-communication-protocols)
2. [Classification of IoT Protocols](#2-classification-of-iot-protocols)
3. [Infrastructure Level Protocols](#3-infrastructure-level-protocols)
   - [IPv6](#ipv6)
   - [RPL](#rpl-routing-protocol-for-low-power-and-lossy-networks)
   - [6LoWPAN](#6lowpan-ipv6-over-low-power-wireless-personal-area-networks)
   - [CCN (Content-Centric Networking)](#ccn-content-centric-networking)
4. [Discovery Protocols](#4-discovery-protocols)
   - [Physical Web](#physical-web)
   - [mDNS (Multicast DNS)](#mdns-multicast-dns)
   - [UPnP (Universal Plug and Play)](#upnp-universal-plug-and-play)
   - [DNS and ARP/RARP](#dns-and-arrarp)
5. [Data Protocols](#5-data-protocols)
   - [MQTT](#mqtt-message-queue-telemetry-transport)
   - [CoAP](#coap-constrained-application-protocol)
   - [AMQP](#amqp)
   - [XMPP](#xmpp)
   - [WebSocket](#websocket)
   - [HTTP (REST/JSON)](#http-restjson)
6. [Identification Protocols](#6-identification-protocols)
7. [Device Management Protocols](#7-device-management-protocols)
8. [Semantic Protocols](#8-semantic-protocols)
9. [Quick Revision Cheat Sheet](#9-quick-revision-cheat-sheet)
10. [Exam Questions — Model Answers](#10-exam-questions--model-answers)

---

# 1. INTRODUCTION TO IOT COMMUNICATION PROTOCOLS

## 1.1 What are IoT Communication Protocols?

IoT protocols are a set of rules suitable for IoT applications to ensure that data sent from an IoT device gets read and understood by another device. IoT protocols are needed because:

- IoT devices and services over the Internet form a broad range of applications
- Internet Protocol (IP) is typically used for connecting IoT devices to the Internet
- Different IoT devices and their applications require different application-layer protocols
- Protocols need to ensure optimum security of exchanged information between connected devices

## 1.2 Why Different Protocols?

Different protocols exist because:
- Some protocols are designed for fast and reliable business transactions
- Some are optimized for data collection such as sensor updates in constrained networks
- Some are suitable for Instant Messaging (IM) and online presence detection
- Each protocol has its own advantages and disadvantages when dealing with different IoT scenarios

---

# 2. CLASSIFICATION OF IOT PROTOCOLS

IoT communication protocols are aligned with the top 3 layers of the OSI reference architecture: **Application, Presentation, and Session layer**. They can be classified into **6 groups**:

| # | Protocol Category | Examples |
|---|------------------|----------|
| 1 | **Infrastructure Protocols** | IPv6, RPL, 6LoWPAN, CCN |
| 2 | **Discovery Protocols** | Physical Web, mDNS, UPnP |
| 3 | **Data Protocols** | MQTT, CoAP, AMQP, XMPP, WebSocket, HTTP (REST/JSON) |
| 4 | **Identification Protocols** | EPC, URIs, μCode |
| 5 | **Device Management Protocols** | TR-069, OMA-DM |
| 6 | **Semantic Protocols** | JSON-LD, Web of Things (WoT) |

---

# 3. INFRASTRUCTURE LEVEL PROTOCOLS

Infrastructure protocols are protocols which are hugely dependent on the network and the network infrastructure.

## 3.1 IPv6 (Internet Protocol version 6)

IPv6 was developed by IETF (Internet Engineering Task Force) to cope with the need of massive scalability and limited resources requirements of IoT, which were not possible with IPv4.

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address Length | 32 bits | 128 bits |
| Address Space | ~4.3 billion | ~340 undecillion |
| Address Notation | Decimal (192.168.1.1) | Hexadecimal (2001:db8::1) |
| Header Complexity | Complex | Simplified |
| Security | Optional (added later) | Built-in (IPSec) |
| Auto-configuration | DHCP required | Stateless/Stateful auto-config |
| NAT Required | Yes | No |

### Key Features of IPv6:

1. **Larger Addressing Range:** IPv6 has roughly 4 times more addressable bits than IPv4, accommodating address requirements for any number of connected devices.

2. **Simplified Header Structure:** Although bigger than IPv4, the IPv6 header has seldom-used optional fields at the end, making routing decisions faster.

3. **End-to-End Connectivity:** Globally unique addresses enable packets to reach destination nodes directly without Network Address Translation (NAT).

4. **Auto-configuration:** Addresses are automatically configured (stateless and stateful methods), working even without DHCP servers.

5. **Faster Packet Forwarding:** Fewer fields to check in the header means faster routing decisions.

6. **Inbuilt Security (IPSec):** IPv6 supports inbuilt security mechanisms which IPv4 does not directly support.

7. **Anycast Support:** Multiple interfaces assigned the same IPv6 address globally; routers send packets to the nearest available destination.

8. **Mobility Support:** Mobile nodes can retain IP addresses and remain connected while changing geographic areas.

9. **Enhanced Priority Support:** Traffic classes and flow labels determine efficient routing paths.

10. **Extensibility of Headers:** The options part of an IPv6 header can be extended by adding more information; not limited in size.

**Note:** IPv6 is not backward compatible with IPv4 applications directly.

---

## 3.2 RPL (Routing Protocol for Low-power and Lossy Networks)

RPL stands for Routing Protocol for Low-power and Lossy networks (LLN) and is designed for IPv6 routing. It follows a distance vector based routing mechanism.

### Key Concepts:

- **DODAG (Destination-Oriented Directed Acyclic Graph):** A logical routing topology built over a physical network, formed based on an objective function and network metrics.

- **Objective Function:** Dictates rules for the formation of the DODAG, using a set of metrics and constraints to calculate the optimum path.

- **Metrics in RPL:** Expected Transmission Values (ETX), path latencies, and others. Metrics are either minimized or maximized.

- **Constraints in RPL:** Encryption of links, presence of battery-operated nodes, etc. Constraints need to be minimized.

### RPL Operation:

- A single node in the mesh network may have multiple objective functions due to different network traffic path quality requirements.
- RPL supports QoS-aware and constraint-based routing.
- RPL nodes can simultaneously take on multiple network roles: leaf node, router, and others.

### RPL Instances:

| Type | Characteristics |
|------|----------------|
| **Global RPL Instances** | Coordinated behavior, possibility of more than one DODAG, long lifetime |
| **Local RPL Instances** | Single DODAGs, root associated directly with DODAG-ID |

**RPL Instance ID:** Allocated collaboratively and unilaterally, divided between global and local instances. RPL control and data messages are tagged with RPL instance IDs to avoid ambiguity.

---

## 3.3 6LoWPAN (IPv6 over Low Power Wireless Personal Area Networks)

6LoWPAN is an IPv6 protocol extended from IPv6 over Low Power Personal Area Network (WPAN).

### Key Features:

- Works on Wireless Personal Area Network (WPAN), i.e., IEEE 802.15.4 chips and radios
- Proposed standard based on IETF RFC 4944
- Designed for devices with very low cost, short-range, low memory usage, and low bit rate
- Makes individual nodes IP-enabled
- Can interact with 802.15.4 devices and other types of devices (e.g., Wi-Fi) on an IP network
- Uses AES 128 link layer security (block cipher with key size of 128/192/256 bits)
- Requires sleep mode for battery saving
- Minimal memory requirement
- Lowered routing overhead

### 6LoWPAN Specifications:

| Parameter | Value |
|-----------|-------|
| Frequency Band | 2.4 GHz (IEEE 802.15.4) |
| Outdoor Range | ~200 m (maximum) |
| Data Rate | 200 kbps (maximum) |
| Maximum Nodes | ~100 |
| Network Type | Mesh network (robust, scalable, self-healing) |

### Advantages:
- One-to-many and many-to-one routing
- Low-cost and secure communication in IoT devices
- Uses IPv6, can be directly routed to cloud platforms
- Leaf nodes can be in sleep mode for longer durations

### Disadvantages:
- Comparatively less secure than Zigbee
- Lesser immunity to interference than Wi-Fi and Bluetooth
- Without mesh topology, supports short range
- Only allows smaller devices with very limited processing ability to establish communication using IPv6

### Applications:
- Home automation
- Smart agricultural techniques
- Industrial monitoring
- IPv6 packet transmission on networks with constrained power and reliability resources

---

## 3.4 CCN (Content-Centric Networking)

CCN is more commonly known as Information-Centric Networking (ICN). Other names include Named Data Networking (NDN) and Publish-Subscribe Networking (PSIRP).

### Key Concepts:

- CCN enables communication by defining and adhering to the concept of **uniquely named data**
- Unlike conventional networking approaches, CCN is independent of location, application, and storage requirements
- CCN is anchorless, enabling mobility and focuses on **in-network caching** for operations
- Extends features of data and communication efficiency, enhances scalability and robustness even in constrained networks

### How CCN Works:

- Users access cached content from multiple content generating sources by accessing data from trusted content servers (security of data, not communication channel)
- A forwarder checks a named request through hierarchical prefix matching (typically longest prefix match) with a Forwarding Information Base (FIB)
- FIB matching at each CCN router stores information in a table updated by a routing mechanism
- Although path segments and names are theoretically unbounded, they are restricted by the routing protocol used for practical reasons

---

# 4. DISCOVERY PROTOCOLS

Discovery protocols focus on the discovery of services and logical addresses.

## 4.1 Physical Web

Proposed by Google, the basic idea of Physical Web is to tag real-world objects. The Physical Web broadcasts a list of URLs within a short radius around it so that anyone in range can see available URLs and interact with them.

### How It Works:
- URLs could lead to web pages or web apps, opening infinite possibilities
- Built primarily upon **Bluetooth Low Energy (BLE)**, used to broadcast content as beacons
- BLE was chosen for its ubiquity, efficiency, and extended battery life (several years)
- Supporting beacons must support the **Eddystone protocol** specification

### Features:
- URLs are core principles of the web and can be flexible or decentralized
- Allow any application to have a presence on the web, enabling digital presence of objects
- Integrated with web security model: secured login, HTTPS, domain obfuscation
- Typical listeners are mobile phones

### User Interaction Methods:

| Method | Description |
|--------|-------------|
| **Passive** | When a beacon is detected nearby, mobile phones show a notification notifying the user of something interesting offered nearby |
| **Active** | An app can search for beacons nearby (e.g., Google Search app) |

### Examples:
- User-friendly buses alerting users about route-related information
- Smart home appliances teaching new users how to use them
- Self-diagnostic robots and machinery in industries
- Smart pet tags providing information about the pet's owner and home location

---

## 4.2 DNS - Prerequisite for mDNS

**DNS (Domain Name System)** uses DNS servers which map host name to IP address, similar to phone books or directories mapping name to phone number.

- Easy to remember names compared to IP addresses (e.g., google.com → 192.168.0.1)
- Works by exchanging messages between client and server machines
- Client passes destination host name to DNS process to obtain IP address
- DNS is a distributed database implemented in a hierarchy of name servers
- **ARP/RARP** protocols convert IP address to MAC address and vice versa

---

## 4.3 mDNS (Multicast DNS)

mDNS is a joint effort by IETF participants, Zero Configuration Networking (zeroconf), and DNS Extensions (dnsext) working groups.

### How mDNS Works:

- Enables DNS-like operations within local networks without a traditional DNS server
- Operates on **UDP port 5353**
- Allows devices to discover each other and their services, commonly seen in IoT devices
- Every client maintains their own list of names and IP addresses
- If an unknown address is requested, a "multicast" is sent to many/all computers in the network
- Computers that have requested information reply back to the client
- Client performs another multicast with the "best" answer received
- All computers add the new entry to their local list

### mDNS vs DNS:

| Feature | DNS | mDNS |
|---------|-----|------|
| Scope | Global level | Local network level |
| Server Required | Yes (DNS server) | No (serverless) |
| Configuration | Manual/ DHCP | Zero configuration |
| Port | 53 | 5353 |

### Popular Implementations:
- Apple Bonjour service
- Networked printer discovery service in Windows 10

### Limitations:
- Host name resolution reach limited to top-level domain only

### ".local" Domain:
- IETF defines one single top level domain ".local" reserved for link-local name used in mDNS network
- Any device can generate its link local domain name (e.g., "Mycomputer.local.", "c.printing.local.", "d.printing.local.")
- If domain name ends with ".local.", message should be processed by mDNS protocol

---

## 4.4 UPnP (Universal Plug and Play)

UPnP is a service that allows devices on the same local network to discover each other and automatically connect through standard networking protocols (TCP/IP, HTTP, UDP, XML, DHCP, etc.).

### Examples of UPnP Devices:
- Printers, gaming consoles, WiFi devices, IP cameras, routers, mobile devices, Smart TVs

### Characteristics:
- Targets home networks, proximity networks, small businesses, and commercial buildings
- Enables data communication between any two devices under command of any control device on the network
- Independent of operating system, programming language, or network technology
- Offers **zero-configuration** (no human authentication required to establish connection)
- Ports are automatically forwarded when UPnP request is received

### Security Concerns:
- Zero-configuration makes it easy for infected connections to spiral out of control
- If UPnP establishes connections with malware-infected devices, **DDoS attacks** become possible

---

## 4.5 DNS and ARP/RARP

- **DNS:** Maps host names to IP addresses; distributed database in hierarchy of name servers
- **ARP (Address Resolution Protocol):** Converts IP address to MAC address
- **RARP (Reverse ARP):** Converts MAC address to IP address

---

# 5. DATA PROTOCOLS

Data protocols are directly related to access, storage, and distribution of data through IoT network. Data may be transferred between clients and servers, as well as between brokers and subscribers.

Examples: MQTT, MQTT-SN, CoAP, AMQP, XMPP, REST, WebSocket

---

## 5.1 MQTT (Message Queue Telemetry Transport)

MQTT is an open standard, application layer protocol. It is a Client/Server publish/subscribe messaging transport protocol that runs over TCP/IP, WebSocket, or other network protocols providing ordered, lossless, bi-directional connections.

### Features:
- Publish/subscribe message pattern providing one-to-many message distribution and decoupling of applications
- Messaging transport agnostic to content of payload
- Small transport overhead and minimized protocol exchanges to reduce network traffic
- Mechanism to notify interested parties when abnormal disconnection occurs

### MQTT Basic Terms:

| Term | Definition |
|------|------------|
| **Broker** | Web service that accepts messages from clients and delivers them to interested clients. Messages belong to a topic. Also called "servers." |
| **Client** | A device that publishes messages to a topic, subscribes to a topic, or both. |
| **Topic** | A namespace (place) for messages on the broker. Clients subscribe and publish to a topic. |
| **Publish** | Client sending a message to the broker using a topic name. |
| **Subscribe** | Client tells broker which topics interest it. Broker sends messages published to that topic. |
| **Unsubscribe** | Tells broker to stop sending messages on a topic. |

### MQTT Working:

- **Broker** = "Post Office" (server)
- **Clients** can publish (send letters) or subscribe (receive letters) to topics
- Clients can both publish and subscribe
- Topics can have subtopics
- Example: A wireless thermometer client publishes temperature data to topic `/sensors/temp`, and a humidity sensor client publishes to `/sensors/humid`

### MQTT Server (Broker):
- Accepts network connections from Clients
- Accepts Application Messages published by Clients
- Processes subscribe and unsubscribe requests from Clients
- Forwards Application Messages matching Client Subscriptions
- May persist Application Messages for delivery even if Subscriber is not online

### MQTT Client:
- Establishes Network Connection to the Server
- Can Publish Application Messages, Create Subscriptions, Unsubscribe, Disconnect

### MQTT Subscription:
- Comprises a **Topic Filter** and a maximum **QoS**
- Associated with a single Session
- Each Subscription within a Session has a different Topic Filter
- Topic Filter can include wildcard characters to subscribe to multiple topics at once

### MQTT Session:
- Stateful interaction between Client and Server
- Some sessions last only as long as Network Connection; others span multiple consecutive Network Connections
- Interaction controlled using **Control Packet**

### MQTT QoS Levels:

| QoS Level | Description | Use Case |
|-----------|-------------|----------|
| **At most once (0)** | Best effort delivery; message loss can occur | Ambient sensor data (lost reading not critical) |
| **At least once (1)** | Messages assured to arrive but duplicates can occur | General messaging |
| **Exactly once (2)** | Messages assured to arrive exactly once | Billing systems (duplicate/lost messages cause incorrect charges) |

### MQTT Keep Alive:
- A time interval measured in seconds, expressed as a 16-bit word
- Maximum time interval permitted between Control Packets sent by Client
- Client's responsibility to ensure interval doesn't exceed Keep Alive value

### MQTT Topic Levels:
- Topic Level Separator divides Topic Name into multiple topic levels
- Subscription's Topic Filter can contain special wildcard characters to subscribe to multiple topics at once

---

## 5.2 CoAP (Constrained Application Protocol)

### What is CoAP?

CoAP is a specialized web transfer protocol for use with constrained nodes (low power sensors and actuators) and constrained networks (low power, lossy network). It enables constrained nodes to talk with other constrained nodes over Internet. Designed for M2M applications such as smart energy, home automation, and Industrial applications.

### CoAP Characteristics:

- **Based on RESTful architecture**
- Designed for IoT devices with limited resources (embedded processors, limited RAM/ROM)
- Devices need to operate on battery without replacement for weeks, months, or years
- Needs to communicate data swiftly though small in amount but on limited network bandwidth

---

## 5.3 Other Data Protocols

| Protocol | Full Form | Description |
|----------|-----------|-------------|
| **AMQP** | Advanced Message Queuing Protocol | Open standard application layer protocol for message-oriented middleware |
| **XMPP** | Extensible Messaging and Presence Protocol | Used for instant messaging and presence information |
| **WebSocket** | - | Full-duplex communication over a single TCP connection |
| **HTTP** | HyperText Transfer Protocol | REST/JSON based communication |
| **MQTT-SN** | MQTT for Sensor Networks | MQTT variant for sensor networks |

---

# 6. IDENTIFICATION PROTOCOLS

Identification protocols deal with identification of devices and objects.

| Protocol | Description |
|----------|-------------|
| **EPC** | Electronic Product Code - unique identifier for physical objects |
| **URI** | Uniform Resource Identifier - string of characters identifying a resource |
| **µCode** | Micro Code - identification technology |

---

# 7. DEVICE MANAGEMENT PROTOCOLS

| Protocol | Description |
|----------|-------------|
| **TR-069** | CPE WAN Management Protocol - for remote management of customer-premises equipment |
| **OMA-DM** | Open Mobile Alliance Device Management - standard for device management |

---

# 8. SEMANTIC PROTOCOLS

| Protocol | Description |
|----------|-------------|
| **JSON-LD** | JSON for Linked Data - method of encoding Linked Data using JSON |
| **Web of Things (WoT)** | WoT Thing Model - standardizes how IoT devices are described and interacted with |

---

# 9. QUICK REVISION CHEAT SHEET

| Topic | Key Point |
|-------|-----------|
| **IoT Protocols** | Rules for IoT device communication; ensure data is read and understood |
| **6 Protocol Categories** | Infrastructure, Discovery, Data, Identification, Device Management, Semantic |
| **IPv6** | 128-bit address, auto-config, IPSec, no NAT, mobility support |
| **RPL** | Distance vector routing for LLNs; uses DODAG and objective function |
| **6LoWPAN** | IPv6 over 802.15.4; 2.4 GHz, 200 kbps, ~200m range, ~100 nodes, mesh |
| **CCN/ICN** | Content-centric; uniquely named data; anchorless; in-network caching |
| **Physical Web** | Google's project; BLE beacons; Eddystone; URLs broadcast nearby |
| **mDNS** | UDP port 5353; local network; ".local" domain; zero config |
| **UPnP** | Zero-config; home networks; security risk (DDoS) |
| **MQTT** | Pub/Sub; broker/client/topic; QoS 0/1/2; TCP/WebSocket |
| **CoAP** | RESTful; constrained nodes/networks; M2M applications |
| **Security** | IPv6 has IPSec; 6LoWPAN uses AES-128; UPnP has DDoS risk |

**HIGH-YIELD EXAM TOPICS:**
1. IPv6 vs IPv4 comparison
2. MQTT architecture (broker/client/topic) and QoS levels
3. 6LoWPAN features and specifications
4. mDNS vs DNS comparison
5. UPnP architecture and security concerns
6. CoAP for constrained devices

---

# 10. EXAM QUESTIONS — MODEL ANSWERS

**Q1. Explain the need for IoT protocols and classify them.**

**Answer:**
IoT protocols are needed because IoT devices and services over the Internet form a broad range of applications. Different IoT devices require different application-layer protocols to ensure data sent from one device is read and understood by another, with optimum security.

Classification (aligned with OSI top 3 layers):
1. **Infrastructure Protocols:** IPv6, RPL, 6LoWPAN, CCN — handle network infrastructure
2. **Discovery Protocols:** Physical Web, mDNS, UPnP — discover services and logical addresses
3. **Data Protocols:** MQTT, CoAP, AMQP, XMPP, WebSocket, HTTP — access, storage, distribution of data
4. **Identification Protocols:** EPC, URI, µCode — identify devices and objects
5. **Device Management Protocols:** TR-069, OMA-DM — manage devices remotely
6. **Semantic Protocols:** JSON-LD, WoT — semantic understanding of data

---

**Q2. Explain IPv6 features and why it's important for IoT.**

**Answer:**
IPv6 was developed by IETF to cope with massive scalability and limited resources of IoT, which weren't possible with IPv4.

**Key Features:**
1. **Larger Addressing Range:** 128-bit addresses (vs 32-bit IPv4), ~340 undecillion addresses
2. **Simplified Header:** Fewer fields, faster routing decisions
3. **End-to-End Connectivity:** Globally unique addresses, no NAT needed
4. **Auto-configuration:** Stateless and stateful methods, works without DHCP
5. **Inbuilt Security:** IPSec support
6. **Anycast Support:** Packets sent to nearest available destination
7. **Mobility Support:** Nodes retain IP addresses while moving
8. **Extensibility:** Header options can be extended

**Why Important for IoT:**
- Massive number of IoT devices need unique addresses
- Resource-constrained devices need efficient, lightweight processing
- Security is critical for IoT deployments
- Mobile IoT devices need to maintain connectivity while moving

---

**Q3. Explain MQTT protocol with its architecture and QoS levels.**

**Answer:**

**MQTT (Message Queue Telemetry Transport)** is an open standard, application layer, Client/Server publish/subscribe messaging transport protocol.

**Architecture Components:**
- **Broker (Server):** Accepts messages from clients and delivers to interested clients based on topics
- **Client:** Device that publishes or subscribes to topics
- **Topic:** Namespace for messages on the broker
- **Publish:** Client sending message to broker
- **Subscribe:** Client telling broker which topics interest it

**QoS Levels:**
| Level | Name | Delivery Guarantee | Use Case |
|-------|------|-------------------|----------|
| 0 | At most once | Best effort, may lose messages | Ambient sensor data |
| 1 | At least once | Assured delivery, duplicates possible | General messaging |
| 2 | Exactly once | Assured delivery, no duplicates | Billing systems |

**Example:** A wireless thermometer publishes temperature to topic `/sensors/temp`; a humidity sensor publishes to `/sensors/humid`. Other clients subscribe to these topics to receive the data.

---

**Q4. Compare IPv4 and IPv6.**

**Answer:**

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address Length | 32 bits | 128 bits |
| Address Space | ~4.3 billion | ~340 undecillion |
| Notation | Decimal | Hexadecimal |
| Header | Complex | Simplified |
| Security | Optional | Built-in (IPSec) |
| Auto-config | DHCP required | Stateless/Stateful |
| NAT | Required | Not required |
| Backward Compat | - | Not compatible with IPv4 |

**Why IPv6 for IoT:** Massive address space for billions of IoT devices, built-in security, auto-configuration for easy deployment, mobility support.

---

**Q5. Explain 6LoWPAN.**

**Answer:**
6LoWPAN (IPv6 over Low Power Wireless Personal Area Network) is an IPv6 protocol extended from IPv6 over WPAN.

**Specifications:**
- Frequency: 2.4 GHz (IEEE 802.15.4)
- Data Rate: 200 kbps max
- Range: ~200 m outdoor
- Max Nodes: ~100
- Network Type: Mesh (robust, scalable, self-healing)
- Security: AES-128 link layer encryption

**Features:**
- Makes individual nodes IP-enabled
- Can interact with 802.15.4 and other devices (Wi-Fi)
- Requires sleep mode for battery saving
- Minimal memory, lower routing overhead
- One-to-many and many-to-one routing
- Leaf nodes can sleep for longer durations

**Applications:** Home automation, smart agriculture, industrial monitoring.

---

## 10. SELF-TEST QUESTIONS

1. **True/False:** IPv6 is backward compatible with IPv4.
2. **True/False:** MQTT uses publish/subscribe pattern.
3. **Multiple Choice:** Which protocol operates on UDP port 5353? (A) DNS (B) mDNS (C) UPnP (D) HTTP
4. **Multiple Choice:** Which QoS level guarantees exactly-once delivery? (A) 0 (B) 1 (C) 2 (D) 3
5. **Short Answer:** What does 6LoWPAN stand for?
6. **Short Answer:** Name two discovery protocols in IoT.
7. **Scenario:** A smart home needs to connect 50+ battery-powered sensors with low data rates. Which protocol would you recommend and why?

**Answer Key:**
1. False (IPv6 is NOT backward compatible with IPv4)
2. True
3. B (mDNS)
4. C (QoS 2 = Exactly once)
5. IPv6 over Low Power Wireless Personal Area Network
6. Physical Web, mDNS, UPnP (any two)
7. 6LoWPAN — designed for constrained devices, low power, mesh networking, battery operation

---

**Good luck with your Unit 3 IoT exam!** Focus on understanding the protocol comparisons and MQTT architecture — these are high-yield topics.