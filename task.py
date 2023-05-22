from robotics import Robot
import constants 
import re
from datetime import datetime
import openai

robot = Robot(constants.bot_name,True)


def introduce_yourself(SCIENTISTS):
    robot.say_hello(SCIENTISTS)
    
def wikipedia(page,SCIENTISTS):
    for scientist in SCIENTISTS:
        paragraph = robot.open_webpage(page+scientist,scientist)
        date_pattern = r"\b\d{1,2} \w+ \d{4}\b"
        matches = re.findall(date_pattern, paragraph)
        age(matches)
        print(paragraph)
        print(constants.dashes)
        #run_ai(scientist)

def age(matches):
    date_of_birth = matches[0]
    date_of_death = matches[1]
    # Define the date format
    date_format = "%d %B %Y"
    birth_date = datetime.strptime(date_of_birth, date_format)
    death_date = datetime.strptime(date_of_death, date_format)

    age = death_date.year - birth_date.year

    if death_date.month < birth_date.month:
        age -= 1
    elif death_date.month == birth_date.month and death_date.day < birth_date.day:
        age -= 1

    print(constants.age_text+str(age))

def run_ai(scientist):
    openai.api_key = 'INSERT_YOUR_API_KEY_HERE'
    model_engine = "text-davinci-002"
    prompt = "make a joke about "+scientist
    # Set the number of completions
    n = 1
    # Set the temperature
    temperature = 0.5
    # Set the max length of the completion
    max_tokens = 1024
    # Set the top_p
    top_p = 1
    # Set the frequency penalty
    frequency_penalty = 0
    # Set the presence penalty
    presence_penalty = 0
    # Set the best_of
    best_of = 1
    # Set the stop
    stop = None
    completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    n=n,
    max_tokens=max_tokens,
    temperature=temperature,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty,
    best_of=best_of,
    stop=stop
    )
    for completion in completions.choices:
        print(completion.text)

def main():
    introduce_yourself(constants.SCIENTISTS)
    wikipedia(constants.page,constants.SCIENTISTS)
    exit()

if __name__ == "__main__":
    main()
