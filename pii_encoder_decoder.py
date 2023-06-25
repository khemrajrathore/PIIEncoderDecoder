import spacy

nlp = spacy.load("en_core_web_sm")

def identify_pii_and_labels(text):
    doc = nlp(text)
    pii_entities = []
    pii_labels = []
    for ent in doc.ents:
        pii_entities.append(ent.text)
        pii_labels.append(ent.label_)
    return pii_entities, pii_labels


def apply_mapping(input_text, mapping):
    result_text = input_text
    for mapping_token in mapping:
        result_text = result_text.replace(mapping_token, mapping[mapping_token])
    return result_text

def create_mapping(pii_list, pii_labels):
    counter = 1
    mapping = dict()
    reverse_mapping = dict()
    for pii, pii_label in zip(pii_list, pii_labels):
        mappingTag = f'{pii_label}_{counter}'
        if pii not in mapping:
            mapping[pii] = mappingTag
            reverse_mapping[mappingTag] = pii
            counter += 1
    return mapping, reverse_mapping

def execute(encoded_string):
    # You can perform operations like sending this prompt to OPEN API, or as a wrapper to logger, third party API calls etc
    output_string = '''Subject: Congratulations on Your Promotion to Senior Software Engineer!

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
            [GPE_3]'''
    return output_string

def main():
    input_string = "Create me a congratulatory email from John working at Google Inc, California to David for being promoted to the role Senior Software Engineer at Accenture Private Limited, New York"
    pii_entities, pii_labels = identify_pii_and_labels(input_string)
    mapping, reverse_mapping = create_mapping(pii_entities, pii_labels)

    # Encode the identified PII entities
    encoded_string = apply_mapping(input_string, mapping)
    print("Encoded string:", encoded_string)

    # Use the encoded string to solve your use case, and on the returned output apply decoding 
    output_string = execute(encoded_string)

    # Decode the encoded string
    decoded_string = apply_mapping(output_string, reverse_mapping)
    print("Decoded string:", decoded_string)

if __name__ == "__main__":
    main()
