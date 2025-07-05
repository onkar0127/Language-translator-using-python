# Language-translator-using-python
This repository contains a simple Language Translator application built using the googletrans and gtts (Google Text-to-Speech) libraries in Python. The application allows users to translate text from one language to another and convert the translated text into speech.
# Language Translator

A simple language translator application built using the Streamlit framework and the Google Translate API.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/language-translator.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the application:
```
streamlit run translator.py
```

2. The application will open in your default web browser.

3. Enter the text you want to translate in the "Input" section.

4. Select the target language from the dropdown menu.

5. Click the "Translate" button to see the translated text in the "Translation" section.

6. If the translation is successful, an audio player will be displayed below the translated text, allowing you to listen to the translation.

7. You can download the audio translation by clicking the "Download Audio" button.

## API

The application uses the following APIs:

- [Google Translate API](https://cloud.google.com/translate/docs) for text translation.
- [Google Text-to-Speech (gTTS) API](https://pypi.org/project/gTTS/) for audio conversion.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests for this project, use the following command:

```
pytest tests/
```

This will run all the tests defined in the `tests/` directory.
