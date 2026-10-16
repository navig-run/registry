"""Language names to the ISO codes speech models accept, with or without navig.

    from navig_sdk.lang import language_code
    language_code("Russian")  # "ru"
    language_code("auto")     # None -> let the model detect it

With navig installed this is ``navig.core.language.language_code`` itself. Without navig it is
the same table: a name ("Russian"), a code ("ru") or an auto value ("", "auto", "detect")
maps onto a code, and anything unrecognised becomes ``None`` (auto-detect) rather than a value
the provider would refuse. A parity test in core fails the build if the two drift.
"""

from __future__ import annotations

__all__ = ["language_code"]

_AUTO = {"", "auto", "detect", "source", "any"}

_NAME_TO_CODE: dict[str, str] = {
    "afrikaans": "af", "albanian": "sq", "amharic": "am", "arabic": "ar", "armenian": "hy",
    "assamese": "as", "azerbaijani": "az", "bashkir": "ba", "basque": "eu",
    "belarusian": "be", "bengali": "bn", "bosnian": "bs", "breton": "br", "bulgarian": "bg",
    "burmese": "my", "cantonese": "yue", "castilian": "es", "catalan": "ca",
    "chinese": "zh", "croatian": "hr", "czech": "cs", "danish": "da", "dutch": "nl",
    "english": "en", "estonian": "et", "faroese": "fo", "finnish": "fi", "flemish": "nl",
    "french": "fr", "galician": "gl", "georgian": "ka", "german": "de", "greek": "el",
    "gujarati": "gu", "haitian": "ht", "haitian creole": "ht", "hausa": "ha",
    "hawaiian": "haw", "hebrew": "he", "hindi": "hi", "hungarian": "hu", "icelandic": "is",
    "indonesian": "id", "italian": "it", "japanese": "ja", "javanese": "jw",
    "kannada": "kn", "kazakh": "kk", "khmer": "km", "korean": "ko", "lao": "lo",
    "latin": "la", "latvian": "lv", "letzeburgesch": "lb", "lingala": "ln",
    "lithuanian": "lt", "luxembourgish": "lb", "macedonian": "mk", "malagasy": "mg",
    "malay": "ms", "malayalam": "ml", "maltese": "mt", "mandarin": "zh", "maori": "mi",
    "marathi": "mr", "moldavian": "ro", "moldovan": "ro", "mongolian": "mn",
    "myanmar": "my", "nepali": "ne", "norwegian": "no", "nynorsk": "nn", "occitan": "oc",
    "panjabi": "pa", "pashto": "ps", "persian": "fa", "polish": "pl", "portuguese": "pt",
    "punjabi": "pa", "pushto": "ps", "romanian": "ro", "russian": "ru", "sanskrit": "sa",
    "serbian": "sr", "shona": "sn", "sindhi": "sd", "sinhala": "si", "sinhalese": "si",
    "slovak": "sk", "slovenian": "sl", "somali": "so", "spanish": "es", "sundanese": "su",
    "swahili": "sw", "swedish": "sv", "tagalog": "tl", "tajik": "tg", "tamil": "ta",
    "tatar": "tt", "telugu": "te", "thai": "th", "tibetan": "bo", "turkish": "tr",
    "turkmen": "tk", "ukrainian": "uk", "urdu": "ur", "uzbek": "uz", "valencian": "ca",
    "vietnamese": "vi", "welsh": "cy", "yiddish": "yi", "yoruba": "yo",
}  # fmt: skip

_CODES: frozenset[str] = frozenset(_NAME_TO_CODE.values())


def language_code(value: object) -> str | None:
    """The ISO code a speech model will accept, or ``None`` for auto-detect."""
    try:
        from navig.core.language import language_code as _impl  # noqa: PLC0415
    except ImportError:
        return _language_code_fallback(value)
    return _impl(value)


def _language_code_fallback(value: object) -> str | None:
    key = str(value or "").strip().lower()
    if key in _AUTO:
        return None
    if key in _CODES:
        return key
    return _NAME_TO_CODE.get(key)
