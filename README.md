# grammarbot-py

## Installation

```sh
pip install grammarbot
```

## Usage

See the example below

```py
# import the client library
from grammarbot import GrammarBotClient

# Creating the client
# ===================
client = GrammarBotClient('API_KEY')

# Analyzing the text
# ==================

# There is only one method to perform the analysis, viz. GrammarBotClient.check
# method.

text = 'I cant remember how to go their'

# check the text, returns GrammarBotApiResponse object
res = client.check(text)

# Inspecting the GrammarBotApiResponse object
# ===========================================

# check detected language
res.detected_language # "en-US"

# check if the result is incomplete
res.result_is_incomplete # False

# see the suggestions / corrections suggested by the GrammarBot API
# returns a list of GrammarBotMatch objects describing each replacement
res.matches

# Inspecting the GrammarBotMatch object
# =====================================

match0 = match[0]

# get replacement information
res.replacement_offset
res.replacement_length

# get suggested replacements
res.replacements

# get list of possible correct sentences after applying the replacements
res.corrections

# get the rules, type and category information of the match
res.rule
res.category
res.type

# getting a friendly message regarding the replacement suggestion
res.message

# Getting even more information
# =============================

# if the information provided by the class properties is not enough, you can
# always access the complete original JSON response from GrammarBotApiResponse
# object
res.raw_json
```

## API docs

You can see the API documentation here: https://grammarbot-py.readthedocs.io/en/latest/
