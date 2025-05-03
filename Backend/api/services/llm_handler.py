from google import genai
import json

class QueryResponse:
    def __init__(self):        
        self.client = genai.Client(api_key="")
    
    def generateResponse(self, diet):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f'''
            Analyze the symptoms mentioned below, generate a html table suggesting potential conditions based *only* on them.
            Symptons: [{diet}].

                The table should have the following columns in this exact order: Disease, possibility.

                Structure the response as a complete HTML `<table>` element, including `<thead>` for headers and `<tbody>` for the rows.

                Output ONLY the HTML `<table>` element and its full content. Do not include any surrounding text, markdown code blocks (like ```html), or any other characters before or after the HTML table code.

                Example structure of the HTML you should generate (use the actual meal plan data for the content):

                ```html
                <table>
                <thead>
                    <tr>
                    <th>Disease</th>
                    <th>Possibility</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>[Disease Name]</td>
                    <td>[Possibility in percentage]</td>
                    </tr>
                    <tr>
                    <td>[Disease Name]</td>
                    <td>[Possibility in percentage]</td>
                    </tr>
                    <!-- ... and so on for other diseases -->
                </tbody>
                </table>
                '''
                '''Output Requirements:
                IMPORTANT: 
                NEVER use markdown formatting, code blocks (` ``` `), or escape sequences like `\n`.
                Provide the requested information directly without conversational filler..
                
                Begin the output now:''',
        )
        return response.text


# if __name__ == '__name__':