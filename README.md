# grammarbot-py

Grammar Bot provides spelling and grammar check. Signup for an API key at
https://www.grammarbot.io/ for increased usage limits. The API still works
with no key, but the daily usage limit is lower.

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
client = GrammarBotClient()

# or, signup for an API Key to get higher usage limits here: https://www.grammarbot.io/
client = GrammarBotClient(api_key='my_api_key_here') # GrammarBotClient(api_key=my_api_key_here)

# you can even set the base URI to a different server
client = GrammarBotClient(base_uri='http://backup.grammarbot.io:80')

# Analyzing the text
# ==================

# There is only one method to perform the analysis, viz. GrammarBotClient.check
# method.

text = 'I cant remember how to go their'

# check the text, returns GrammarBotApiResponse object
res = client.check(text) # GrammarBotApiResponse(matches=[GrammarBotMatch(offset=2, length=4, rule={'CANT'}, category={'TYPOS'}), GrammarBotMatch(offset=26, length=5, rule={'CONFUSION_RULE'}, category={'TYPOS'})])

# you can even specify the language of input text
res = client.check(text, 'en-GB')

# Inspecting the GrammarBotApiResponse object
# ===========================================

# check detected language
res.detected_language # "en-US"

# check if the result is incomplete
res.result_is_incomplete # False

# see the suggestions / corrections suggested by the GrammarBot API
# returns a list of GrammarBotMatch objects describing each replacement
res.matches # [GrammarBotMatch(offset=2, length=4, rule={'CANT'}, category={'TYPOS'}), GrammarBotMatch(offset=26, length=5, rule={'CONFUSION_RULE'}, category={'TYPOS'})]


# Inspecting the GrammarBotMatch object
# =====================================

match0 = match[0] # GrammarBotMatch(offset=2, length=4, rule={'CANT'}, category={'TYPOS'})


# get replacement information
match0.replacement_offset # 2
match0.replacement_length # 4

# get suggested replacements
match0.replacements # ["can't", 'cannot']

# get list of possible correct sentences after applying the replacements
match0.corrections # ["I can't remember how to go their", 'I cannot remember how to go their']


# get the rules, type and category information of the match
match0.rule # 'CANT'
match0.category # 'TYPOS'
match0.type # 'Other'

# getting a friendly message regarding the replacement suggestion
match0.message # 'Did you mean "can\'t" or "cannot"?'

# Getting even more information
# =============================

# if the information provided by the class properties is not enough, you can
# always access the complete original JSON response from GrammarBotApiResponse
# object
res.raw_json
```

## API docs

You can see the API documentation here: https://grammarbot-py.readthedocs.io/en/latest/
