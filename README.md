🍯 Honey Comb: An AI-Powered Software Development Agent

  Honey Comb is an advanced, agentic AI assistant designed to streamline software development tasks. Powered by Google's Gemini
  Pro, this intelligent agent can understand complex requests, use a variety of tools to interact with a codebase, and even access
  the internet for research. It's a powerful demonstration of how AI can be leveraged to build sophisticated and secure developer
  tools.

<br>

  !GIF Demo Placeholder (<https://placehold.co/800x400/222/fff?text=Add+a+GIF+Demo+Here>)
  (Suggestion: Record a short GIF of the agent in action and replace the placeholder above to make this README even more
  engaging.)

<br>

  ✨ Key Features

  Honey Comb is more than just a chatbot. It's a true agent with a suite of powerful capabilities:

* 🤖 Agentic AI Core: Utilizes Google's Gemini Pro model to make intelligent plans and use a variety of tools to accomplish
complex tasks.
  * 💬 Interactive Chat Interface: A polished, rich-powered command-line interface for a smooth and intuitive user experience.
  * 🧰 Multi-Tool Functionality: The agent is equipped with a versatile set of tools, including:
    * File System Operations: Can read, write, and list files within the project directory.
    * Git Integration: Can check the status of the repository, view diffs, and commit changes.
    * Web Search: Can access the internet using the DuckDuckGo Search API to research solutions and gather information.
    * Code Execution: Can run Python scripts to test code and perform other tasks.
  * 🔒 Secure Sandboxed Execution: All Python code is executed in a secure, isolated Docker container, preventing it from
     accessing the host system. This demonstrates a strong commitment to security best practices.
  * 🤝 User Confirmation: For potentially destructive operations like writing files or making commits, the agent will always ask
     for user confirmation, ensuring you have the final say.
  * 💅 Rich CLI Output: All output is beautifully formatted with rich, including Markdown rendering for the AI's responses,
     making code blocks, lists, and other elements easy to read.

  🛠️ Tech Stack

  This project demonstrates proficiency in a modern, robust tech stack:

  * Backend: Python 3.11+
  * AI: Google Gemini Pro API
  * Package Management: uv
  * Containerization: Docker
  * CLI: rich
  * Core Libraries: google-generativeai, docker, duckduckgo-search, requests, beautifulsoup4

  🚀 Getting Started

  Follow these instructions to get your own instance of Honey Comb up and running.

  Prerequisites

  * Python 3.11+
  * Docker (<https://www.docker.com/get-started>)
  * uv (<https://github.com/astral-sh/uv>) (Python package installer)
  * A Google Gemini API Key. You can get one from Google AI Studio (<https://aistudio.google.com/app/apikey>).

  Installation

   1. Clone the repository:
   1  git clone <https://github.com/felixsolomon/honey-comb.git>
   2     cd honey-comb

   2. Create a virtual environment and install dependencies:

   1     uv venv
   2     uv pip install -r pyproject.toml

   3. Set up your environment variables:
       * Create a file named .env in the root of the project.
       * Add your Gemini API key to the .env file like this:

   1         GEMINI_API_KEY="YOUR_API_KEY_HERE"

  Usage

  To start the agent in interactive mode, simply run:

   1 python main.py

  You can then start giving instructions to the agent at the prompt.

  🔮 Future Improvements

  This project has a solid foundation, and there are many exciting possibilities for future   development:

  * Project Scaffolding: Teach the agent to create new projects from scratch.
  * Automated Testing: Empower the agent to write and run its own tests.
  * Session History: Implement a feature to save and load conversation history.
  * Configuration File: Add a config.yaml file to make it easier to manage settings.
