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

## 4. Data Model

### 4.1. Neo4j Graph Structure

#### Nodes (Electrical Components)
```cypher
(:Panel { panel_id, location, voltage, capacity_amperage })
(:Breaker { breaker_id, amperage_rating, breaker_type, position_in_panel })
(:Outlet { outlet_id, type, location })
(:Device { device_id, type, power_rating_watts })
(:ElectricalBox { box_id, junction_type, location })
```

#### Relationships (Circuits & Wiring)
```cypher
(:Panel)-[:HOT_FEEDS]->(:Breaker)
(:Breaker)-[:HOT_FEEDS]->(:Outlet)
(:Device)-[:NEUTRAL_FEEDS]->(:Panel)
(:Device)-[:GROUND_FEEDS]->(:Panel)
```

#### Edge Properties (For Wiring Details)
```cypher
{ wire_gauge, length_ft, voltage, amperage_limit }
```

## 5. Backend API Design

### 5.1. REST API Endpoints

| Method | Endpoint            | Description                          |
|--------|--------------------|--------------------------------------|
| `GET`  | `/get_graph`       | Fetch the current electrical system graph. |
| `POST` | `/update_power`    | Generate the next power snapshot.   |
| `GET`  | `/get_history`     | Retrieve past power snapshots.      |
| `POST` | `/restore_snapshot` | Load a previous power state.       |

### 5.2. Flask Power Update Logic

```python
import random
from flask import Flask, jsonify
from neo4j import GraphDatabase

app = Flask(__name__)

def update_power_usage():
    """Simulates power fluctuations for the next second."""
    with driver.session() as session:
        result = session.run("MATCH (d:Device) RETURN d.device_id AS id, d.power_rating_watts AS power")
        updates = []
        for record in result:
            fluctuation = random.uniform(-0.1, 0.1)  # ±10% variation
            new_power = int(record["power"] * (1 + fluctuation))
            updates.append({"id": record["id"], "power": new_power})
            session.run("MATCH (d:Device {device_id: $id}) SET d.power_rating_watts = $power", 
                        id=record["id"], power=new_power)
    return updates

@app.route('/update_power', methods=['POST'])
def update_power_route():
    """API Endpoint to update power usage."""
    new_data = update_power_usage()
    return jsonify({"status": "success", "updated_data": new_data})

if __name__ == '__main__':
    app.run(debug=True)
```

## 6. Frontend (React) Implementation

### 6.1. Graph Rendering with D3.js

```tsx
import React, { useEffect, useState } from 'react';
import * as d3 from 'd3';

const ElectricalGraph = () => {
    const [graphData, setGraphData] = useState(null);

    useEffect(() => {
        fetch('/get_graph')
            .then(response => response.json())
            .then(data => setGraphData(data));
    }, []);

    useEffect(() => {
        if (!graphData) return;
        const svg = d3.select('#graph-svg');
        // Render nodes and edges dynamically
    }, [graphData]);

    return <svg id="graph-svg" width="800" height="600"></svg>;
};

export default ElectricalGraph;
```

## 7. Error Handling & Edge Cases

| Scenario                     | Handling Strategy                                      |
|------------------------------|-------------------------------------------------------|
| **Database Connection Fails** | Flask returns `500` with an error message.           |
| **Invalid API Input**         | Returns `400 Bad Request`.                           |
| **Overloaded Circuit Detected** | UI highlights node in red, dashboard warns user.   |

## 8. Testing Plan

### 8.1. Unit Tests (Backend)

| Test Case                | Expected Output                                      |
|--------------------------|------------------------------------------------------|
| **Fetch graph data**     | Returns valid JSON with all nodes & edges.          |
| **Simulated power update** | Randomized changes within ±10% per second.        |
| **Overloaded circuit**   | Correctly flagged as overloaded.                    |

### 8.2. Integration Tests (Frontend & Backend)

- **Graph Rendering**: Verify all electrical components display correctly.
- **Power Update Simulation**: Clicking "Next Second" should trigger visible changes.
- **Snapshot History**: Ensure old snapshots persist and restore correctly.

## 9. Future Enhancements

- **Smart Meter API Integration** for real-world power monitoring.
- **Export to CSV/JSON** for historical power analysis.
- **Multi-Phase Power Distribution** modeling (3-phase for commercial buildings).



