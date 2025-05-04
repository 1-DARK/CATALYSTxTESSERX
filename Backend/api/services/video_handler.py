from google import genai
from google.genai import types
import time
from pathlib import Path

class VideoHandler():
    client = genai.Client(api_key="")
    current_dir = Path(__file__).resolve()
    parent_dir = current_dir.parents[2]

    def Response(self, videoName):
        #         video_file_name = f"/home/linuxer77/Programs/Hackathon-Project/Disease-bullshit/media/videos/{videoName}"
        # video_bytes = open(video_file_name, 'rb').read()

        myfile = self.client.files.upload(file=f"{self.parent_dir}/media/videos/{videoName}")

        time.sleep(15)
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=[myfile, '''
                Analyze the provided video. Based SOLELY on the visual patterns you detect, create a html table stating potential corresponding diseases or significant abnormalities. sIf no disease is found just respond with "No abnormalities detected."


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
                If no disease is found just respond with "No abnormalities detected."
                Begin the output now:
                                                ''']
        )

        return response.text