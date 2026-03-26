# OpenChat

OpenChat is a chat application that leverages Google's Gemini API for AI-powered interactions.


## Screenshot
![Image](/src/images/0.png)

[Try It Out](https://openchat-xpus.onrender.com/)


## Installation and Testing

### Prerequisites

- **Python 3.x**
- **Git**
- **Pip**

### Clone the Repository

Open your terminal (or Command Prompt on Windows) and run:

```bash
git clone https://github.com/daud0x0/OpenChat.git
cd OpenChat
```

### For Linux and macOS

1. **Create a virtual environment:**

   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Install the requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain Google Gemini API Key:**

   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Set the API key as an environment variable:

     ```bash
     export GOOGLE_API_KEY="YOUR_API_KEY"
     ```

     **Note:** To make this change persistent, add the above line to your `~/.bashrc`, `~/.bash_profile`, or `~/.profile` file.

5. **Run the server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the application:**

   - Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### For Windows

1. **Create a virtual environment:**

   ```cmd
   python -m venv .venv
   ```

2. **Activate the virtual environment:**

   ```cmd
   .\.venv\Scripts\activate
   ```

3. **Install the requirements:**

   ```cmd
   pip install -r requirements.txt
   ```

4. **Obtain Google Gemini API Key:**

   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Set the API key as an environment variable:

     ```cmd
     set GOOGLE_API_KEY="YOUR_API_KEY"
     ```

     **Note:** To make this change persistent, add it to your system environment variables:

     - Go to **Control Panel** > **System and Security** > **System**.
     - Click on **Advanced system settings**.
     - Click on **Environment Variables**.
     - Under **User variables**, click **New**.
     - Enter `GOOGLE_API_KEY` as the variable name and your API key as the variable value.
     - Click **OK** to save.

5. **Run the server:**

   ```cmd
   python manage.py runserver
   ```

6. **Access the application:**

   - Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

**Cheers!**
