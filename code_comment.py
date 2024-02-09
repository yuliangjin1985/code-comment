from openai import OpenAI


#Internally it will retrieve the env vironment: os.environ.get("OPENAI_API_KEY")
client = OpenAI()

def generate_comment(code_line):
    model_engine = 'gpt-3.5-turbo'
    p = f'Please provide appropriate code comments for the given code snippet. Here is the code:""{code_line}""'

    completion = client.chat.completions.create(
        model=model_engine,
        messages=[
            {"role": "user", "content": p}
        ])
    return completion.choices[0].message.content

def comment_program(file_path):
    commented_program = []
    with open(file_path, 'r') as file:
        for line in file:
            if len(line) < 100: 
                commented_program.append(f"{line} \n")
                continue
            comment = generate_comment(line)
            commented_program.append(f"{line}  # {comment}\n")
    return commented_program

file_path = 'program.txt'

commented_program = comment_program(file_path)

for commented_line in commented_program:
    if len(commented_line) > 100:
        print(commented_line)
        
