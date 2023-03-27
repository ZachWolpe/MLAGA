
"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

s = "pourquoi le président américain est-il soupçonné d&#39;être un fan de Call of Duty n&#39;est pas ce que vous pensez en 2018, l&#39;ancien président américain Donald Trump a annoncé la vente des premiers avions de chasse F 52 et F-35 à la Norvège, attendez une seconde si 52 maintenant le F50 2 n&#39;existe pas en fait dans le jeu Call of Duty Advanced Warfare, mais il s&#39;avère que le président Trump s&#39;est juste mal exprimé, je voulais dire 52 F-35 Jets et il n&#39;est pas le seul président américain à dire les mauvais mots"

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=s)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="fr-FR", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
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

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')