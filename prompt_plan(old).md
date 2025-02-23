Home Electrical Graph Simulator - Developer Prompt Plan

Overview

This document provides a step-by-step plan for building the Home Electrical Graph Simulator, with iterative chunks and prompts for a code-generation LLM to implement each step in a test-driven manner. The goal is to ensure incremental progress, strong testing, and a smooth integration of components.

1. High-Level Blueprint

Phase 1: Environment Setup and Project Scaffolding

Set up Flask Backend with a simple /health check endpoint.

Create a React Frontend using TypeScript and a basic UI scaffold.

Add Testing Frameworks: Pytest for the backend, Jest for the frontend.

Phase 2: Database and API Foundation

Connect Flask to Neo4j with a basic graph schema.

Implement API Endpoints (Mocked Data):

/get_graph - Returns static graph JSON.

/update_power - Returns mock response.

/get_history - Empty history response.

/restore_snapshot - Placeholder implementation.

Connect Frontend to API - Calls endpoints and displays mock data.

Phase 3: Core Functionality

Implement Power Update Logic:

Adjust device power consumption by ±10%.

Store updates in Neo4j.

Create Snapshot System:

Store power state snapshots in Neo4j.

Enable retrieval and restoration of snapshots.

Enhance UI Graph Rendering:

Color-coded nodes for load.

Interactive edges with wire details.

Phase 4: Advanced Features

Add Circuit Balancing Logic:

Identify overloaded circuits.

Return warnings in API responses.

Develop Dashboard Panel:

Show total power consumption.

Highlight top power-consuming devices.

Final Testing, Edge Cases & Integration:

Handle database failures and API errors.

Conduct a complete UI/Backend integration test.

2. Iterative Chunks

Below is a refined, step-by-step breakdown of tasks, each leading to a well-defined, testable feature.

Chunk A: Environment Setup

Steps:

Create a new Flask + React project.

Set up Python virtual environment & dependencies (Flask, pytest).

Add Jest & TypeScript to React project.

Create app.py with a /health check endpoint.

Write a test ensuring /health returns {"status": "ok"}.

Create a Graph React component.

Add a button labeled "Next Second" (no functionality yet).

Chunk B: Neo4j Connection & Data Model

Steps:

Install the Neo4j Python driver.

Create db.py to manage Neo4j sessions.

Store sample nodes (:Device {power_rating_watts: 100}).

Write Pytest test to insert/query sample data.

Chunk C: Initial REST Endpoints (Mocked Data)

Steps:

Implement /get_graph, /update_power, /get_history, /restore_snapshot as placeholder endpoints.

Write Pytest tests verifying correct JSON response structures.

Connect the frontend to mock endpoints.

Chunk D: Implement Power Update Logic

Steps:

Retrieve all (:Device) nodes in Neo4j.

Randomly adjust power_rating_watts by ±10%.

Write tests ensuring power values remain within the expected range.

Replace /update_power mock response with real database updates.

Chunk E: Implement Snapshot History & Restoration

Steps:

Create (:Snapshot) nodes storing all device states.

Implement /get_history returning snapshot timestamps.

Implement /restore_snapshot to revert devices to a prior state.

Write tests verifying snapshot creation and restoration.

Chunk F: UI Enhancements - Graph Rendering

Steps:

Modify /get_graph to include circuit details.

Add D3.js-based visualization with interactive edges.

Highlight overloaded circuits in red.

Write tests verifying the UI correctly displays graph state changes.

Chunk G: Dashboard & Circuit Balancing

Steps:

Implement logic for detecting overloaded circuits.

Expand /get_graph to return a circuit_overload flag.

Add a Dashboard.tsx UI component displaying:

Total power consumption.

Top power-consuming devices.

Circuit warnings.

Write unit tests for backend overload logic and frontend UI updates.

Chunk H: Error Handling & Final Testing

Steps:

Handle invalid API inputs.

Implement a graceful fallback if the database is unreachable.

Write additional unit tests covering edge cases.

Conduct a final integration test ensuring all features work seamlessly.

3. Prompt List for Code-Generation LLM

Prompt 1: Flask + Pytest Scaffolding

Create a minimal Flask project with:
- A `requirements.txt` file with Flask & pytest.
- An `app.py` with a `/health` check returning `{"status": "ok"}`.
- A `tests/test_app.py` file using Pytest to verify `/health`.
- Instructions on installing dependencies and running tests.

Prompt 2: Neo4j Connection and Data Model

Extend Flask to connect to a Neo4j database:
- Install the Neo4j driver.
- Create `db.py` for session management.
- Add a sample `(:Device {device_id: "test-device", power_rating_watts:100})`.
- Write a Pytest test inserting/querying this data.

Prompt 3: Basic REST API with Mocked Data

Add REST API routes:
- `GET /get_graph` returning `{ "graph": "stub" }`.
- `POST /update_power` returning `{ "status": "stub" }`.
- `GET /get_history` returning `{ "history": [] }`.
- `POST /restore_snapshot` returning `{ "restored": "stub" }`.
- Write Pytest tests verifying JSON structure.

Prompt 4: Implement Power Update Logic

Modify `/update_power` to:
- Query all `(:Device)` nodes.
- Adjust `power_rating_watts` by ±10%.
- Return updated values in JSON.
- Write Pytest tests ensuring values remain within expected bounds.

Prompt 5: Snapshot History & Restoration

Implement snapshot functionality:
- Store system state snapshots in Neo4j.
- Update `/get_history` to return snapshot timestamps.
- Implement `/restore_snapshot` to revert system state.
- Write tests verifying snapshot creation and restoration.

Prompt 6: UI Enhancements - Graph Rendering

Modify `/get_graph`:
- Include circuit connections.
- Implement UI graph rendering using D3.js.
- Highlight overloaded circuits.
- Write tests verifying graph updates.

Prompt 7: Dashboard & Overload Warnings

Implement a `Dashboard.tsx` component:
- Display total power usage, highest load devices, and warnings.
- Fetch from a new `/dashboard_stats` endpoint.
- Write Jest tests verifying correct dashboard rendering.

Prompt 8: Final Error Handling & Integration

Ensure robust error handling:
- Handle invalid snapshot IDs.
- Return `500` if Neo4j is unreachable.
- Write tests covering these error cases.
- Final integration tests ensuring all features work together.