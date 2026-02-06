def translate(text, target_language):
    """
    Translates the given text to the target language.
    Args:
        text (str): The text to translate.
        target_language (str): The language to translate to (e.g., 'fr', 'es').
    Returns:
        str: The translated text.
    """
    try:
        # Assuming a function get_translation exists that interacts with a translation API
        translated_text = get_translation(text, target_language)
        return translated_text
    except Exception as e:
        print(f'Error occurred during translation: {e}')
        return None

# Example usage
if __name__ == '__main__':
    text_to_translate = 'Hello, world!'
    translation = translate(text_to_translate, 'fr')
    if translation:
        print(f'Translated text: {translation}')