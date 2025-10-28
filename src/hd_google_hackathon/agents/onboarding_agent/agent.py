from google.adk.agents import Agent
from hd_google_hackathon.config import DEFAULT_MODEL

def provide_training_materials(dealer_info: dict) -> dict:
    """Provides personalized training materials and tutorials for a new dealer."""
    dealer_name = dealer_info.get("name", "New Dealer")
    return {"materials": f"Sent personalized welcome kit and training portal access to {dealer_name}."}

def setup_account(dealer_info: dict) -> dict:
    """Sets up the dealer's account, payment methods, and branding preferences."""
    return {"status": "success", "message": "Account created, payment methods linked, and branding preferences saved."}

def schedule_follow_up(dealer_info: dict) -> dict:
    """Schedules a follow-up call with a human account manager."""
    return {"status": "success", "message": "Scheduled a follow-up call with Michael (Account Manager) for next week."}

def create_agent() -> Agent:
    return Agent(
        name="onboarding_agent",
        model=DEFAULT_MODEL,
        description="Automates the onboarding process for new dealers.",
        tools=[
            provide_training_materials,
            setup_account,
            schedule_follow_up,
        ],
    )

root_agent = create_agent()
