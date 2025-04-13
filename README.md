# AI Code Generator with Contextual Understanding

![AI Code Generator Banner](https://raw.githubusercontent.com/username/repository/main/images/banner.png)

## Project Overview
This application is a **Streamlit-based AI tool** for generating programming code using **Google's Gemini API**. It provides context-aware code generation and explanations, allowing users to dynamically generate short-commented programming code based on their queries. The application uses conversational history to refine subsequent responses, making it highly interactive and conversational—similar to ChatGPT.

<div align="center">
  <img src="https://raw.githubusercontent.com/username/repository/main/images/app_overview.png" alt="Application Overview" width="700">
</div>

## Features
* **Context-Aware Code Generation**: Generates code based on user prompts and incorporates the context of previous interactions for improved accuracy.
* **Code Explanation**: Provides a simple explanation of the generated code, focusing on functionality and key components.
* **Multi-Language Support**: Supports popular programming languages, including Python, Java, C, and C++.
* **Interactive User Interface**: Built with Streamlit for a clean and responsive design.
* **Social Media Integration**: Includes links to connect with the creator through LinkedIn, Instagram, and WhatsApp.

<div align="center">
  <img src="https://raw.githubusercontent.com/username/repository/main/images/features_diagram.png" alt="Features Diagram" width="600">
</div>

## Technologies Used
* **Streamlit**: For creating the web application interface.
* **Google Generative AI**: To generate programming code and explanations.
* **Python dotenv**: For managing environment variables securely.

<div align="center">
  <img src="https://raw.githubusercontent.com/username/repository/main/images/tech_stack.png" alt="Technology Stack" width="500">
</div>

## Installation and Setup

### Prerequisites
* Python 3.8 or higher.
* A valid **Google API Key** for accessing the Gemini model.

### Steps to Install
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

<div align="center">
  <img src="https://raw.githubusercontent.com/username/repository/main/images/setup_diagram.png" alt="Setup Process" width="550">
</div>

## Usage
1. Open the application in your browser (default: `http://localhost:8501`).
2. Enter a coding task in the prompt area and select the programming language.
3. View generated code and explanations, along with your previous queries in the chat history.
4. If the prompt specifies **"take input from user"**, the generated code will be interactive and accept user inputs dynamically.

## Application Screenshots

<div align="center">
  <p><b>Initial Interface</b></p>
  <img src="https://raw.githubusercontent.com/username/repository/main/images/initial_interface.png" alt="Initial Interface" width="700">
  <br><br>
  
  <p><b>Code Generation Example</b></p>
  <img src="https://raw.githubusercontent.com/username/repository/main/images/code_generation.png" alt="Code Generation Example" width="700">
  <br><br>
  
  <p><b>Interactive Input Example</b></p>
  <img src="https://raw.githubusercontent.com/username/repository/main/images/interactive_input.png" alt="Interactive Input Example" width="700">
  <br><br>
  
  <p><b>Conversation History</b></p>
  <img src="https://raw.githubusercontent.com/username/repository/main/images/conversation_history.png" alt="Conversation History" width="700">
</div>

## File Structure
* **app.py**: Main application script.
* **requirements.txt**: Lists all dependencies required to run the application.
* **.env**: Stores environment variables (e.g., `GOOGLE_API_KEY`).
* **images/**: Directory containing screenshots and images for documentation.

## Future Enhancements
* Add support for additional programming languages.
* Improve UI/UX with more responsive design elements.
* Enhance conversational context handling for complex queries.
* Implement code execution environment for testing generated code.
* Add ability to save generated code snippets to files.

<div align="center">
  <img src="https://raw.githubusercontent.com/username/repository/main/images/roadmap.png" alt="Future Roadmap" width="600">
</div>

## Connect With Us
Feel free to reach out or follow for updates:

<div align="center">
  <a href="https://linkedin.com/in/vitthal-sawant">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://instagram.com/vitthal_sawant">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
  </a>
  <a href="https://wa.me/1234567890">
    <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>
</div>

## License
This project is open source and available under the MIT License.

<div align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
</div>
