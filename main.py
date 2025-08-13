#!/usr/bin/env python3

import os
from google.cloud import texttospeech

phonetic_descriptor = texttospeech.CustomPronunciationParams(
    phrase="私",
    phonetic_encoding = texttospeech.CustomPronunciationParams.PhoneticEncoding.PHONETIC_ENCODING_JAPANESE_YOMIGANA,
    pronunciation = "わ^た!し"
)

TEXT = "私"
FOLDER = "output"

# Client initialization
client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text=TEXT)
synthesis_input.custom_pronunciations=texttospeech.CustomPronunciations(pronunciations=[phonetic_descriptor])

voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", name="ja-JP-Chirp3-HD-Achernar"
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# TODO: check if the folder exist, create if it's not there
# Best practices and make sure it works cross-platform
# os.mkdir(FOLDER)

outfile = f'{TEXT}-chirp.mp3'

# The response's audio_content is binary.
with open(outfile, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print(f'Audio content written to file "{outfile}"')
