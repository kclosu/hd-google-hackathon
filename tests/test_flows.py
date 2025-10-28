import pytest
import sys
import time

from .mocks.mock_order_repository import MockOrderRepository
from .mocks.mock_product_repository import MockProductRepository
from .mocks.mock_dealer_repository import MockDealerRepository
from .mocks.mock_plant_repository import MockPlantRepository
from .mocks.mock_component_repository import MockComponentRepository

from hd_google_hackathon.agents.support_triage_agent.agent import create_agent as create_support_triage_agent
from hd_google_hackathon.agents.investigation_agent.agent import create_agent as create_investigation_agent
from hd_google_hackathon.agents.policy_compliance_agent.agent import create_agent as create_policy_compliance_agent
from hd_google_hackathon.agents.erp_sherpa_agent.agent import create_agent as create_erp_sherpa_agent
from hd_google_hackathon.agents.playbook_author_agent.agent import create_agent as create_playbook_author_agent
from hd_google_hackathon.agents.metrics_insight_agent.agent import create_agent as create_metrics_insight_agent
from hd_google_hackathon.agents.installer_support_agent.agent import create_agent as create_installer_support_agent
from hd_google_hackathon.agents.configuration_agent.agent import create_agent as create_configuration_agent
from hd_google_hackathon.agents.onboarding_agent.agent import create_agent as create_onboarding_agent

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

# --- Repository Fixtures ---


# --- Agent Fixtures ---

@pytest.fixture
def support_triage_agent():
    return create_support_triage_agent()

@pytest.fixture
def investigation_agent():
    from tests.mocks.mock_order_repository import MockOrderRepository
    from tests.mocks.mock_component_repository import MockComponentRepository
    return create_investigation_agent(
        order_repo=MockOrderRepository(),
        component_repo=MockComponentRepository()
    )

@pytest.fixture
def policy_compliance_agent():
    return create_policy_compliance_agent()

@pytest.fixture
def erp_sherpa_agent():
    return create_erp_sherpa_agent()

@pytest.fixture
def playbook_author_agent():
    return create_playbook_author_agent()

@pytest.fixture
def metrics_insight_agent():
    return create_metrics_insight_agent()

@pytest.fixture
def installer_support_agent():
    from tests.mocks.mock_product_repository import MockProductRepository
    return create_installer_support_agent(product_repo=MockProductRepository())

@pytest.fixture
def configuration_agent():
    return create_configuration_agent()

@pytest.fixture
def onboarding_agent():
    return create_onboarding_agent()

# --- Flow Implementations ---

def test_successful_new_order_flow(configuration_agent):
    from tests.mocks.mock_order_repository import MockOrderRepository
    order_repository = MockOrderRepository()
    # 1. David (Dealer) places an order for 10 "Duette® Honeycomb Shades".
    print_system_event("Dealer 'David' places an order for 10 of product 'ss_duette' (Duette® Honeycomb Shades).")
    # In a real system, this would come through an API call and be handled by a "Conversational Ordering Agent"
    # For this simulation, we'll create the order directly using the repository.
    new_order = order_repository.create_order("dealer_1", [{"dealer_product_id": "ss_duette", "quantity": 10}], tenant_id="dealer_1")
    print_system_event(f"Order #{new_order.id} created with status '{new_order.status}'.")

    # 2. AI Opportunity: Automated Order Validation (Configuration Agent)
    # This is a simplified representation. A real agent would check inventory, dependencies, etc.
    options = {"items": new_order.items}
    validation_result = configuration_agent.tools[0](options=options, tenant_id="dealer_1")
    print_agent_activity("Configuration Agent", f"Running validation for order #{new_order.id}...\n{validation_result}")
    
    # 3. System updates order status
    order_repository.update_order_status(new_order.id, "in_progress", "dealer_1")
    print_system_event(f"Order #{new_order.id} status updated to 'in_progress'.")

    # 4. Manufacturing and Shipping
    print_system_event("Manufacturing occurs at the plants...")
    time.sleep(1)
    order_repository.update_order_status(new_order.id, "shipped", "dealer_1")
    print_system_event(f"Order #{new_order.id} has been shipped.")

    # 5. Final delivery and completion
    order_repository.update_order_status(new_order.id, "completed", "dealer_1")
    print_system_event(f"Order #{new_order.id} has been successfully delivered and installed. Status: 'completed'.")

def test_component_out_of_stock_flow(investigation_agent):
    from tests.mocks.mock_order_repository import MockOrderRepository
    from tests.mocks.mock_product_repository import MockProductRepository
    order_repository = MockOrderRepository()
    product_repository = MockProductRepository()
    # 1. David (Dealer) places an order for 5 "Silhouette® Window Shadings".
    print_system_event("Dealer 'David' places an order for 5 of product 'ss_silhouette' (Silhouette® Window Shadings).")
    # For this simulation, we'll create the order directly using the repository.
    new_order = order_repository.create_order("dealer_1", [{"dealer_product_id": "ss_silhouette", "quantity": 5}], tenant_id="dealer_1")
    print_system_event(f"Order #{new_order.id} created with status '{new_order.status}'.")

    # 2. The Investigation Agent checks inventory and finds that fabric_2 is out of stock.
    
    # First, find out which components are needed for the ordered product.
    dealer_product = product_repository.get_dealer_product_by_id(new_order.items[0].dealer_product_id, "dealer_1")
    product = product_repository.get_product_by_id(dealer_product.product_id, "dealer_1")
    print_system_event(f"Order requires components: {product.components}")

    # Now, have the agent check the stock for each component.
    for component_id in product.components:
        stock_check_result = investigation_agent.tools[1](component_id=component_id)
        stock_level = stock_check_result.get("stock", -1)
        if stock_level == 0:
            print_agent_activity("Investigation Agent", f"Checking stock for component '{component_id}'... {colors.FAIL}FAILURE: Component is out of stock.{colors.ENDC}")
            # 3. System puts the order on hold
            order_repository.update_order_status(new_order.id, "on_hold", "dealer_1")
            print_system_event(f"Order #{new_order.id} status updated to 'on_hold'. An alert has been raised for the planner.")
            break
        else:
            print_agent_activity("Investigation Agent", f"Checking stock for component '{component_id}'... SUCCESS: {stock_level} units in stock.")


def test_damaged_product_flow(support_triage_agent, investigation_agent, policy_compliance_agent, playbook_author_agent):
    # 1. David (Dealer) creates a new support ticket (Claim).
    dealer_request = "The Duette shades for order #order_1 arrived damaged. The box was crushed. Please advise."
    print_system_event(f"INCOMING CLAIM from 'David': {dealer_request}")

    # 2. Automated Triage & Enrichment (Support Triage Agent)
    classification = support_triage_agent.tools[0](request=dealer_request)
    print_agent_activity("Support Triage Agent", f"Intent: '{classification['type']}'.")
    enriched_request = support_triage_agent.tools[1](request=dealer_request)
    print_agent_activity("Support Triage Agent", f"Context added: {enriched_request['enriched_request']}")

    # 3. Automated Investigation (Investigation Agent)
    order_history = investigation_agent.tools[0](order_id="order_1")
    print_agent_activity("Investigation Agent", f"Pulling history for order #order_1... SUCCESS: {order_history['history']}")
    anomalies = investigation_agent.tools[4](data={})
    resolution = investigation_agent.tools[5](anomalies=anomalies['anomalies'])
    print_agent_activity("Investigation Agent", f"SOLUTION_PROPOSED: {resolution['resolution']}")

    # 4. Automated Compliance Check (Policy & Compliance Agent)
    action_to_check = resolution['resolution']
    regional_rules_ok = policy_compliance_agent.tools[0](action=action_to_check)
    print_agent_activity("Policy & Compliance Agent", f"Checking regional rules... {'Compliant' if regional_rules_ok['compliant'] else 'Not Compliant'}")
    warranty_terms_ok = policy_compliance_agent.tools[1](action=action_to_check)
    print_agent_activity("Policy & Compliance Agent", f"Checking warranty terms... {'Compliant' if warranty_terms_ok['compliant'] else 'Not Compliant'}")
    print_agent_activity("Policy & Compliance Agent", "ACTION_APPROVED.", color=colors.GREEN)

    # 5. Automated Knowledge Capture (Playbook Author Agent)
    playbook = playbook_author_agent.tools[0](case_id="claim_123")
    print_agent_activity("Playbook Author Agent", playbook['playbook'])


def test_installation_issue_flow(installer_support_agent):
    # 1. Installer discovers a missing part during installation.
    installer_issue = "I'm on site installing a Luminette shade and I'm missing a part for the headrail."
    print_system_event(f"INCOMING CALL from Installer: {installer_issue}")

    # 2. On-Site Installer Support (Installer Support Agent)
    solution = installer_support_agent.tools[0](issue=installer_issue)
    print_agent_activity("Installer Support Agent", f"Searching manuals for: '{installer_issue}'...\nSOLUTION: {solution['solution']}")

    # 3. The agent can also provide component details if needed.
    components = installer_support_agent.tools[1](product_id="luminette")
    print_agent_activity("Installer Support Agent", f"Providing component list for product 'luminette': {components['components']}")


def test_proactive_maintenance_flow(metrics_insight_agent):
    # 1. The Metrics & Insight Agent monitors product data.
    print_system_event("The Metrics & Insight Agent runs its scheduled analysis of field data.")

    # 2. The agent identifies a product with a high risk of failure.
    prediction = metrics_insight_agent.tools[1](tenant_id="dealer_1")
    print_agent_activity("Metrics & Insight Agent", f"ANALYSIS COMPLETE: {prediction['prediction']}")

    # 3. The agent proactively notifies the dealer.
    print_system_event(f"Proactive alert sent to dealer 'David': {prediction['recommendation']}")


def test_complex_product_configuration_flow(configuration_agent):
    # 1. David (Dealer) needs to order a complex product.
    print_system_event("Dealer 'David' starts configuring a complex product.")
    config_options = {"fabric": "fabric_1", "headrail": "headrail_1", "motorized": True, "quantity": 2}

    # 2. The Configuration Agent guides David through the options.
    validation_result = configuration_agent.tools[0](options=config_options, tenant_id="dealer_1")
    print_agent_activity("Configuration Agent", f"Validating configuration: {config_options}... {'VALID' if validation_result['valid'] else 'INVALID'}")

    # 3. The agent generates a quote.
    if validation_result['valid']:
        quote = configuration_agent.tools[1](config=config_options, tenant_id="dealer_1")
        print_agent_activity("Configuration Agent", f"Configuration is valid. Quote: {quote['quote']}")
        print_system_event("Dealer 'David' confirms the order.")
    else:
        print_agent_activity("Configuration Agent", f"Configuration is invalid: {validation_result['reason']}", color=colors.FAIL)

def test_get_orders_by_dealer():
    from tests.mocks.mock_order_repository import MockOrderRepository
    order_repository = MockOrderRepository()
    # 1. Create a new order for a specific dealer.
    dealer_id = "dealer_2"
    new_order = order_repository.create_order(dealer_id, [{"dealer_product_id": "ss_duette", "quantity": 1}], tenant_id=dealer_id)
    print_system_event(f"Order #{new_order.id} created for dealer '{dealer_id}'.")

    # 2. Retrieve all orders for that dealer.
    orders = order_repository.get_orders_by_dealer(dealer_id, tenant_id="any_tenant")
    print_system_event(f"Found {len(orders)} orders for dealer '{dealer_id}'.")

    # 3. Verify that the newly created order is in the list.
    assert any(order.id == new_order.id for order in orders)
    print_system_event(f"Verified that order #{new_order.id} is in the list of orders for dealer '{dealer_id}'.")


def test_dealer_onboarding_flow(onboarding_agent):
    print_narrator("Executing Flow 7: New Flow - Dealer Onboarding")

    # 1. A new dealer signs up.
    new_dealer_info = {"name": "Budget Blinds", "region": "USA"}
    print_system_event(f"New dealer has signed up: {new_dealer_info['name']}")

    # 2. The Onboarding Agent initiates the process.
    print_narrator("AI Opportunity: The Onboarding Agent automates the initial setup.")
    training = onboarding_agent.tools[0](dealer_info=new_dealer_info)
    print_agent_activity("Onboarding Agent", training['materials'])

    # 3. The agent sets up the account.
    account_setup = onboarding_agent.tools[1](dealer_info=new_dealer_info)
    print_agent_activity("Onboarding Agent", account_setup['message'])

    # 4. The agent schedules a follow-up.
    follow_up = onboarding_agent.tools[2](dealer_info=new_dealer_info)
    print_agent_activity("Onboarding Agent", follow_up['message'])

    print_narrator("Flow 7 execution complete.")

def test_dealer_onboarding_flow(onboarding_agent):
    print_narrator("Executing Flow 7: New Flow - Dealer Onboarding")

    # 1. A new dealer signs up.
    new_dealer_info = {"name": "Budget Blinds", "region": "USA"}
    print_system_event(f"New dealer has signed up: {new_dealer_info['name']}")

    # 2. The Onboarding Agent initiates the process.
    print_narrator("AI Opportunity: The Onboarding Agent automates the initial setup.")
    training = onboarding_agent.tools[0](dealer_info=new_dealer_info)
    print_agent_activity("Onboarding Agent", training['materials'])

    # 3. The agent sets up the account.
    account_setup = onboarding_agent.tools[1](dealer_info=new_dealer_info)
    print_agent_activity("Onboarding Agent", account_setup['message'])

    # 4. The agent schedules a follow-up.
    follow_up = onboarding_agent.tools[2](dealer_info=new_dealer_info)
    print_agent_activity("Onboarding Agent", follow_up['message'])

    print_narrator("Flow 7 execution complete.")
