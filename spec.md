# Home Electrical Graph Simulator - Developer Specification

## 1. Overview
The **Home Electrical Graph Simulator** is a web application that visually represents a home's electrical system using a **graph database (Neo4j)**. It enables users to **simulate** electricity flow, observe **real-time power usage snapshots**, and analyze **circuit balancing, overloads, and wiring structure**.

## 2. Features & Requirements

### 2.1. Core Features
- **Graph-Based Visualization** of electrical components (panels, breakers, outlets, devices).
- **Simulated Power Updates** via a "Next Second" button introducing realistic power fluctuations.
- **Live UI Updates** with color-coded nodes, dynamic edge thickness, and AC/DC differentiation.
- **Circuit Balancing Analysis**, tracking phase loads and overload warnings.
- **Snapshot History Sidebar** for browsing and restoring past power states.
- **Dashboard Panel** showing total power consumption, highest-load devices, and warnings.

### 2.2. User Interactions
- **View Home Electrical Graph** – Displays a **static snapshot** of the system.
- **Click "Next Second"** – Triggers **random power fluctuations** and updates the UI.
- **View Snapshot History** – Browse previous snapshots and restore past states.
- **Expand Dashboard Panel** – View real-time **power trends and circuit warnings**.

## 3. Technical Architecture

### 3.1. Tech Stack
| Component | Technology |
|-----------|------------|
| **Frontend** | React (TypeScript), D3.js for graph visualization |
| **Backend** | Flask (Python) |
| **Database** | Neo4j (Graph Database) |
| **Data Exchange** | REST API (JSON) |

### 3.2. System Architecture Diagram
[ React (TypeScript) UI ] <-- REST API --> [ Flask Backend ] <-- Neo4j Queries --> [ Neo4j Graph Database ]

The system architecture diagram above illustrates the flow of data and interactions between the different components of the Home Electrical Graph Simulator. 

- The **React (TypeScript) UI** serves as the frontend of the application, providing the user interface for interacting with the electrical graph and displaying real-time power updates.
- The **Flask Backend** acts as the intermediary between the frontend and the Neo4j Graph Database. It handles incoming requests from the UI, processes them, and executes the corresponding Neo4j queries.
- The **Neo4j Graph Database** stores the electrical system data in a graph format, allowing for efficient querying and traversal of the electrical components.
- The **REST API** facilitates communication between the frontend and the backend, enabling data exchange in JSON format.

This architecture enables the Home Electrical Graph Simulator to provide a responsive and interactive user experience, while leveraging the power of a graph database for efficient data storage and retrieval.
