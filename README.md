# 🤖 AI Code Generator

## 📚 Project Overview
This application is a **Streamlit-based AI tool** for generating programming code using **Google's Gemini API**. It provides context-aware code generation and explanations, allowing users to dynamically generate short-commented programming code based on their queries. The application uses conversational history to refine subsequent responses, making it highly interactive and conversational—similar to ChatGPT.

## ✨ Features
* 🧠 **Context-Aware Code Generation**: Generates code based on user prompts and incorporates the context of previous interactions for improved accuracy.
* 📝 **Code Explanation**: Provides a simple explanation of the generated code, focusing on functionality and key components.
* 🌐 **Multi-Language Support**: Supports popular programming languages, including Python, Java, C, and C++.
* 💻 **Interactive User Interface**: Built with Streamlit for a clean and responsive design.
* 🔗 **Social Media Integration**: Includes links to connect with the creator through LinkedIn, Instagram, and WhatsApp.

## 🛠️ Technologies Used
* 🚀 **Streamlit**: For creating the web application interface.
* 🧩 **Google Generative AI**: To generate programming code and explanations.
* 🔒 **Python dotenv**: For managing environment variables securely.

## ⚙️ Installation and Setup

### 📋 Prerequisites
* 🐍 Python 3.8 or higher.
* 🔑 A valid **Google API Key** for accessing the Gemini model.

### 📥 Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root folder and add your **Google API Key**:
   ```plaintext
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Run the application locally:
   ```bash
   streamlit run app.py
   ```

## 📱 Usage
1. 🌐 Open the application in your browser (default: `http://localhost:8501`).
2. ⌨️ Enter a coding task in the prompt area and select the programming language.
3. 👀 View generated code and explanations, along with your previous queries in the chat history.
4. 🔄 If the prompt specifies **"take input from user"**, the generated code will be interactive and accept user inputs dynamically.

## 📂 File Structure
* 📄 **app.py**: Main application script.
* 📋 **requirements.txt**: Lists all dependencies required to run the application.
* 🔐 **.env**: Stores environment variables (e.g., `GOOGLE_API_KEY`).

## 🚀 Future Enhancements
* ➕ Add support for additional programming languages.
* 🎨 Improve UI/UX with more responsive design elements.
* 💬 Enhance conversational context handling for complex queries.

## 🌟 Connect With Us
Feel free to reach out or follow for updates:
* 👔 **LinkedIn**: [Connect with Vitthal Sawant](https://www.linkedin.com/in/vitthal-sawant-maharastra01/)
* 📸 **Instagram**: [Follow on Instagram](https://www.instagram.com/vitthal_sawant__/)
* 📱 **WhatsApp**: [Message on WhatsApp](https://wa.me/+918308075485)
* 📧 **Email**: vitthslsawant300@gmail.com

## 🔗 Live Project
Try out the application here: [Code Generator AI](https://codegeneratorai.streamlit.app/)

## 🔍 Technical Analysis

I'll analyze the code to explain the LLM model being used and other important aspects of your application.

Looking at your code.py file, I can see that you're using Google's Gemini AI model. Let me break down the key components:

### 1. **LLM Model: Gemini 2.0 Flash**
```python
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config
)
```
- You're using the `gemini-2.0-flash` model, which is Google's latest generative AI model
- This model is optimized for:
  - Fast response times (hence "flash" in the name)
  - Code generation and explanation
  - Context-aware responses
  - Handling multiple programming languages

### 2. **Model Configuration**
```python
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 1024,
}
```
- `temperature`: 0.7 (controls creativity/randomness in responses)
- `top_p` and `top_k`: 1 (controls diversity of responses)
- `max_output_tokens`: 1024 (maximum length of generated responses)

### 3. **Key Features of Your Application:**

#### a) **Context-Aware Code Generation:**
```python
def generate_code_with_context(prompt, language, chat_history):
    # Uses previous conversation history to maintain context
    context = "\n".join([f"Q: {entry['prompt']}\nA: {entry['code']}" for entry in chat_history])
```
- Maintains conversation history
- Generates code based on previous interactions
- Supports multiple programming languages (C, C++, Java, Python)

#### b) **Code Explanation Feature:**
```python
def explain_code_with_context(code, language, chat_history):
    # Explains generated code in simple terms
    explanation_prompt = f"Based on the previous conversation:\n{context}\nNow, explain this {language} code..."
```
- Provides explanations for generated code
- Maintains context across explanations
- Focuses on main functionality and key components

### 4. **User Interface Features:**
- Clean Streamlit interface with sidebar navigation
- Social media integration (LinkedIn, Instagram, WhatsApp)
- Language selection dropdown
- Chat history display
- Code display with syntax highlighting

### 5. **Session State Management:**
```python
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'input_key' not in st.session_state:
    st.session_state['input_key'] = 0
```
- Maintains conversation history across reruns
- Manages input field state
- Preserves user context

### 6. **Error Handling:**
```python
try:
    # Code generation/explanation logic
except Exception as e:
    return f"Error generating code: {str(e)}"
```
- Graceful error handling for API calls
- User-friendly error messages
- Prevents application crashes

### 7. **Environment Configuration:**
```python
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
```
- Secure API key management using .env file
- Environment variable loading
- API key validation

### 8. **Dependencies (from requirements.txt):**
- `streamlit>=1.28.0`: Modern web interface
- `google-generativeai>=0.3.0`: Gemini AI integration
- `python-dotenv>=1.0.0`: Environment variable management
- Additional UI enhancement packages:
  - `streamlit-option-menu>=0.3.6`
  - `streamlit-extras>=0.4.0`
  - `pillow>=10.0.0` (for image handling)
  - `watchdog>=3.0.0` (for hot reloading)

This application is particularly useful for:
1. Learning programming concepts
2. Getting code explanations
3. Generating code snippets with context
4. Understanding code functionality
5. Maintaining conversation history for better context
6. Supporting multiple programming languages
7. Providing a user-friendly interface for AI-powered code generation

The combination of Gemini AI with Streamlit creates a powerful, interactive coding assistant that can help users learn and understand code better while maintaining context across interactions.

## 📄 License
This project is open source and available under the MIT License. ❤️

## 👥 Contributing
Contributions are welcome and greatly appreciated! If you're interested in improving this project, here's how you can help:

1. 🍴 Fork the repository
2. 🔧 Create your feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Commit your changes (`git commit -m 'Add some amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔁 Open a Pull Request

Whether you're fixing bugs, improving documentation, or adding new features, your contributions will make this project better for everyone! Feel free to reach out to Vitthal Sawant with any questions or ideas.

Let's build something amazing together! 🚀
