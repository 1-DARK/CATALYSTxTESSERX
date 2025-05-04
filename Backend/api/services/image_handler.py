from google.genai import types
from google import genai
import os
from pathlib import Path

class PossibleDisease:
    current_dir = Path(__file__).resolve()
    parent_dir = current_dir.parents[2]

    client = genai.Client(api_key="")
    def getDisease(self, imgName):
        with open(f'{self.parent_dir}/media/uploads/{imgName}', 'rb') as f:
            self.img_bytes = f.read()

        response = self.client.models.generate_content(
            model='gemini-2.5-flash-preview-04-17',
            contents=[
                types.Part.from_bytes(
                data=self.img_bytes,
                mime_type='image/jpeg',
                ),
                '''Analyze the provided chest X-ray image. Based SOLELY on the visual patterns you detect, create a html table stating potential corresponding diseases or significant abnormalities.

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
                IF NO IMAGE IS PROVIDED THEN ANALYIZE THE USER BASED ON THE TEXT PROVIDED AND GIVE OUT THE TABLE OF POSSIBLE DISEASE ON THE SYMPTOMPS PROVIDED
                NEVER use markdown formatting, code blocks (` ``` `), or escape sequences like `\n`.
                Provide the requested information directly without conversational filler..
                If no disease is found just respond with "No abnormalities detected."
                Begin the output now:'''
                ]
        )

        return response.text

