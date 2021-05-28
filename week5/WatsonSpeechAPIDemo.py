
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/a49b4817-5e3f-4dbf-bdbf-0aa8634e6e08"
iam_apikey_s2t = "TaHzVGCnxUKp01gCPreV4IKewPPGYUPHowAJg7qWssa2"
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

audioFile = "/Users/san6685/PycharmProjects/python-courea-sessions/PolynomialRegressionandPipelines.mp3"

with open(audioFile, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

response.result
print(f"Resuslt of response: {response.result}")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
print(f"recognized_text: {recognized_text}")
print(f"Type of recognized_text: {type(recognized_text)}")


# Language Translator:
from ibm_watson import LanguageTranslatorV3
url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/66deb65e-bae9-4e4d-9644-1434d8f19789'
apikey_lt='RK_vYlQ_8ILWkNXjCDfat-Urnnk7SpG1yvPliUJPbXau'
version_lt='2021-05-28'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas import json_normalize
#recognized_text="in this video we will cover polynomial regression and pipelines "
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
print(f"translation: {translation}")
spanish_translation =translation['translations'][0]['translation']
print(f"spanish_translation: {spanish_translation}")

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
print(f"translation_eng: {translation_eng}")

