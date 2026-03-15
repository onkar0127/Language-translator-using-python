import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO


# Fetch all supported languages from deep-translator
@st.cache_data
def get_all_languages():
    # This returns a dict like {'afrikaans': 'af', 'albanian': 'sq', ...}
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    # Capitalize names for a better UI
    return {name.capitalize(): code for name, code in langs.items()}


def text_translation(given_text, target_code):
    try:
        translated = GoogleTranslator(source='auto', target=target_code).translate(given_text)
        return translated
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None


def audio_conversion(given_text, given_lang_code):
    try:
        # Note: gTTS supports fewer languages than Google Translate.
        # If gTTS doesn't support the code, it will raise an error.
        tts = gTTS(text=given_text, lang=given_lang_code)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        # We handle cases where translation is supported but speech isn't
        return "NotSupported"


def main():
    st.set_page_config(page_title="Global Translator Pro", layout="wide")
    st.title("🌎 Universal Language Translator")

    # Initialize session state
    if 'translated_text' not in st.session_state:
        st.session_state.translated_text = ""
    if 'audio' not in st.session_state:
        st.session_state.audio = None

    # Load all languages
    languages_dict = get_all_languages()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input")
        input_text = st.text_area("Enter text", height=200, placeholder="Type here...", key="input_area")

        # Searchable dropdown with 100+ languages
        selection = st.selectbox(
            "Select target language",
            options=list(languages_dict.keys()),
            index=list(languages_dict.keys()).index("English") if "English" in languages_dict else 0
        )
        target_code = languages_dict[selection]

        if st.button("Translate & Generate Audio", type="primary"):
            if input_text.strip():
                with st.spinner(f"Translating to {selection}..."):
                    result = text_translation(input_text, target_code)

                    if result:
                        st.session_state.translated_text = result
                        st.session_state.output_box = result

                        # Attempt Audio
                        audio_data = audio_conversion(result, target_code)
                        if audio_data == "NotSupported":
                            st.session_state.audio = None
                            st.info(f"Audio is not yet supported for {selection}, but here is the text!")
                        else:
                            st.session_state.audio = audio_data

                        st.rerun()
            else:
                st.warning("Please enter text first.")

    with col2:
        st.subheader("Output")

        if st.session_state.translated_text:
            st.text_area(
                "Translated Text",
                height=200,
                key="output_box"
            )

            if st.session_state.audio:
                st.audio(st.session_state.audio, format='audio/mp3')
                st.download_button(
                    label="Download Audio",
                    data=st.session_state.audio,
                    file_name="translation.mp3",
                    mime="audio/mp3"
                )

            if st.button("Clear All"):
                st.session_state.translated_text = ""
                st.session_state.audio = None
                if "output_box" in st.session_state:
                    st.session_state.output_box = ""
                st.rerun()
        else:
            st.info("Translation will appear here.")


if __name__ == "__main__":
    main()
