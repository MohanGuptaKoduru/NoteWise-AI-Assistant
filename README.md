# NoteWise AI Assistant

An AI-powered personal assistant that can **search through your notes** and **fetch information from the web**.  
Built with Python, LLMs (Gemini + Mistral), and vector databases (ChromaDB).  

---

## Features
- Search personal notes (`mynotes.md`) with **semantic embeddings**
- Retrieve and summarize notes using **MistralAI**
- Web search with **DuckDuckGo** and webpage reader tools
- Conversational AI powered by **Gemini 2.0**
- Maintains **conversation history** for context-aware responses
- Built with `smolagents`, `llama_index`, and `chromadb`

---

## Project Structure
<pre>
NoteWise-AI-Assistant/
│── mynotes.md # Your personal notes
│── main.py # Main AI assistant loop
│── note_tool.py # Search my notes tool
│── keys.py # API key loader
│── requirements.txt
│── README.md
</pre>

---

## 🛠️ Setup & Installation

1. **Clone the repository**
 ```bash
   git clone https://github.com/MohanGuptaKoduru/NoteWise-AI-Assistant.git
   cd NoteWise-AI-Assistant
   ```
2.  Create a virtual environment
   ``` 
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```

4. Add your API Keys in the keys.py file
``` bash
GEMINI_API_KEY=your-gemini-key-here
MISTRAL_API_KEY=your-mistral-key-here
```
5. Run the assistant
```bash
python main.py
```
📊 Example Usage
You: Search my notes about spatiotemporal data

Assistant: [Step 2: Duration 5.85 seconds| Input tokens: 5,577 | Output tokens: 1,067]
Assistant: Spatio-temporal data refers to information that integrates both spatial (geographic location) and temporal (time-based) dimensions. It is critical for understanding dynamic phenomena, such as moving object trajectories (e.g., vehicle GPS tracks), environmental sensor readings over time, or time-varying satellite imagery.

Key aspects of spatio-temporal data include:

1. Applications: Used extensively in Geographic Information Systems (GIS), smart cities initiatives, environmental monitoring, transportation management, and epidemiology. Examples include tracking the spread of diseases over time, optimizing traffic flow patterns, and analyzing climate changes.
2. Data Models & Representations: Utilizes various models to represent spatial and temporal aspects. Spatial models encompass vector (points, lines, polygons) and raster (gridded formats like GeoTIFF). Temporal models include time-series data, trajectories (ordered time-location pairs), and image sequences. Spatio-temporal models represent dynamic objects and event-based models (e.g., disease rate mapping over time).
3. Indexing & Query Techniques: Employs hybrid indexes (e.g., time-augmented R-trees) that combine spatial and temporal dimensions for efficient searches. Common queries involve distance range calculations, nearest neighbor searches, trajectory analysis, and intersection checks.      
4. Data Governance & Management: Requires scalable storage solutions (e.g., ArcGIS Spatiotemporal Big Data Store) to manage high-volume observational data. Challenges include handling missing values, heterogeneous formats, and multi-modal data fusion.
5. Analytics & Mining: Involves tasks such as clustering, prediction, anomaly detection, and frequent pattern mining. Deep learning (CNNs, RNNs) and Graph Neural Networks (GNNs) are widely used for forecasting, disaster response, and precision agriculture.
6. Visualization & Exploration: Uses techniques like dashboards, heat maps, and animated sequences to interpret dynamic changes. Challenges include modeling continuous versus discrete changes and avoiding misinterpretation, such as the Modifiable Areal Unit Problem.
7. Special Use Cases & Advances: Explored in smart cities using geo-textual indexing, trajectory keyword search, and spatial crowdsourcing. Emerging trends include Spatio-Temporal Foundation Models (STFMs) for generalized task learning and distributed partitioning methods for large-scale data.

Spatio-temporal data analysis is a continuously evolving field with ongoing advancements in techniques and applications

# 📌 Future Improvements

Add a simple web or desktop UI

Support multiple documents in the knowledge base

Deploy as a cloud-hosted chatbot
