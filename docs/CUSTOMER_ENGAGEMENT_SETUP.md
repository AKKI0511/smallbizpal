# Customer Engagement Agent - Dev Setup & Usage Guide

## 🎯 Overview

During local development we run **all agents in the same Python process** using the ADK *dev UI* (`adk web`).  The public-facing `CustomerEngagementAgent` talks to the internal `KBProxyAgent` via an in-process **`AgentTool`**.  
(When we graduate to a hosted demo we will swap this AgentTool wrapper with an A2A call, but nothing else will need to change.)

```
Visitor ➜ CustomerEngagementAgent ──AgentTool──► KBProxyAgent ➜ Private KB
```

## 🏗️ Local Architecture (Dev Mode)
• **CustomerEngagementAgent** – lives in `smallbizpal/agents/customer_engagement`  
  – Tools: `ask_internal_kb` (AgentTool), `schedule_meeting`

• **KBProxyAgent** – lives in `smallbizpal/agents/kb_proxy`  
  – Tool: `search_private_kb` (Full business data now, vector RAG later)

• **Private Knowledge Base** – JSON file at `data/knowledge_base.json`  
  – Populated by the Business-Discovery agent.

## 🚀 Quick Start (Dev)

```bash
# 1. Install deps (editable mode)
uv sync

# 2. Launch the ADK dev UI
adk web
```

Open the browser UI (defaults to http://localhost:8000) and chat as:
* **Business owner** – talk to the Orchestrator to fill in your profile.
* **Customer** – switch role and ask questions; the Customer-Engagement agent will fetch answers via the KB proxy.

## 📋 Current Feature Set
✓ 24/7 Q&A using your business profile  
✓ Lead capture & meeting scheduling  
✓ In-process security boundary (public agent can only access KB via the proxy tool)  
✓ Ready for seamless swap to A2A + vector RAG (no agent-prompt changes required)

## 🔄 Updating Business Information
After you add or modify info through the Business-Discovery agent, the KBProxyAgent sees the changes immediately because both agents read the same JSON file.  
(No manual refresh required during dev.)

## 🛠️ Next Milestones
1. Replace full business data in `search_private_kb` with Qdrant vector retrieval.  
2. Swap the AgentTool wrapper for an A2A JSON-RPC call when we move to separate deployments.  
3. Add document/PDF ingestion and chunk-embedding pipeline.

## 📋 Features

### Customer Engagement Agent
- ✅ **24/7 Availability**: Never miss a potential customer
- ✅ **Lead Qualification**: Identifies serious prospects automatically
- ✅ **Meeting Scheduling**: Converts conversations into booked meetings
- ✅ **Brand Consistency**: Uses your business information and tone
- ✅ **Easy Integration**: One-line embed code for any website

### Admin Dashboard
- ✅ **Lead Management**: View and manage all customer leads
- ✅ **Knowledge Base Control**: Update business information securely
- ✅ **Performance Analytics**: Track engagement metrics
- ✅ **Agent Orchestration**: Access to all business management agents

## 🔧 Configuration

### Business Information
The agent uses your existing business profile from the knowledge base. To update:

1. Use the Admin Dashboard at `localhost:8000`
2. Chat with the Orchestrator to update business information
3. The public knowledge base will be automatically regenerated

### Widget Customization (TODO)
The chat widget automatically adapts to your business:
- Business name from your profile
- Brand colors (customizable)
- Greeting message
- Response tone and style

## 📊 Lead Management

### Lead Capture
When customers schedule meetings, leads are automatically:
- Saved to `data/leads/leads.json`
- Stored in the knowledge base for analytics
- Available in the admin dashboard

### Lead Data Structure
```json
{
  "name": "Customer Name",
  "email": "customer@email.com", 
  "topic": "Reason for meeting",
  "preferred_time": "Optional preferred time",
  "timestamp": "2025-01-XX...",
  "status": "new",
  "source": "customer_engagement_agent"
}
```

## 🌐 Website Integration (TODO)

### Embed the Widget
Add this single line to your website's HTML:
```html
<script src="http://your-domain:8001/widget/embed.js"></script>
```

### Widget Features
- **Responsive Design**: Works on desktop and mobile
- **Minimal Footprint**: Lightweight and fast-loading
- **Customizable**: Adapts to your brand automatically
- **Session Management**: Maintains conversation context

## 🔒 Security & Privacy

### Data Separation
- **Private Data**: Stays on the admin server (localhost only)
- **Public Data**: Only safe, marketing-appropriate information
- **A2A Protocol**: Secure communication between agents

### Access Control
- **Admin Server**: Bound to localhost (127.0.0.1) only
- **Engagement Server**: Public-facing but with limited data access
- **No Sensitive Data**: Customer-facing agent cannot access private information

## 🛠️ Development & Customization

### Agent Customization
Edit `smallbizpal/agents/customer_engagement/config.py` to modify:
- Conversation style
- Lead qualification criteria
- Meeting scheduling logic
- Response templates

### Knowledge Base Updates
The system automatically:
- Generates public KB from private data
- Updates when business information changes
- Maintains security boundaries

## 🔄 Updates & Maintenance

### Updating Business Information
1. Use admin dashboard to update business profile
2. System automatically regenerates public knowledge base
3. Changes reflect immediately in customer conversations

---

**🎉 Congratulations!** Your AI-powered customer engagement system is ready to convert visitors into customers 24/7! 