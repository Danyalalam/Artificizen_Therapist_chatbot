# Therapist Chatbot

This project is a therapist chatbot designed to provide mental health support. The chatbot uses natural language processing to understand and respond to user inputs.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7 or higher**
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/Danyalalam/Artificizen_Therapist_chatbot.git
cd Therapist_chatbot
```

### 2. Create a Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```bash
touch .env
```

## Running the Chatbot Locally

Follow these steps to start the chatbot server and interact with it via your web browser.

### 1. Start the Chatbot Server

Run the following command to start the FastAPI server using uvicorn:

```bash
uvicorn backend:app --reload --host 0.0.0.0 --port 5000
```

- `--reload`: Enables auto-reloading on code changes.
- `--host 0.0.0.0`: Makes the server accessible externally (optional for local development).
- `--port 5000`: Specifies the port number.

### 2. Access the Chatbot

Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to interact with the chatbot.