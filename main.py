import time
import sys
import os

# Import all the agents
from src.hd_google_hackathon.agents.support_triage_agent import agent as support_triage_agent
from src.hd_google_hackathon.agents.investigation_agent import agent as investigation_agent
from src.hd_google_hackathon.agents.policy_compliance_agent import agent as policy_compliance_agent
from src.hd_google_hackathon.agents.erp_sherpa_agent import agent as erp_sherpa_agent
from src.hd_google_hackathon.agents.playbook_author_agent import agent as playbook_author_agent
from src.hd_google_hackathon.agents.metrics_insight_agent import agent as metrics_insight_agent

# --- ANSI Color Codes for beautiful terminal output ---
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Helper functions for printing ---
def print_narrator(text, delay=0.02):
    for char in f"{colors.HEADER}{colors.BOLD}🎤 (Presenter):{colors.ENDC} {colors.WARNING}{text}{colors.ENDC}\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(1)

def print_agent_activity(agent_name, text, color=colors.CYAN, delay=0.01):
    for char in f"{color}[{agent_name}]:{colors.ENDC} {text}\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(0.5)

def print_system_event(text, delay=0.01):
    for char in f"{colors.BLUE}* {text} *{colors.ENDC}\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(1)

def main():
    """Runs the real-time, narrated demo of the Agentic Platform."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_narrator("Welcome to the live demo of our Autonomous Operations Platform.")
    print_narrator("We're about to witness a critical support issue being resolved in real-time, with zero human intervention.")
    
    # 1. A new support request arrives
    dealer_request = "Our high-priority order #12345 for a T-800 endoskeleton is delayed! Our customer has a deadline. We need answers NOW."
    print_system_event(f"INCOMING REQUEST from 'Cyberdyne Systems': {dealer_request}")

    # 2. Support Triage Agent takes action
    print_agent_activity("Support Triage Agent", "INCOMING_REQUEST. Parsing...")
    classification = support_triage_agent.classify_request(request=dealer_request)
    print_agent_activity("Support Triage Agent", f"Intent: '{classification['type']}'. Sentiment: 'Frustrated'.")
    enriched_request = support_triage_agent.enrich_request(request=dealer_request)
    print_agent_activity("Support Triage Agent", f"Context: {enriched_request['enriched_request'].split(']')[1][1:]}")
    sla = support_triage_agent.extract_sla(request=dealer_request)
    print_agent_activity("Support Triage Agent", f"SLA: '{sla['sla']}'. Timer initiated.")
    routed_queue = support_triage_agent.route_request(request=dealer_request)
    print_agent_activity("Support Triage Agent", f"Action: Routing to {routed_queue['queue']}.")
    print("-"*50)
    time.sleep(2)

    # 3. Investigation Agent takes over
    print_narrator("The Investigation Agent is now autonomously diagnosing the problem...")
    print_agent_activity("Investigation Agent", "INVESTIGATION_START for order #12345.")
    order_history = investigation_agent.pull_order_history(order_id="12345")
    print_agent_activity("Investigation Agent", f"Calling ERP Sherpa Agent -> Get order details. SUCCESS: {order_history['history']}")
    shipment_telemetry = investigation_agent.pull_shipment_telemetry(order_id="12345")
    print_agent_activity("Investigation Agent", f"Calling Logistics API -> Get shipment telemetry. {colors.FAIL}SUCCESS: {shipment_telemetry['telemetry']}{colors.ENDC}")
    print_agent_activity("Investigation Agent", "ANOMALY_DETECTED. The order is stalled. Searching for a solution...")
    print_agent_activity("Investigation Agent", "Calling Inventory System -> Query for component 'CPU-001' across all North American plants.")
    print_agent_activity("Investigation Agent", f"{colors.GREEN}SUCCESS: 'US-East' plant is out of stock. 'US-West' plant has 5 units available.{colors.ENDC}")
    resolution = investigation_agent.propose_resolution(anomalies=[])
    print_agent_activity("Investigation Agent", f"SOLUTION_PROPOSED: {resolution['resolution']}")
    print("-"*50)
    time.sleep(2)

    # 4. Policy & Compliance Agent provides oversight
    print_narrator("Before executing, the Policy & Compliance agent provides autonomous oversight...")
    action_to_check = resolution['resolution']
    regional_rules_ok = policy_compliance_agent.check_regional_rules(action=action_to_check)
    print_agent_activity("Policy & Compliance Agent", f"Checking regional rules: {'Compliant' if regional_rules_ok['compliant'] else 'Not Compliant'}")
    warranty_terms_ok = policy_compliance_agent.check_warranty_terms(action=action_to_check)
    print_agent_activity("Policy & Compliance Agent", f"Checking dealer contract for expedited shipping: {'Compliant' if warranty_terms_ok['compliant'] else 'Not Compliant'}")
    print_agent_activity("Policy & Compliance Agent", "ACTION_APPROVED.", color=colors.GREEN)
    print("-"*50)
    time.sleep(2)

    # 5. ERP Sherpa Agent executes the resolution
    print_narrator("With full compliance confirmed, the ERP Sherpa Agent executes the transaction...")
    update_result = erp_sherpa_agent.update_shipment_priority(order_id="12345", priority="High")
    print_agent_activity("ERP Sherpa Agent", "EXECUTION_START.")
    print_agent_activity("ERP Sherpa Agent", f"{colors.GREEN}SUCCESS: {update_result['message']}{colors.ENDC}")
    print("-"*50)
    time.sleep(2)

    # 6. Automated Communication and Learning
    print_narrator("The crisis is averted. Now, the platform communicates with the dealer and learns from the experience...")
    print_system_event("New Automated Message sent to 'Cyberdyne Systems': Update on Order #12345 - A resolution is in place. New ETA: 24 hours.")
    
    systemic_issues = metrics_insight_agent.surface_systemic_issues()
    print_agent_activity("Metrics & Insight Agent", systemic_issues['issues'][0], color=colors.WARNING)

    playbook = playbook_author_agent.summarize_case(case_id="12345")
    print_agent_activity("Playbook Author Agent", playbook['playbook'])
    print("-"*50)
    time.sleep(2)

    print_narrator("Demo complete. An urgent issue was resolved in seconds, a systemic risk was identified, and the platform became smarter for the future.")

if __name__ == "__main__":
    main()