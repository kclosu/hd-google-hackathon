# Agentic Platform for the manufacturer

## Project Structure

```
hd-google-hackathon/
├── docs/                      # Design notes and architecture references
├── mock_data/                 # Python fixtures and sample data for tests
├── src/
│   └── hd_google_hackathon/   # Runtime package (empty scaffold for now)
└── tests/                     # Pytest suites mirroring src/ for coverage
```

Run `python main.py` for a quick smoke check, or `pytest` once additional tests are added (the suite exercises the `mock_data` fixtures).

## North Star & Guardrails

* Unify internal support experience around dealer-facing issues without forcing a single dealer tech stack; rely on protocols, data contracts, and lightweight adapters.
* Target measurable reductions in mean time to resolution, cross-region escalation effort, and redundant ERP queries to prove value.
* Design for regional compliance (data residency, consent) by making federation, tenancy controls, and policy-aware routing first-class.

## Layered Architecture

* Interaction Hub: Internal support portal and API routing layer with role-aware workspaces for support agents, account managers, planners.
* Agent Orchestration Fabric: Event-driven hub (e.g., LangGraph/LangChain orchestration or Google Vertex AI Agent Builder) that coordinates specialized agents, enforces guardrails, manages retries, and logs provenance.
* Federated Integration Mesh: Adapters/gateways per ERP cluster or dealer system, using a common protocol (schema contracts, change events, OAuth/service accounts) rather than shared UI; push frequently-needed data into a normalized cache for fast agent access.
* Knowledge Services: Memory layer (short-term conversation state + episodic ticket history), knowledge graph for entities/relationships, vector store for unstructured docs, all wrapped in governance (access policies, retention).
*Observability & Governance: Central policy engine (RBAC/ABAC), audit ledger, cost dashboards, and feature toggles to manage regional rollouts.

## Agents Garden

* Support Triage Agent: Classifies inbound tickets/chats, enriches with dealer context, routes to correct queue, auto-extracts SLA timers.
* Investigation Agent: Pulls order history, production status, shipment telemetry; compares against standards to flag anomalies and propose resolutions.
* ERP Sherpa Agent: Encapsulates knowledge of each ERP variant via tool connectors; translates high-level intents (“update shipment priority”) into correct transactions.
* Policy & Compliance Agent: Checks suggested actions against regional rules, warranty terms, data-sharing agreements before execution.
* Playbook Author Agent: Summarizes resolved cases into reusable playbooks, flags gaps in documentation, suggests knowledge articles.
* Metrics & Insight Agent: Synthesizes operational KPIs, surfacing systemic issues (e.g., recurring part shortages or dealer training gaps).

## Shared Tools & Connectors

* Tool catalog: standardized interfaces for ticket systems (ServiceNow, Zendesk), ERP adapters, logistics APIs, knowledge graph queries, document retrieval, communication channels (email, Teams/Slack).
* Protocol templates: shared schemas for order, shipment, support events; transformation rules so dealers can provide minimal conformance without stack changes.
* Security utilities: consent-as-code checks, PII redaction, regional data routing.
* Simulation/sandbox tooling for testing agents against historical tickets before production.


## Memory & Knowledge Graph

* Short-term memory: conversation/session store with TTL to maintain context per ticket.
* Long-term episodic memory: case notebook capturing prior resolutions, linked to dealers/products; supports personalization and avoids repeat questions.
* Knowledge graph: Entities (Product, Component, Order, Dealer, Region, Claim, Installer) with edges describing dependencies, warranties, responsibilities; fed by ERP snapshots, ticket outcomes, and manually curated data; enables root cause analysis and agent reasoning.
* Vector store: embeddings of manuals, SOPs, regional regulations, dealer agreements; used for retrieval-augmented responses.
