# AI Engineering Framework

A production-ready, modular Python framework for building AI-powered applications, agents, Retrieval-Augmented Generation (RAG) systems, and automation workflows.

---

## Overview

The **AI Engineering Framework** is a reusable foundation for developing scalable AI applications. It provides common infrastructure such as configuration management, storage, providers, utilities, exception handling, and base classes so new AI projects can be built consistently and quickly.

Current module:

* **ai-core** – Core framework and reusable infrastructure.

---

## Features

* Modular architecture
* Reusable base classes
* AI provider abstraction
* Configuration management
* Centralized constants
* Structured exception handling
* File and storage management
* Utility helpers
* Unit-tested components
* Production-ready project structure

---

## Project Structure

```text
ai-core/
├── src/
│   ├── ai/
│   ├── base/
│   ├── config/
│   ├── constants/
│   ├── exceptions/
│   ├── providers/
│   ├── storage/
│   └── utils/
│
├── tests/
│
├── pyproject.toml
├── pytest.ini
├── README.md
├── LICENSE
└── MANIFEST.in
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/techakkena/ai-engineering-framework.git
```

Move into the project:

```bash
cd ai-components/ai-core
```

Install in editable mode:

```bash
pip install -e .
```

---

## Running Tests

Run the complete test suite:

```bash
python -m pytest tests -v
```

Current status:

* **207 / 207 tests passing**

---

## Core Modules

### Base

Reusable abstract classes including:

* BaseAgent
* BaseComponent
* BaseController
* BaseManager
* BaseModel
* BaseRepository
* BaseService

### Configuration

* Environment management
* Settings
* Logging

### Constants

Centralized constants for:

* AI
* API
* Database
* Authentication
* Storage
* Logging

### Providers

AI provider abstraction supporting:

* OpenAI
* Anthropic
* Google
* Azure OpenAI
* Ollama
* Hugging Face

### Storage

* File Storage
* Cache Manager
* Backup Manager
* Upload Manager
* Vector Storage
* Storage Manager

### Utilities

* Date & Time
* File
* Hash
* JSON
* Path
* String
* Validation
* ID Generation

### Exceptions

Comprehensive framework-specific exception hierarchy with standardized error codes.

---

## Development Workflow

Install dependencies:

```bash
pip install -e .
```

Run tests:

```bash
python -m pytest tests -v
```

---

## Roadmap

### Completed

* ✅ ai-core

### Planned

* ai-chat
* ai-rag
* ai-agents
* ai-workflows
* ai-api
* ai-customer-agent

---

## Version

Current Release:

**v0.1.0-core-tested**

---

## Author

**TECHAKKENA**

---

## License

This project is licensed under the MIT License.
