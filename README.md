# PIIEncoderDecoder

This is a Python project that allows you to identify personally identifiable information (PII) entities in a given text, encode them, use the encoded text as 
- A prompt to chatGPT
- A wrapper for logging functions, third-party, APIs

Apply the decoding function to get output with PII

The project utilizes Named Entity Recognition (NER) provided by the `spaCy` library to identify PII entities such as names, organizations, locations, etc. It then applies a simple encoding scheme to replace the identified entities with unique values.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/PIIEncoderDecoder.git

cd PIIEncoderDecoder
```


2. Install the required dependencies:

```
pip install spacy

python -m spacy download en_core_web_sm
```


## Usage

1. Open the `pii_encoder_decoder.py` file in your preferred code editor.

2. Run the script:

3. Enter the text you want to process (currently hardcoded).

4. The script will identify PII entities, and encode the text by replacing the entities with unique values

5. The encoded text can be passed to the method `execute` and used as a prompt to chatGPT, as a wrapper to logging functions, third party API's

6. Decode the output text from the `execute` method using the mapping.

7. The encoded and decoded strings will be displayed as output.




Feel free to customize the README file based on your project's specific requirements and add any additional sections or information that you think would be helpful.


