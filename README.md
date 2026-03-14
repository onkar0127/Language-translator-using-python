# Language-translator-using-python
A high-performance, modern language translation web application built with Streamlit. This app supports over 100+ global languages and converts translated text into speech instantly.

## Installation

1. Clone the repository:
```
https://github.com/onkar0127/Language-translator-using-python.git
```

2. Install the required dependencies:
```
pip install streamlit deep-translator gTTS
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

## API & Library Reference
The application uses the following open-source libraries to interface with Google's translation and speech engines without requiring a paid API key:

[Deep-Translator](https://pypi.org/project/deep-translator/): Used for the core translation logic. It replaces the older googletrans library to provide better stability and compatibility with Python 3.13+. It handles over 100+ languages dynamically.

[gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/): Converts the translated string into a natural-sounding voice. The audio is processed in-memory using BytesIO for faster performance and privacy.

[Streamlit](https://streamlit.io/): Powers the web interface and handles the Session State, ensuring that text and audio stay synchronized when you switch languages.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

