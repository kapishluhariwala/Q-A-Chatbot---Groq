# Q&A Chatbot using Groq

Welcome to the **AI Chatbot** repository! This project demonstrates a chatbot application powered by **Groq** for efficient AI processing and **Streamlit** for a seamless user interface.

---

## Features

- **Basic Conversational AI:** Powered by Groq.
- **Streamlit-based UI:** A clean, intuitive interface for interacting with the chatbot.

---

## Getting Started

Follow these steps to set up and run the chatbot on your local machine.

### Prerequisites

- Python 3.10+
- Groq SDK installed ([Groq Documentation](https://www.groq.com/documentation))
- Streamlit installed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kapishluhariwala/chatbot-with-groq.git
   cd chatbot-with-groq
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Verify Groq setup: Ensure that your Groq system is properly configured. Refer to [Groq's setup guide](https://www.groq.com/documentation) for more details.

---

## Running the Chatbot

1. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to:

   ```
   http://localhost:8501
   ```

3. Obtain a Groq API Key:
4. 
   Follow the steps below to get your Groq API key for integrating with the chatbot:
   - Sign in to your Groq account on the [Groq](https://console.groq.com/keys).
   - Navigate to the **API Keys** section in your dashboard.
   - Click on **Generate New Key** and provide a name for your key (e.g., `ChatbotApp`).
   - Copy the API key and keep it secure. You will use this key to authenticate requests.
   - Paste the API key in the UI.

5. Interact with the chatbot through the user-friendly interface.

---

## File Structure

```plaintext
.
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation

```

---

## How It Works

### Backend (Groq)

- The chatbot leverages Groq's high-performance processing for real-time conversational AI.
- Groq handles model inference, ensuring rapid response times and low latency.

### Frontend (Streamlit)

- Streamlit provides an interactive UI where users can type messages and view responses in real time.
- The interface includes:
  - Input box for user queries
  - Display area for chatbot responses
  - Customizable LLM options

---

## Contact

If you have any questions, feel free to reach out:

- **Kapish Luhariwala:** [kapishluhariwala@hotmail.com](mailto\:kapishluhariwala@hotmail.com)
- **GitHub:** [@kapishluhariwala](https://github.com/kapishluhariwala)

