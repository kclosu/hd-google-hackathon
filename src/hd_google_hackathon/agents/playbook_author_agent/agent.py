from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def summarize_case(case_id: str) -> dict:
    """Summarizes a resolved case into a reusable playbook."""
    return {"status": "success", "playbook": "New playbook created: 'Resolving Cross-Plant Component Shortages'."}

def flag_documentation_gap(gap_description: str) -> dict:
    """Flags a gap in the documentation."""
    return {"status": "success", "message": "Documentation gap flagged: " + gap_description}

def suggest_knowledge_article(topic: str) -> dict:
    """Suggests a new knowledge article."""
    return {"status": "success", "message": "Knowledge article suggested for topic: " + topic}


root_agent = Agent(
    name="playbook_author_agent",
    model=DEFAULT_MODEL,
    description="Summarizes resolved cases into reusable playbooks, flags gaps in documentation, suggests knowledge articles.",
    tools=[
        summarize_case,
        flag_documentation_gap,
        suggest_knowledge_article,
    ],
)