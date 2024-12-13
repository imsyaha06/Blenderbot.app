# import streamlit as st
# from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# # Load the saved BlenderBot model and tokenizer
# model_name = "./blenderbot-400M-distill"
# tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
# model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# # Function to generate chatbot response
# def get_response(input_text):
#     inputs = tokenizer(input_text, return_tensors="pt")
#     reply_ids = model.generate(**inputs)
#     return tokenizer.decode(reply_ids[0], skip_special_tokens=True)

# # Streamlit App
# st.title("Chatbot App with BlenderBot")
# st.write("This chatbot is powered by the BlenderBot model.")

# # Input text box for user query
# user_input = st.text_input("You:", placeholder="Type your message here...")

# if st.button("Send"):
#     if user_input.strip():
#         with st.spinner("Chatbot is responding..."):
#             try:
#                 # Generate response
#                 chatbot_response = get_response(user_input)
#                 st.write(f"**Chatbot:** {chatbot_response}")
#             except Exception as e:
#                 st.error(f"An error occurred: {e}")
#     else:
#         st.warning("Please type a message to send.")









import streamlit as st
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the saved BlenderBot model and tokenizer
model_name = "./blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Function to generate chatbot response
def get_response(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    reply_ids = model.generate(**inputs)
    return tokenizer.decode(reply_ids[0], skip_special_tokens=True)

# Sidebar Information
with st.sidebar:
    st.title("About the Chatbot")
    st.write(
        """
        - **Model:** BlenderBot-400M
        - **Purpose:** General conversational AI
        - **Technology:** Built using Transformers by Hugging Face
        - **Developer:** Sumbal Haroon!
        """
    )

# Main Chatbot Interface
st.title("Chatbot App with BlenderBot 💬")
st.write("This chatbot is powered by the BlenderBot model. Have a friendly chat!")

# Input text box for user query
user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send"):
    if user_input.strip():
        with st.spinner("Chatbot is responding..."):
            try:
                # Generate response
                chatbot_response = get_response(user_input)
                st.write(f"**Chatbot:** {chatbot_response}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a message to send.")
        
 
 
 
 




# import streamlit as st
# from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# # Load the saved BlenderBot model and tokenizer
# model_name = "./blenderbot-400M-distill"
# tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
# model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# # Function to generate chatbot response
# def get_response(input_text):
#     inputs = tokenizer(input_text, return_tensors="pt")
#     reply_ids = model.generate(**inputs)
#     return tokenizer.decode(reply_ids[0], skip_special_tokens=True)

# # Streamlit App
# st.set_page_config(page_title="Friendly Chatbot", layout="wide")
# st.title(st.image(
#         "LetsChat.png",
#          use_column_width=True,) "Friendly Chatbot")
# st.write("This chatbot is here to chat with you in a friendly way. Feel free to ask anything!")

# # Sidebar Information
# with st.sidebar:
#     st.title("About the Chatbot")
#     st.write(
#         """
#         - **Model:** BlenderBot-400M
#         - **Purpose:** General conversational AI
#         - **Technology:** Built using Transformers by Hugging Face
#         - **Developer:** You!
#         """
#     )
#     st.image(
#         "https://cdn.pixabay.com/photo/2023/03/01/12/20/ai-robot-7822043_960_720.jpg",
#         caption="Your friendly chatbot companion",
#         use_column_width=True,
#     )

# # # Main Chat Interface
# # col1, col2 = st.columns([1, 3])

# # with col1:
# #     st.image(
# #         "LetsChat.png",
# #         # caption="Let's chat!",
# #         use_column_width=True,
# #     )

# # with col2:
# #     user_input = st.text_input("You:", placeholder="Type your message here...")

#     if st.button("Send"):
#         if user_input.strip():
#             with st.spinner("Chatbot is responding..."):
#                 try:
#                     # Generate response
#                     chatbot_response = get_response(user_input)
#                     st.write(f"**Chatbot:** {chatbot_response}")
#                 except Exception as e:
#                     st.error(f"An error occurred: {e}")
#         else:
#             st.warning("Please type a message to send.")

# # Footer
# st.markdown("---")
# st.markdown("💬 **Enjoy chatting with your friendly AI!** Powered by [Streamlit](https://streamlit.io) and [Hugging Face](https://huggingface.co).")
