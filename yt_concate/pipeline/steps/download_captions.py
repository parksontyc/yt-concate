import os

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
from yt_concate.config import CAPTIONS_DIR



class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print('downloading caption for', url)
            if utils.get_caption_filepath(url):
                print('found existing caption file')
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, ArithmeticError):
                print('Error when downloading caption for', url)
                continue

            print(en_caption_convert_to_srt)

            text_file = open(utils.get_caption_filepath(url) + ".txt", "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
