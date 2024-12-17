# from openai import AzureOpenAI
# import os

# api_version = "2024-08-01-preview"

# client = AzureOpenAI(
#     api_version=api_version,
#     api_key=os.environ["AZURE_OPENAI_API_KEY"],
#     azure_endpoint="https://langrag.openai.azure.com/",
# )

# completion = client.chat.completions.create(
#     model="gpt-4",  
#     messages=[
#         {
#             "role": "user",
#             "content": "hello",
#         },
#     ],
# )
# print(completion)

from openai import AzureOpenAI
import os
import io
import base64

# Test GPT-4
def test_chat():
    client = AzureOpenAI(
        api_version="2024-08-01-preview",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        azure_endpoint="https://langrag.openai.azure.com/"
    )

    completion = client.chat.completions.create(
        model="gpt-4",  
        messages=[
            {
                "role": "user",
                "content": "hello",
            },
        ],
    )
    print("Chat completion:", completion)

# Test Text-to-Speech
def test_tts():
    client = AzureOpenAI(
        api_version="2024-08-01-preview",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        azure_endpoint="https://langrag.openai.azure.com/"
    )

    try:
        speech = client.audio.speech.create(
            model="tts-1-hd",  # Try different model name
            voice="nova",
            input="Hello, I am your AI therapist."
        )
        
        # Test audio generation
        audio_data = io.BytesIO()
        speech.stream_to_file(audio_data)
        audio_base64 = base64.b64encode(audio_data.getvalue()).decode('utf-8')
        print("TTS successful, audio length:", len(audio_base64))
        
    except Exception as e:
        print("TTS Error:", e)

if __name__ == "__main__":
    print("Testing Chat Completion...")
    test_chat()
    print("\nTesting Text-to-Speech...")
    test_tts()

