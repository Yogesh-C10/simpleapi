from flask import Flask, send_file, abort, Response
import os

app = Flask(__name__)

@app.route('/download')
def download_file():
    # Get the path to the current directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the relative file name
    file_name = 'EG915UECABR02A03M08_01.200.01.200V01-EG915UECABR03A04M08_01.200.01.200V01.pack'

    # Combine the current directory with the file name
    file_path = os.path.join(current_dir, file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        abort(404, description="File not found")

    # Send the file to the user with proper headers for download
    response = send_file(
        file_path,
        as_attachment=True,
        download_name='file.pack',  # This sets the downloaded file name
        mimetype='application/octet-stream',  # Generic binary file type
    )

    # Disable caching (set Cache-Control header manually)
    response.cache_control.no_cache = True  # Equivalent to cache_timeout=0

    return response

if __name__ == '__main__':
    app.run(debug=True)