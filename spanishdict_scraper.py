import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse

def fetch_vocabulary_list(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all vocabulary items
    vocab_items = []
    
    for item in soup.find_all('div', class_='pKddbGA6'):
        word_element = item.find('div', class_='xehIoI3Z')
        translation_element = item.find('div', class_='X4KF_Xog')
        
        if word_element and translation_element:
            word = word_element.get_text(strip=True)
            translation = translation_element.get_text(strip=True)
            vocab_items.append({'Word': word, 'Translation': translation})
    
    return vocab_items

def get_usage_example(spanish_word, english_translation):
    # Construct the URL for the SpanishDict page
    url = f'https://www.spanishdict.com/translate/{spanish_word}'

    # Send a request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all definitions
    definitions = soup.find_all('div', class_='FBrUXflP')

    for definition in definitions:
        # Find the English translation text
        definition_text = definition.find('span', class_='a9peX5qq')
        if definition_text:
            definition_text = definition_text.get_text(strip=True)

            # Find the subdefinition that matches the English translation
            subdefinitions = definition.find_all('a', class_='HOypmmqy')
            for subdefinition in subdefinitions:
                subdefinition_text = subdefinition.get_text(strip=True)

                if subdefinition_text and english_translation in subdefinition_text:
                    # Find the usage examples related to this subdefinition
                    examples = definition.find_all('div', class_='Ho2hYDXJ')
                    for example in examples:
                        # Extract both Spanish and English parts of the example
                        spanish_example = example.find('span', class_='Dz_Re0aB')
                        english_example = example.find('span', class_='okF5TUFl')

                        if spanish_example and english_example:
                            return {
                                'spanish_example': spanish_example.get_text(strip=True),
                                'english_example': english_example.get_text(strip=True)
                            }

    return {'spanish_example': 'Example not found', 'english_example': 'Example not found'}

def save_to_csv(vocab_items, filename):
    df = pd.DataFrame(vocab_items)
    df.to_csv(filename, index=False, encoding='utf-8')

def main(spanishdict_list):
    html = fetch_vocabulary_list(spanishdict_list)
    vocab_items = parse_html(html)

    # Fetch examples for each vocabulary item
    for item in vocab_items:
        examples = get_usage_example(item['Word'], item['Translation'])
        item.update(examples)

    save_to_csv(vocab_items, 'vocabulary_list.csv')
    print('Vocabulary list saved to vocabulary_list.csv')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process a URL.')
    parser.add_argument('-u', '--url', type=str, required=True, help='Valid URL to spanishdict vocabulary list')

    # Parse the arguments
    args = parser.parse_args()
    
    main(args.url)
    
