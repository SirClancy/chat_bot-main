import re

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

if __name__=="__main__":
    print(extract_session_id("projects/kula-chatbot-mcwc/agent/sessions/43445-9396-e8e4-d819-736c51e93e7b/contexts/2fd1b657-b252-4780-b0fc-df7ae1ae138c_id_dialog_context"))