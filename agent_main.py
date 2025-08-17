
from smolagents import CodeAgent
from note_tool import search_my_notes
import os
from keys import RunningApiKey
from smolagents import OpenAIServerModel
from smolagents import DuckDuckGoSearchTool,VisitWebpageTool,FinalAnswerTool
def main():
    print(" Your AI Assistant is ready!")
    RunningApiKey()
    model = OpenAIServerModel(
        model_id = "gemini-2.0-flash",
        api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.environ["GEMINI_API_KEY"]
    )
    agent = CodeAgent(
    tools = [search_my_notes,DuckDuckGoSearchTool(),VisitWebpageTool(),FinalAnswerTool()],
    model=model,
    max_steps=20,
    planning_interval=2
    )
 
    converstion_history = []
    print("I can search through your personal notes. Just ask me anything.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit','exit','bye']:
            print("Goodbye!  ")
            break 
        try:
            if converstion_history:
                context = "Previous conversation context:\n"
                recent_history = converstion_history[-4:]
                for exchange in recent_history:
                    context+= f"User:{exchange['user']} \n Assistant:{exchange['assistant']}\n"
                context+=f"\nCurrent question:{user_input}"
                full_input = context
            else:
                full_input = user_input
            response = agent.run(full_input)
            print(f"Assistant: {response}")
            converstion_history.append({
                'user':user_input,
                'assistant':str(response)
            }
            )
        except Exception as e:
            print(f"Sorry, I had an error:{e}")
if __name__ == "__main__":
    main()
