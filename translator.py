import streamlit as st
from googletrans import Translator,  LANGUAGES
import time
from gtts import gTTS
from io import BytesIO


def text_translation(given_text, target_language):
    try:
        translator_obj = Translator()
        translated = translator_obj.translate(given_text, dest=target_language)
        return translated.text
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None


def audio_conversion(given_text, given_lang_code):
    try:
        tts = gTTS(text=given_text, lang=given_lang_code)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        st.error(f"there is error : {str(e)}")
        return None


def main():
    st.title("Language Translator")
    st.write("Simple translator using googletrans library with text-to-speech capability")

    # Create two columns for input and output
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input")
        input_text = st.text_area("Enter text to translate", height=200)

        # Create a sorted list of languages
        language_list = sorted(LANGUAGES.items(), key=lambda x: x[1])

        # Language selection
        target_language = st.selectbox(
            "Select target language",
            [code for code, name in language_list],
            format_func=lambda x: LANGUAGES[x].capitalize()
        )

        # Translate button
        if st.button("Translate"):
            if input_text:
                with st.spinner("Translating..."):
                    try:
                        translated_text = text_translation(input_text, target_language)
                        st.session_state.translated_text = translated_text

                        # Generate audio for translated text
                        audio_bytes = audio_conversion(translated_text, target_language)
                        if audio_bytes:
                            st.session_state.audio = audio_bytes
                    except Exception as e:
                        st.error("Translation failed. Please try again in a few moments.")
                        time.sleep(1)  # Add small delay before retry
            else:
                st.warning("Please enter text to translate")

    with col2:

        st.subheader("Translation")
        if 'translated_text' in st.session_state:
            translated_area = st.text_area(
                "Translated text",
                st.session_state.translated_text,
                height=200
            )

            # Add audio player if audio is available
            if 'audio' in st.session_state:
                st.audio(st.session_state.audio, format='audio/mp3')

                # Download button for audio
                st.download_button(
                    label="Download Audio",
                    data=st.session_state.audio,
                    file_name="translation.mp3",
                    mime="audio/mp3"
                )


if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Language Translator",
        layout="wide"
    )
    main()
