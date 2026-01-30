"""
OpenRouter AI Integration Module
Supports free tier models via OpenRouter
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class AIClient:
    def __init__(self):
        api_key = os.getenv('OPENROUTER_API_KEY')
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        # OpenRouter uses OpenAI-compatible API
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        self.conversation_history = []
        
        # Use a free model from OpenRouter
        # Options: google/gemma-2-9b-it:free, meta-llama/llama-3.2-3b-instruct:free, etc.
        self.model = os.getenv('AI_MODEL', 'google/gemma-2-9b-it:free')
        
        self.system_prompt = """You are a helpful AI assistant running on a retro 90s BBS (Bulletin Board System). 
Keep your responses conversational and friendly. You can use some retro internet slang and emoticons if appropriate. 
Keep responses concise but informative - remember, this is a text-based terminal interface!
You support multiple languages including English, Russian (Cyrillic), and others. 
Respond in the same language the user writes to you."""
    
    def chat(self, user_message):
        """Send a message to AI and get a response"""
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Prepare messages with system prompt
            messages = [{"role": "system", "content": self.system_prompt}] + self.conversation_history
            
            # Get response from OpenRouter
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
                # OpenRouter-specific headers
                extra_headers={
                    "HTTP-Referer": "https://github.com/yourusername/aibbs",
                    "X-Title": "AI BBS"
                }
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error communicating with AI: {str(e)}"
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
    
    def get_conversation_length(self):
        """Get number of messages in conversation"""
        return len(self.conversation_history)
    
    def get_model_name(self):
        """Get the current model name"""
        return self.model

