import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    st.error("API key not found. Please check your .env file.")
    st.stop()
genai.configure(api_key=GOOGLE_API_KEY)

# Set default parameters for the model
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 1024,
}

# Initialize the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config
)

# Function to generate code using Gemini, considering context
def generate_code_with_context(prompt, language, chat_history):
    try:
        # Prepare the chat history as context
        context = "\n".join([f"Q: {entry['prompt']}\nA: {entry['code']}" for entry in chat_history])
        formatted_prompt = f"Based on the previous conversation:\n{context}\nNow, generate {language} code for the following task with short learning comments only. Do not include redundant code block markers or explanations: {prompt}"
        response = model.generate_content(formatted_prompt)
        return response.text.strip() if response.text else "No code generated."
    except Exception as e:
        return f"Error generating code: {str(e)}"

# Function to explain generated code
def explain_code_with_context(code, language, chat_history):
    try:
        # Prepare the chat history as context
        context = "\n".join([f"Q: {entry['prompt']}\nA: {entry['explanation']}" for entry in chat_history])
        explanation_prompt = f"Based on the previous conversation:\n{context}\nNow, explain this {language} code in simple terms, focusing on its main functionality and key components: {code}"
        response = model.generate_content(explanation_prompt)
        return response.text.strip() if response.text else "Could not generate explanation."
    except Exception as e:
        return f"Error generating explanation: {str(e)}"

# Streamlit interface setup
st.markdown("<h1 style='text-align: center;'>AI Code Generator</h1>", unsafe_allow_html=True)
st.write("🚀 Welcome to Your AI Coding Assistant! Enter your prompt and select a programming language to generate context-aware, short-commented code.")

# Sidebar for language selection and social media links
with st.sidebar:
    # Language selection
    language = st.selectbox(
        "Select Programming Language",
        ["C", "C++", "Java", "Python"]
    )
    
    # Add a separator
    st.markdown("---")
    
    # Social media section
    st.markdown("### Connect with Us")
    
    # Social media links with SVG icons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            f'<a href="https://www.linkedin.com/in/vitthal-sawant-maharastra01/" target="_blank">'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#0077B5"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>'
            f'</a>',
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f'<a href="https://www.instagram.com/vitthal_sawant__/" target="_blank">'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#E4405F"><path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06l.045.03zm0 3.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.76 6.162 6.162 6.162 3.405 0 6.162-2.76 6.162-6.162 0-3.405-2.76-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.646-1.44-1.44 0-.794.646-1.439 1.44-1.439.793-.001 1.44.645 1.44 1.439z"/></svg>'
            f'</a>',
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            f'<a href="https://wa.me/+918308075485" target="_blank">'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#25D366"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>'
            f'</a>',
            unsafe_allow_html=True
        )

# Initialize session state for chat history and input key
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'input_key' not in st.session_state:
    st.session_state['input_key'] = 0

# Prompt input field
prompt = st.text_area(
    "Enter your prompt here:",
    height=100,
    key=f"prompt_text_{st.session_state['input_key']}"
)

# Generate button
if st.button("🚀 Generate Code"):
    if prompt:
        with st.spinner("Generating code..."):
            # Use chat history for context
            chat_history = st.session_state['chat_history']
            
            # Generate code and explanation with context
            code_output = generate_code_with_context(prompt, language, chat_history)
            explanation = explain_code_with_context(code_output, language, chat_history)
            
            # Add the result to chat history
            st.session_state['chat_history'].insert(0, {
                'prompt': prompt,
                'code': code_output,
                'explanation': explanation
            })
            
            # Increment input key to clear the input field
            st.session_state['input_key'] += 1
            st.rerun()
    else:
        st.warning("Please enter a prompt.")

# Display chat history with context
for message in st.session_state['chat_history']:
    st.markdown("### Your Question:")
    st.write(message['prompt'])
    
    st.markdown("### Generated Code:")
    st.code(message['code'], language.lower())
    
    st.markdown("### Code Explanation:")
    st.write(message['explanation'])
    
    st.markdown("---")