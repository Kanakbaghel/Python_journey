<h1 align="center"> My Python Journey </h1>
<div align="center">

<!-- Advanced animated header with gradient background -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18,20,22&height=300&section=header&text=My%20Python%20Journey&fontSize=90&animation=fadeIn&fontAlignY=35&desc=Building%20Python%20Mastery%20Through%20Working%20Code&descAlignY=55&descSize=25&fontColor=8B7D8B" alt="Header"/>

</div>

## About This Repository

This repository documents my **100-day Python challenge** focused on **Data Science**, covering topics from **basic Python programming** to **advanced machine learning and data visualization**.  
Each day contains a Jupyter notebook or script with explanations, examples, and exercises to solidify learning.

---

Learning Path Overview
- *Days 1-25*: *Python Basics* — syntax, data types, control flow, functions, and file handling
- *Days 26-50*: *Intermediate* — NumPy, Pandas, data visualization, OOP, and APIs
- *Days 51-75*: *Advanced* — machine learning algorithms, NLP, deep learning, and model deployment
- *Days 76-100*: *Projects* — end-to-end data science projects, dashboards, and portfolio building
---

# Contributing
Contributions, suggestions, and feedback are welcome!
Please follow these steps to contribute:

- Fork the repository
- Create a new branch (git checkout -b feature/your-feature)
- Commit your changes (git commit -m 'Add some feature')
- Push to the branch (git push origin feature/your-feature)
- Open a Pull Request

---
## Architecture & Learning Path

<div align="center" style="background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%); padding: 40px; border-radius: 20px;">

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#FFE4E1', 'primaryBorderColor':'#8B7D8B', 'primaryTextColor':'#4A4A4A', 'lineColor':'#DDA0DD', 'secondaryColor':'#E6E6FA', 'tertiaryColor':'#F0F8FF', 'background':'#FFFFFF', 'mainBkg':'#FFE4E1', 'secondBkg':'#E6E6FA', 'tertiaryBkg':'#F0F8FF', 'fontFamily':'Georgia, serif', 'fontSize':'16px'}}}%%

flowchart TB
    subgraph Foundation ["Foundation Layer"]
        direction LR
        A[Environment<br/>Setup] --> B[Package<br/>Management]
        B --> C[CLI<br/>Development]
    end
    
    subgraph Core ["Core Skills"]
        direction LR
        D[DateTime<br/>Handling] --> E[Text<br/>Processing]
        E --> F[NLP<br/>Basics]
        F --> G[HTTP &<br/>APIs]
        G --> H[Database<br/>Systems]
    end
    
    subgraph Performance ["Performance Layer"]
        direction LR
        I[Async/<br/>Parallel] --> J[Media<br/>Processing]
        J --> K[System<br/>Optimization]
    end
    
    subgraph DataScience ["Data Science"]
        direction LR
        L[Numerical<br/>Computing] --> M[Data<br/>Visualization]
        M --> N[Machine<br/>Learning]
    end
    
    subgraph Web ["Web Systems"]
        direction LR
        O[Web<br/>Frameworks] --> P[Authentication<br/>& Security]
        P --> Q[Task<br/>Queues]
        Q --> R[Data<br/>Validation]
    end
    
    subgraph Advanced ["Advanced Topics"]
        direction LR
        S[System<br/>Architecture] --> T[Desktop<br/>Applications]
        T --> U[Algorithms<br/>& DS]
        U --> V[Dev<br/>Tools]
    end
    
    Foundation --> Core
    Core --> Performance
    Core --> DataScience
    Core --> Web
    Performance --> Advanced
    DataScience --> Advanced
    Web --> Advanced
    
    style Foundation fill:#FFE4E1,stroke:#8B7D8B,stroke-width:3px
    style Core fill:#EDE5FF,stroke:#8B7D8B,stroke-width:3px
    style Performance fill:#F0E6FF,stroke:#8B7D8B,stroke-width:3px
    style DataScience fill:#FFF0F5,stroke:#8B7D8B,stroke-width:3px
    style Web fill:#FFEFD5,stroke:#8B7D8B,stroke-width:3px
    style Advanced fill:#F5DEB3,stroke:#8B7D8B,stroke-width:3px
```

</div>

## Complete Learning Route

<details>
<summary><b style="color: #8B7D8B;">Phase I: Foundation Layer (Click to expand)</b></summary>

<table style="width: 100%; background: linear-gradient(180deg, #FFE4E1 0%, #FFF0F5 100%); border-radius: 15px; padding: 20px;">
<tr>
<td width="5%" align="center" style="color: #8B7D8B; font-weight: bold;">01</td>
<td width="25%"><b style="color: #706B70;">Environment Management</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Beginner-FFE4E1?style=flat-square&labelColor=8B7D8B" align="right"/>
I evaluated conda, virtualenv, venv, pipenv, poetry, and PDM. Through extensive testing, I discovered venv + pip provides the best balance of simplicity and reliability for development, while uv excels in CI/CD pipelines. Includes performance comparisons and reproducibility tests.
</td>
</tr>
<tr style="background: rgba(237, 229, 255, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">02</td>
<td><b style="color: #706B70;">Package Distribution</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-EDE5FF?style=flat-square&labelColor=8B7D8B" align="right"/>
Publishing packages taught me the intricacies of wheels, sdists, and metadata. I benchmark build times, analyze distribution sizes, and explain why pyproject.toml is replacing setup.py. Real examples from packages I've published.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">03</td>
<td><b style="color: #706B70;">CLI Applications</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-F0E6FF?style=flat-square&labelColor=8B7D8B" align="right"/>
Click vs Typer vs argparse performance analysis with surprising results. I built the same CLI in each framework and measured startup time, memory usage, and developer experience. Includes advanced patterns for subcommands and configuration.
</td>
</tr>
</table>
</details>

<details>
<summary><b style="color: #8B7D8B;">Phase II: Core Skills (Click to expand)</b></summary>

<table style="width: 100%; background: linear-gradient(180deg, #EDE5FF 0%, #F0E6FF 100%); border-radius: 15px; padding: 20px;">
<tr>
<td width="5%" align="center" style="color: #8B7D8B; font-weight: bold;">04</td>
<td width="25%"><b style="color: #706B70;">DateTime Mastery</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-EDE5FF?style=flat-square&labelColor=8B7D8B" align="right"/>
Timezone bugs cost me a week of debugging in production. Now I test everything with pytz, pendulum, and zoneinfo. Includes DST edge cases, UTC best practices, and performance comparisons of datetime libraries.
</td>
</tr>
<tr style="background: rgba(240, 230, 255, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">05</td>
<td><b style="color: #706B70;">Text Processing</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-F0E6FF?style=flat-square&labelColor=8B7D8B" align="right"/>
Unicode nightmares and encoding errors at 3 AM. I document every text processing pitfall I've encountered, with benchmarks of regex vs string methods vs third-party libraries for common operations.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">06</td>
<td><b style="color: #706B70;">NLP Essentials</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-FFF0F5?style=flat-square&labelColor=8B7D8B" align="right"/>
spaCy vs NLTK vs Transformers head-to-head comparison. Memory profiling, speed benchmarks, and accuracy measurements for tokenization, NER, POS tagging, and embeddings.
</td>
</tr>
<tr style="background: rgba(255, 240, 245, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">07</td>
<td><b style="color: #706B70;">HTTP & APIs</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-FFEFD5?style=flat-square&labelColor=8B7D8B" align="right"/>
requests works until you need async. I compare requests, httpx, aiohttp, and urllib3 with real API calls, connection pooling strategies, and retry patterns that actually work in production.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">08</td>
<td><b style="color: #706B70;">Database Systems</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-F5DEB3?style=flat-square&labelColor=8B7D8B" align="right"/>
ORMs look elegant until you see the generated SQL. I profile SQLAlchemy, Django ORM, Peewee, and raw drivers. Includes N+1 query detection, connection pooling, and migration strategies.
</td>
</tr>
<tr style="background: rgba(245, 222, 179, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">09</td>
<td><b style="color: #706B70;">Concurrency Patterns</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-FFE4E1?style=flat-square&labelColor=8B7D8B" align="right"/>
The module that transformed my Python code. Real measurements of threading vs multiprocessing vs asyncio with production patterns for rate limiting, circuit breakers, and backpressure handling.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">10</td>
<td><b style="color: #706B70;">Media Processing</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-EDE5FF?style=flat-square&labelColor=8B7D8B" align="right"/>
Image and video processing without memory explosions. Pillow vs OpenCV vs scikit-image benchmarks, streaming processors, and GPU acceleration patterns.
</td>
</tr>
</table>
</details>

<details>
<summary><b style="color: #8B7D8B;">Phase III: Data Science & ML (Click to expand)</b></summary>

<table style="width: 100%; background: linear-gradient(180deg, #F0E6FF 0%, #FFF0F5 100%); border-radius: 15px; padding: 20px;">
<tr>
<td width="5%" align="center" style="color: #8B7D8B; font-weight: bold;">11</td>
<td width="25%"><b style="color: #706B70;">Numerical Computing</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-F0E6FF?style=flat-square&labelColor=8B7D8B" align="right"/>
NumPy internals revealed. Understanding memory layout, broadcasting, and vectorization improved my code's performance by 100x. Includes BLAS/LAPACK integration and GPU computing introduction.
</td>
</tr>
<tr style="background: rgba(255, 240, 245, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">12</td>
<td><b style="color: #706B70;">Data Visualization</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-FFF0F5?style=flat-square&labelColor=8B7D8B" align="right"/>
Matplotlib vs Plotly vs Altair vs Bokeh. I built identical visualizations in each to compare rendering speed, interactivity, file sizes, and developer experience.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">13</td>
<td><b style="color: #706B70;">Machine Learning</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-FFEFD5?style=flat-square&labelColor=8B7D8B" align="right"/>
From scikit-learn prototype to production deployment. Feature engineering pipelines, model versioning, A/B testing frameworks, and monitoring patterns that catch model drift.
</td>
</tr>
</table>
</details>

<details>
<summary><b style="color: #8B7D8B;">Phase IV: Web Development (Click to expand)</b></summary>

<table style="width: 100%; background: linear-gradient(180deg, #FFF0F5 0%, #FFEFD5 100%); border-radius: 15px; padding: 20px;">
<tr>
<td width="5%" align="center" style="color: #8B7D8B; font-weight: bold;">14</td>
<td width="25%"><b style="color: #706B70;">Web Frameworks</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-FFF0F5?style=flat-square&labelColor=8B7D8B" align="right"/>
FastAPI vs Flask vs Django performance shootout. I built the same API in each framework and measured throughput, latency percentiles, and resource usage under load.
</td>
</tr>
<tr style="background: rgba(255, 239, 213, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">15</td>
<td><b style="color: #706B70;">Authentication</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-FFEFD5?style=flat-square&labelColor=8B7D8B" align="right"/>
JWT, OAuth2, SAML, session management. Security patterns that actually protect applications, with penetration testing results and common vulnerability demonstrations.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">16</td>
<td><b style="color: #706B70;">Task Queues</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-F5DEB3?style=flat-square&labelColor=8B7D8B" align="right"/>
Celery vs RQ vs Huey vs Dramatiq. Performance under load, failure recovery patterns, and monitoring strategies. Real production configurations included.
</td>
</tr>
<tr style="background: rgba(245, 222, 179, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">17</td>
<td><b style="color: #706B70;">Data Validation</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-FFE4E1?style=flat-square&labelColor=8B7D8B" align="right"/>
Pydantic changed everything. Type safety, serialization, validation patterns that catch errors before production. Performance comparisons with marshmallow and cerberus.
</td>
</tr>
</table>
</details>

<details>
<summary><b style="color: #8B7D8B;">Phase V: Quality & Performance (Click to expand)</b></summary>

<table style="width: 100%; background: linear-gradient(180deg, #FFEFD5 0%, #F5DEB3 100%); border-radius: 15px; padding: 20px;">
<tr>
<td width="5%" align="center" style="color: #8B7D8B; font-weight: bold;">18</td>
<td width="25%"><b style="color: #706B70;">Testing Strategies</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-FFEFD5?style=flat-square&labelColor=8B7D8B" align="right"/>
pytest patterns that find real bugs. Property testing with Hypothesis, mutation testing, fixture strategies, and mocking patterns that don't break when code changes.
</td>
</tr>
<tr style="background: rgba(245, 222, 179, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">19</td>
<td><b style="color: #706B70;">Performance Optimization</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Expert-F5DEB3?style=flat-square&labelColor=8B7D8B" align="right"/>
Profiling tools that actually help. cProfile, py-spy, memory_profiler, line_profiler in practice. Finding and fixing the 20% of code that uses 80% of resources.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">20</td>
<td><b style="color: #706B70;">Architecture Patterns</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Expert-FFE4E1?style=flat-square&labelColor=8B7D8B" align="right"/>
Design patterns that survive requirement changes. Event sourcing, CQRS, hexagonal architecture, and dependency injection implemented and benchmarked.
</td>
</tr>
</table>
</details>

<details>
<summary><b style="color: #8B7D8B;">Phase VI: Advanced Topics (Click to expand)</b></summary>

<table style="width: 100%; background: linear-gradient(180deg, #F5DEB3 0%, #FFE4E1 100%); border-radius: 15px; padding: 20px;">
<tr>
<td width="5%" align="center" style="color: #8B7D8B; font-weight: bold;">21</td>
<td width="25%"><b style="color: #706B70;">Desktop Applications</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Advanced-F5DEB3?style=flat-square&labelColor=8B7D8B" align="right"/>
Modern GUIs that don't look dated. PyQt6 vs Tkinter vs Kivy vs Dear PyGui. Performance comparisons, distribution strategies, and native integration patterns.
</td>
</tr>
<tr style="background: rgba(255, 228, 225, 0.2);">
<td align="center" style="color: #8B7D8B; font-weight: bold;">22</td>
<td><b style="color: #706B70;">Algorithms & Data Structures</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Expert-FFE4E1?style=flat-square&labelColor=8B7D8B" align="right"/>
When algorithmic thinking matters in Python. Performance comparisons of built-in vs custom implementations, with real-world applications.
</td>
</tr>
<tr>
<td align="center" style="color: #8B7D8B; font-weight: bold;">23</td>
<td><b style="color: #706B70;">Development Tools</b></td>
<td style="color: #4A4A4A;">
<img src="https://img.shields.io/badge/Difficulty-Intermediate-EDE5FF?style=flat-square&labelColor=8B7D8B" align="right"/>
IDE configurations that boost productivity. Debugging techniques, profiling workflows, and automation scripts that save hours.
</td>
</tr>
</table>
</details>

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18,20,22&height=100&section=footer&animation=fadeIn&fontColor=8B7D8B" />

<h3 style="color: #8B7D8B;">Built with persistence and curiosity</h3>

----------

<p align="center"><em>Crafted with ♥ by <strong>Kanak Baghel</strong> | <a href="https://www.linkedin.com/in/kanakbaghel">LinkedIn</a></em></p>

---
