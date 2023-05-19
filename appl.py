import google.generativeai as palm
from subprocess import run, CalledProcessError
from sys import argv

try:
    run(['cls'])
except FileNotFoundError:
    try:
        run(['clear'])
    except FileNotFoundError:
        pass
    except CalledProcessError:
        pass
except CalledProcessError:
    try:
        run(['clear'])
    except FileNotFoundError:
        pass
    except CalledProcessError:
        pass

try:
    code = open(argv[1], "r").read()
except FileNotFoundError:
    print("No such file '" + argv[1] + "'")
    exit(1)
except IndexError:
    print("Usage:\n\n\tpython3 appl.py <filename.appel>\n")
    exit(1)

palm.configure(api_key="Get your API key at Google MakerSuite and paste it here")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.1,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    # 'safety_settings': [{"category":"LW","threshold":1},{"category":"OW","threshold":1},{"category":"QW","threshold":2},{"category":"NW","threshold":2},{"category":"MW","threshold":2},{"category":"KW","threshold":2}],
    'safety_settings': [],
}
prompt = f"""You are an advanced AI code interpreter, able to run code with any syntax. You only say what the code would output, not an explanation or a summary.

Run this code:
```
{code}
```
"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)
