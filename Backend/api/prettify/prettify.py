import json

class Prettify:
    def prettify_llm_json_string(self, json_string):

        if json_string.startswith('"') and json_string.endswith('"'):
            cleaned_string = json_string[1:-1]
        else:
            cleaned_string = json_string

        start_marker = '```html\n'
        end_marker = '\n```'

        if cleaned_string.startswith(start_marker) and cleaned_string.endswith(end_marker):
            json_content = cleaned_string[len(start_marker):-len(end_marker)]
        else:
            json_content = cleaned_string

        return json_content
