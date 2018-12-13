from typing import List
from urllib.parse import urljoin

import requests


class GrammarBotClient:
    """
    A GrammarBot-API wrapper client.
    """

    def __init__(self, base_uri: str='http://api.grammarbot.io/', api_key: str='python-default'):
        self._api_key = api_key
        self._base_uri = base_uri
        self._endpoint = urljoin(base_uri, '/v2/check')

    def check(self, text: str, lang: str='en-US'):
        """
        Check a given piece of text for grammatical errors.

        :param text:
            Text to be checked using the API.
        :param lang:
            Language code for the text language.
        """
        params = {
            'language': lang,
            'text': text,
            'api_key': self._api_key
        }
        res = requests.get(self._endpoint, params=params)
        json = res.json()
        return GrammarBotApiResponse(json)

    def __repr__(self):
        return 'GrammarBotClient(base_uri={}, api_key={})'.format(
            self._base_uri, self._api_key)


class GrammarBotMatch:
    """
    Represents a GrammarBot match detected by the API.
    """

    def __init__(self, match_json: dict):
        self._match_json = match_json

    @property
    def message(self) -> str:
        """
        Returns the message for the given match.
        """
        return self._match_json["message"]

    @property
    def category(self) -> str:
        """
        Gives the rule category.
        """
        return self._match_json["rule"]["category"]["id"]

    @property
    def replacement_offset(self) -> int:
        """
        Gives the offset at which the replacement should be made.
        """
        return self._match_json["offset"]

    @property
    def replacement_length(self) -> int:
        """
        Gives the length of the string that has to be replaced.
        """
        return self._match_json["length"]

    @property
    def replacements(self) -> List[str]:
        """
        Gives a list of possible replacements.
        """
        return [mjson["value"] for mjson in self._match_json["replacements"]]

    @property
    def corrections(self) -> List[str]:
        """
        Gives a list of possibly correct variation of the input text.
        """
        sentence = self._match_json["sentence"]
        left = sentence[:self.replacement_offset]
        right = sentence[self.replacement_offset + self.replacement_length:]
        return [
            '{left}{replacement}{right}'.format(
                left=left, replacement=replacement, right=right)
                for replacement in self.replacements
        ]

    @property
    def rule(self) -> str:
        """
        Gives the rule ID which applies for this match.
        """
        return self._match_json["rule"]["id"]

    @property
    def type(self) -> str:
        """
        Gives the type of match.
        """
        return self._match_json["type"]["typeName"]

    def __repr__(self) -> str:
        return (
            'GrammarBotMatch(offset={offset}, length={length}, rule={rule}, '
            'category={category})'
        ).format(
            offset=self.replacement_offset,
            length=self.replacement_length,
            rule={self.rule},
            category={self.category}
        )


class GrammarBotApiResponse:
    """
    Represents the JSON API returned by the server.
    """

    def __init__(self, json: dict):
        self._json = json

    @property
    def raw_json(self) -> dict:
        """
        Returns the raw JSON response that was returned by the server.
        """
        return self._json

    @property
    def detected_language(self) -> str:
        """
        Gives the language code for the detected langauge.
        """
        return self._json["language"]["detectedLanguage"]["code"]

    @property
    def result_is_incomplete(self) -> bool:
        """
        States whether these results are complete or incomplete.
        """
        return self._json["warnings"]["incompleteResults"]

    @property
    def matches(self) -> List[GrammarBotMatch]:
        """
        Different matches detected by the GrammarBot API.
        """
        return [GrammarBotMatch(mjson) for mjson in self._json["matches"]]

    def __repr__(self):
        return 'GrammarBotApiResponse(matches={})'.format(self.matches)
