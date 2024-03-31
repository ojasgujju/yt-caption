from http.server import BaseHTTPRequestHandler, HTTPServer
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse
import json

# Dummy function TRANS.get_transcript
def get_transcript(id, preserve_formatting=True):
    # Dummy data

    result = YouTubeTranscriptApi.get_transcript(id, preserve_formatting=True)

    return result

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_url = urllib.parse.urlparse(self.path)
        
        # Get the query parameters
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        # Check if 'id' parameter exists
        if 'id' in query_params:
            # Extract the ID value
            id_value = query_params['id'][0]
            
            # Call TRANS.get_transcript function to get the transcript
            result = get_transcript(id_value, preserve_formatting=True)
            
            # Convert the transcript to HTML format
            html_response = "<html><body><h1>Transcript for ID: {}</h1>".format(id_value)
            for item in result:
                html_response += "<p>{} (Start: {}, Duration: {})</p>".format(item['text'], item['start'], item['duration'])
            html_response += "</body></html>"
            
            # Send the HTML response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(html_response, "utf-8"))
        else:
            # If 'id' parameter is not found, send a 400 error response
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("Error: 'id' parameter not found in URL", "utf-8"))

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Server stopped.')

if __name__ == "__main__":
    run()
