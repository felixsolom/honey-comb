
# 🍯 Honey Comb: AI-Powered Software Development Agent

An intelligent coding assistant that combines Google's Gemini Pro with secure sandboxed execution to help developers write, test, and manage code safely.

## 🎯 Project Overview

Honey Comb demonstrates advanced AI engineering principles by building a production-ready agentic system. Unlike simple chatbots, this agent can plan multi-step tasks, use multiple tools autonomously, and execute code in isolated environments—all while maintaining strict security boundaries.

**Key Achievement**: Built a secure, tool-using AI agent that can modify codebases while preventing unauthorized system access through Docker isolation and user confirmation workflows.

## ✨ Features

### Agentic Intelligence

- **Multi-step Planning**: Powered by Google Gemini Pro with function calling to break down complex development tasks
- **Autonomous Tool Selection**: Intelligently chooses from 7+ tools based on task requirements
- **Context Awareness**: Maintains conversation history to handle follow-up requests

### Development Tools

- **File System Operations**: Read, write, and list files within project scope
- **Git Integration**: Check status, view diffs, and commit changes
- **Web Research**: DuckDuckGo integration for searching documentation and solutions
- **Python Execution**: Run and test code with full output capture

### Security & Safety

- **Sandboxed Execution**: All Python code runs in isolated Docker containers with:
  - No network access
  - Read-only filesystem mounts
  - Memory and CPU limits (512MB, 50% CPU)
  - Path traversal prevention
- **User Confirmation**: Prompts before destructive operations (file writes, commits)
- **Input Validation**: Sanitizes file paths and validates Python file extensions

### User Experience

- **Rich CLI Interface**: Beautiful terminal UI with Markdown rendering
- **Real-time Feedback**: Streaming responses with proper code highlighting
- **Clear Error Messages**: Helpful context for debugging issues

## 🛠️ Tech Stack

**Core Technologies**

- Python 3.11+ with type hints (Pyright strict mode)
- Google Gemini Pro API (function calling)
- Docker SDK for secure code execution
- `uv` for fast dependency management

**Key Libraries**

- `google-generativeai` - AI model integration
- `docker` - Container orchestration
- `rich` - Terminal UI rendering
- `duckduckgo-search` - Web research
- `beautifulsoup4` - HTML parsing

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- [Docker](https://www.docker.com/get-started) (running daemon required)
- [uv](https://github.com/astral-sh/uv) package manager
- [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/felixsolom/honey-comb.git
cd honey-comb
```

2. **Install dependencies**

```bash
uv venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
uv pip install -r pyproject.toml
```

3. **Configure environment**
Create `.env` in the project root:
GEMINI_API_KEY="your_api_key_here"

4. **Set up Docker sandbox**
Build the sandbox image:

```bash
docker build -t honey-comb-sandbox .
```

### Configuration

The agent operates on a target codebase specified in `config.py`:

```bash
config.py
WORKING_DIR = "./calculator" # Change to your project path
```

**Options:**

- Use the default `./calculator` directory (included)
- Point to your own project: `WORKING_DIR = "/path/to/your/project"`

### Usage

Start the interactive agent:

```bash
python main.py
```

**Example commands:**

```bash
Add a new function to calculate fibonacci numbers
Run the tests and fix any failures
Search for how to implement LRU cache in Python
Show me the git diff
```

## 📁 Project Structure

```bash
honey-comb/
├── agent.py # Core agent logic with tool calling
├── tools.py # Tool implementations (file ops, git, search)
├── config.py # Configuration settings
├── main.py # CLI entry point
├── Dockerfile # Sandbox container definition
├── calculator/ # Example project
└── .env # API keys (not in repo)
```

## 🏗️ Architecture Highlights

**Agentic Loop**: Request → Planning → Tool Selection → Execution → Response → Repeat

**Security Layers**:

1. Path validation (prevents directory traversal)
2. Docker isolation (filesystem + network)
3. Resource limits (memory, CPU, timeout)
4. User confirmation gates

**Error Handling**: Comprehensive exception catching with helpful messages for API errors, Docker issues, and file operations

## 🔮 Roadmap

**Implemented:**

- ✅ Secure sandboxed Python execution
- ✅ Multi-tool agent with function calling
- ✅ Git operations with user confirmation
- ✅ Web search integration
- ✅ Rich terminal UI with Markdown

**Future Enhancements:**

- [ ] Project scaffolding from templates
- [ ] Automated test generation and execution
- [ ] Conversation history persistence
- [ ] YAML-based configuration
- [ ] Support for more languages (Node.js, Go)
- [ ] VS Code extension integration

## 🤝 Contributing

This is a portfolio project, but suggestions are welcome! Feel free to:

- Open issues for bugs or feature ideas
- Submit PRs with improvements
- Share how you've used it in your own projects

## 📝 License

MIT License - see [LICENSE](LICENSE) for details

## 👤 Author

**Felix Solomon**

- GitHub: [@felixsolom](https://github.com/felixsolom)

---

**⭐ If you found this project interesting, please give it a star!**
