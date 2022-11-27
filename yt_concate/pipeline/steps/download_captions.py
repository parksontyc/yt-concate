import os

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
from yt_concate.config import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())

            print(en_caption_convert_to_srt)

            text_file = open(utils.get_caption_path(url) + ".txt", "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()






