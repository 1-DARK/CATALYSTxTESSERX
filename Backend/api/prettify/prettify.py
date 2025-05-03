import json

class Prettify:
    def prettify_llm_json_string(self, json_string):
        """
        Cleans up a JSON string potentially wrapped in markdown and outer quotes,
        then parses and prettifies the JSON content.

        Args:
            json_string: The raw string received from the LLM API.

        Returns:
            A prettified JSON string, or an error message if processing fails.
        """
        # 1. Remove the outermost double quotes if they exist
        # The string starts and ends with a double quote in your example
        if json_string.startswith('"') and json_string.endswith('"'):
            # Remove the first and last characters (the double quotes)
            cleaned_string = json_string[1:-1]
        else:
            # If it doesn't have outer quotes, assume it's already the inner part
            cleaned_string = json_string

        # 2. Remove the markdown code block wrappers (```json\n and \n```)
        start_marker = '```html\n'
        end_marker = '\n```'

        if cleaned_string.startswith(start_marker) and cleaned_string.endswith(end_marker):
            # Slice the string to remove the markers
            json_content = cleaned_string[len(start_marker):-len(end_marker)]
        else:
            # If the wrappers are not found, assume the cleaned string is the JSON content
            # This handles cases where the LLM might not include the wrappers sometimes
            json_content = cleaned_string

        # 3. Parse the JSON content string into a Python dictionary/object
        return json_content
# print(prettified_output)