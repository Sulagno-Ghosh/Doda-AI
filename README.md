# Doda-AI

# AI Assistant for Home Automation

![AI Assistant](demo.gif)

## Overview

This project is a Flask-based AI assistant that can control lights and perform various day-to-day tasks. It's designed to make your life easier by providing an interactive interface for home automation and general assistance. This README will guide you through setting up and using the AI Assistant.

## Features

- **Voice Control:** The AI Assistant can understand voice commands and execute corresponding actions.
- **Light Control:** You can control your smart lights with simple voice commands or through the web interface.
- **Task Automation:** Perform tasks like setting reminders, sending emails, or searching the web using natural language commands.
- **User-Friendly Interface:** The web interface provides an intuitive and responsive design using HTML, CSS, and JavaScript.
- **Customization:** Easily add new voice commands and actions to extend the assistant's capabilities.

## Technologies Used

- **Flask:** A lightweight web framework for building the backend.
- **HTML, CSS, JavaScript:** Frontend technologies for creating the web interface.
- **Speech Recognition:** To process voice commands.
- [Smart Light API]: Integrate your smart light system with the assistant.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Virtual environment for isolating dependencies (optional but recommended).

### Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```
## Configuration

1. Configure your smart lights by modifying the `config.py` file.
2. Set up any additional APIs or services you want to integrate with in the same file.

## Usage

1. Run the Flask application:

```bash
python app.py
```
Open your web browser and navigate to http://localhost:5000 to access the AI Assistant.
You can now interact with the assistant using both text and voice commands.

