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


## Example

Input

```
Create me a congratulatory email for David for being promoted to the role Senior Software Engineer at Accenture Private Limited, New York
```

Encoded String
```
Create me a congratulatory email from PERSON_1 working at ORG_2, GPE_3 to PERSON_4 for being promoted to the role Senior Software Engineer at ORG_5, GPE_6
```

Output from ChatGPT
```
Subject: Congratulations on Your Promotion to Senior Software Engineer!

Dear [PERSON_4],

I am absolutely thrilled to extend my warmest congratulations to you on your well-deserved promotion to the role of Senior Software Engineer at [ORG_5], located in [GPE_6]. This is a tremendous achievement and a testament to your hard work, dedication, and exceptional skills.

Throughout your tenure at [ORG_2], your contributions as a Software Engineer have been remarkable. Your ability to tackle complex challenges, your commitment to delivering high-quality work, and your continuous pursuit of excellence have not gone unnoticed. Your promotion to Senior Software Engineer is a testament to your outstanding capabilities and the trust that [ORG_5] has placed in you.

As a Senior Software Engineer, you will have the opportunity to take on greater responsibilities, lead important projects, and make an even more significant impact within the organization. Your technical expertise, leadership abilities, and strong problem-solving skills will undoubtedly shine in this new role.

I have no doubt that you will continue to excel and thrive as a Senior Software Engineer at [ORG_5]. Your professionalism, dedication, and positive attitude make you an asset to any team you work with.

On behalf of the entire team at [ORG_2], I congratulate you once again on this remarkable achievement. Your promotion is well-deserved, and we are excited to see the incredible accomplishments you will achieve in your new role.

Please feel free to reach out if you have any questions or if there is anything I can do to support you during this transition. We are here to celebrate your success and help you in any way possible.

Congratulations, [PERSON_4]! Wishing you continued success and fulfillment in your career journey as a Senior Software Engineer at [ORG_5].

Best regards,

[PERSON_1]
[Your Position]
[ORG_2]
[GPE_3]
```


Decoded Output
```
Subject: Congratulations on Your Promotion to Senior Software Engineer!

Dear [David],

I am absolutely thrilled to extend my warmest congratulations to you on your well-deserved promotion to the role of Senior Software Engineer at [Accenture Private Limited], located in [New York]. This is a tremendous achievement and a testament to your hard work, dedication, and exceptional skills.

Throughout your tenure at [Google Inc], your contributions as a Software Engineer have been remarkable. Your ability to tackle complex challenges, your commitment to delivering high-quality work, and your continuous pursuit of excellence have not gone unnoticed. Your promotion to Senior Software Engineer is a testament to your outstanding capabilities and the trust that [Accenture Private Limited] has placed in you.

As a Senior Software Engineer, you will have the opportunity to take on greater responsibilities, lead important projects, and make an even more significant impact within the organization. Your technical expertise, leadership abilities, and strong problem-solving skills will undoubtedly shine in this new role.

I have no doubt that you will continue to excel and thrive as a Senior Software Engineer at [Accenture Private Limited]. Your professionalism, dedication, and positive attitude make you an asset to any team you work with.

On behalf of the entire team at [Google Inc], I congratulate you once again on this remarkable achievement. Your promotion is well-deserved, and we are excited to see the incredible accomplishments you will achieve in your new role.

Please feel free to reach out if you have any questions or if there is anything I can do to support you during this transition. We are here to celebrate your success and help you in any way possible.

Congratulations, [David]! Wishing you continued success and fulfillment in your career journey as a Senior Software Engineer at [Accenture Private Limited].

Best regards,

[John]
[Your Position]
[Google Inc]
[California]
```




Feel free to customize the README file based on your project's specific requirements and add any additional sections or information that you think would be helpful.


