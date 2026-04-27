## 🚀 AI Voice Assistant (JARVIS / Friday)

This project is a real-time AI-powered personal assistant inspired by **Iron Man’s Friday/JARVIS**, built using LiveKit agents and OpenAI’s realtime capabilities. The assistant can interact through voice, perform tasks using tools, and maintain memory of past conversations to provide a personalized experience.

---

## 🧠 Features

* 🎙️ **Real-time Voice Interaction**

  * Uses OpenAI Realtime model for natural conversations
  * Supports audio input/output with noise cancellation

* 🤖 **Custom AI Personality**

  * Butler-style assistant (sarcastic, classy, concise)
  * Responds in a single sentence like a true AI companion

* 🧩 **Tool Integration**

  * 🌦️ Weather information retrieval
  * 🌐 Web search functionality
  * 📧 Email sending capability

* 🧠 **Memory System (Persistent Context)**

  * Stores past conversations using Mem0
  * Retrieves user history for personalized responses
  * Context-aware replies based on previous interactions

* 🔗 **MCP Server Integration**

  * Dynamically extends assistant capabilities via external tools (N8N MCP Server)

* 🔊 **Noise Cancellation**

  * Enhanced audio clarity using LiveKit noise cancellation plugin

---

## 🛠️ Tech Stack

* **Python**
* **LiveKit Agents**
* **OpenAI Realtime API**
* **Mem0 (Memory Management)**
* **MCP (Model Context Protocol)**
* **DuckDuckGo Search API**
* **dotenv (Environment Management)**

---

## ⚙️ How It Works

1. Initializes a LiveKit agent session
2. Loads previous user memories (if available)
3. Starts a real-time voice interaction session
4. Uses tools dynamically based on user queries
5. Stores conversation history on shutdown for future use

---

## 📁 Project Structure

```
├── agent.py          # Main assistant logic & entrypoint
├── prompts.py        # AI personality & session instructions
├── tools.py          # External tool functions (weather, web, email)
├── requirements.txt  # Dependencies
```

---

## ▶️ Setup & Installation

```bash
git clone <your-repo-link>
cd <your-project-folder>

pip install -r requirements.txt
```

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key
N8N_MCP_SERVER_URL=your_mcp_server_url
```

Run the assistant:

```bash
python agent.py
```

---

## 💡 Use Cases

* Personal AI desk assistant 🤖
* Voice-controlled automation
* Smart home integration (extendable)
* Productivity assistant

---

## 🔮 Future Improvements

* Mobile app integration
* Smart IoT control (ESP32 integration 👀)
* Multi-user support
* Advanced task automation workflows

---

