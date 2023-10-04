import openai
import time

openai.api_key = "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"

def get_summary_for_resume(description):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Summarize the following in bullet points for my resume \n\n"+description,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        if len(response['choices'][0]) > 0:
            points = response['choices'][0]['text'].split("\n")
            s = ""
            # Remove the Bullet point from the response text
            for point in points:
                s += point[1:]+"\n"
            return s
    except openai.error.RateLimitError as e:
        print(f"RateLimitError: {e}")
        print("Continuing without summarization...")
    
    return description

def get_summary_for_projects(description):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Summarize the following in 2 bullet points for my resume \n\n"+description,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        if len(response['choices'][0]) > 0:
            points = response['choices'][0]['text'].split("\n")
            s = ""
            # Remove the Bullet point from the response text
            for point in points:
                s += point[1:]+"\n"
            return s
    except openai.error.RateLimitError as e:
        print(f"RateLimitError: {e}")
        print("Continuing without summarization...")
    
    return description
