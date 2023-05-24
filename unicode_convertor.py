import pandas as pd
import base64
import io


def get_clear(file_path, save=False):
    """ This function get address of a csv file that contain html column encoded base64 and return decoded content as
    utf-8, even you can pass second parameter equal True to save decoded content as html file in same path"""
    csv_data = pd.read_csv(file_path, on_bad_lines='skip')
    binary_file_data = csv_data['html']

    base64_message = binary_file_data[0]
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    html = message_bytes.decode('utf-8')
    if save:
        with io.open(file_path+".html", 'w', encoding='utf-8') as f:
            f.write(html)
    return html

