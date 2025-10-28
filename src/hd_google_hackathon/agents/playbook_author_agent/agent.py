from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def summarize_case(case_id: str) -> dict:
    """Summarizes the case and creates a new playbook."""
    return {"playbook": "New playbook created: 'Resolving Cross-Plant Component Shortages'"}

def create_agent() -> Agent:
    return Agent(
        name="playbook_author_agent",
        model=DEFAULT_MODEL,
        description="Summarizes resolved cases and creates new playbooks for future use.",
        tools=[summarize_case],
    )

root_agent = create_agent()