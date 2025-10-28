
import chainlit as cl
import asyncio

# Import all the agents
from src.hd_google_hackathon.agents.support_triage_agent import agent as support_triage_agent
from src.hd_google_hackathon.agents.investigation_agent import agent as investigation_agent
from src.hd_google_hackathon.agents.policy_compliance_agent import agent as policy_compliance_agent
from src.hd_google_hackathon.agents.erp_sherpa_agent import agent as erp_sherpa_agent
from src.hd_google_hackathon.agents.playbook_author_agent import agent as playbook_author_agent
from src.hd_google_hackathon.agents.metrics_insight_agent import agent as metrics_insight_agent

@cl.on_chat_start
async def start_demo():
    # Define avatars for each participant in the demo
    await cl.Avatar(name="Presenter", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here",).send()
    await cl.Avatar(name="System", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()
    await cl.Avatar(name="Support Triage Agent", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()
    await cl.Avatar(name="Investigation Agent", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()
    await cl.Avatar(name="Policy & Compliance Agent", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()
    await cl.Avatar(name="ERP Sherpa Agent", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()
    await cl.Avatar(name="Metrics & Insight Agent", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()
    await cl.Avatar(name="Playbook Author Agent", url="https://avatars.githubusercontent.com/u/128686189?s=400&u=a1d151b49261ac44LLM_MODEL_ICON_alt_text_here").send()

    # Set the initial message
    await cl.Message(author="Presenter", content="Welcome to the live demo of our Autonomous Operations Platform!").send()
    await asyncio.sleep(1)

    # Start the interactive demo by asking the user to initiate
    res = await cl.AskActionMessage(
        author="Presenter",
        content="Press the button to simulate an urgent dealer request and start the demo.",
        actions=[
            cl.Action(name="start_demo", value="start", label="💥 Simulate 'Urgent Order Crisis'")
        ],
        timeout=600
    ).send()

    if res and res.get("value") == "start":
        # --- Start of the Demo Flow ---
        dealer_request = "Our high-priority order #12345 for a T-800 endoskeleton is delayed! Our customer has a deadline. We need answers NOW."
        msg = cl.Message(author="System", content=f"**INCOMING REQUEST from 'Cyberdyne Systems'**: {dealer_request}")
        await msg.send()
        await asyncio.sleep(2)

        # --- Support Triage Agent Step ---
        async with cl.Step(name="Support Triage Agent", type="agent") as step:
            step.input = dealer_request
            await asyncio.sleep(1)
            classification = support_triage_agent.classify_request(request=dealer_request)
            step.output = f"- Intent: '{classification['type']}'\n- Sentiment: 'Frustrated'\n- Context: Dealer Tier is 'Platinum'\n- SLA: '{support_triage_agent.extract_sla(request=dealer_request)['sla']}'\n- Action: Routing to Investigation Queue"
            await step.update()

        # --- Investigation Agent Step ---
        async with cl.Step(name="Investigation Agent", type="agent") as step:
            await asyncio.sleep(1)
            step.input = "Order #12345"
            order_history = investigation_agent.pull_order_history(order_id="12345")
            shipment_telemetry = investigation_agent.pull_shipment_telemetry(order_id="12345")
            resolution = investigation_agent.propose_resolution(anomalies=[])
            step.output = f"- **Order History**: {order_history['history']}\n- **Shipment Telemetry**: {shipment_telemetry['telemetry']}\n- **Anomaly**: Shipment is delayed due to component shortage.\n- **Proposed Solution**: {resolution['resolution']}"
            await step.update()

        # --- Policy & Compliance Agent Step ---
        async with cl.Step(name="Policy & Compliance Agent", type="agent") as step:
            await asyncio.sleep(1)
            step.input = f"Action: {resolution['resolution']}"
            step.output = "- Regional Rules Check: Compliant\n- Dealer Contract Check: Compliant\n- **Action Approved**"
            await step.update()

        # --- ERP Sherpa Agent Step ---
        async with cl.Step(name="ERP Sherpa Agent", type="agent") as step:
            await asyncio.sleep(1)
            update_result = erp_sherpa_agent.update_shipment_priority(order_id="12345", priority="High")
            step.input = "Execute approved resolution for order #12345"
            step.output = f"**SUCCESS**: {update_result['message']}"
            await step.update()
        
        await cl.Message(author="System", content="**AUTOMATED MESSAGE Sent to 'Cyberdyne Systems'**: Update on Order #12345 - A resolution is in place. New ETA: 24 hours.").send()
        await asyncio.sleep(2)

        # --- Final Outcomes ---
        final_msg = cl.Message(author="Presenter", content="Demo complete! The urgent issue was resolved in seconds. But more importantly, the platform generated long-term value:")
        await final_msg.send()

        systemic_issues = metrics_insight_agent.surface_systemic_issues()
        playbook = playbook_author_agent.summarize_case(case_id="12345")

        await cl.Message(
            author="Metrics & Insight Agent",
            content=f"**Systemic Insight**: {systemic_issues['issues'][0]}",
            parent_id=final_msg.id,
            indent=1
        ).send()

        await cl.Message(
            author="Playbook Author Agent",
            content=f"**Knowledge Creation**: {playbook['playbook']}",
            parent_id=final_msg.id,
            indent=1
        ).send()
