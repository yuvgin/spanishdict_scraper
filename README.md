# SpanishDict Vocabulary Scraper

This Python script scrapes vocabulary lists from SpanishDict and retrieves usage examples for each word. It then saves the results to a CSV file.

## Features

- Scrapes vocabulary words and translations from a public SpanishDict vocabulary list
- Retrieves usage examples for each word from SpanishDict
- Saves the results (word, translation, Spanish example, English example) to a CSV file

## Requirements

- Python 3.6+
- Required Python packages:
  - requests
  - beautifulsoup4
  - pandas

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```
pip install requests beautifulsoup4 pandas
```

## Usage

1. On SpanishDict, make sure your vocabulary list is public.
2. Click the "Share" button on your vocabulary list and copy the share link.
3. Run the script with the copied URL as an argument:

```
python spanishdict_scraper.py -u "https://www.spanishdict.com/lists/YOUR_LIST_ID/your-list-name"
```

Replace `"https://www.spanishdict.com/lists/YOUR_LIST_ID/your-list-name"` with the actual URL you copied.

## Output

The script will create a file named `vocabulary_list.csv` in the same directory. This CSV file will contain the following columns:

- Word: The Spanish word
- Translation: The English translation
- spanish_example: A usage example in Spanish
- english_example: The English translation of the usage example

## Notes

- The script may take some time to run, especially for larger vocabulary lists, as it fetches examples for each word individually.
- Be respectful of SpanishDict's servers and avoid running the script too frequently or on very large lists.
- This script is for educational purposes only. Make sure you comply with SpanishDict's terms of service when using it.

## Troubleshooting

- If you encounter any errors related to the URL, make sure your vocabulary list is public and that you've copied the correct share link.
- If you're having issues with retrieving examples, it might be due to changes in SpanishDict's website structure. Check the HTML classes used in the `get_usage_example` function and update them if necessary.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
