[![Open in Cloud Shell][shell_img]][shell_link]

[shell_img]: http://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/alexlaurence/DoReMi&page=editor&open_in_editor=DoReMi-app

![Alt text](https://i.imgur.com/OS76n8F.png)

## Inspiration
According to the South Korean Ministry of Health and Welfare, there were 252,779 people with hearing impairment in South Korea as of 2014. Recent estimated figures for the number of deaf people in South Korea range from 180,000 to 300,000.

South Korea has embraced technology to help the disabled, most notably last year when South Korean startup 'Coactus' developed "Goyohan Taxi" or "Silent Taxi" app to enable the deaf to work as taxi drivers. While Coactus is hoping that more deaf drivers on the road will help break stigma across South Korea about hearing-impaired drivers, I hope I can play a part in helping the blind to land jobs in South Korea.

## What it does
DoReMi is a tool for blind users to search job listings from by synthesising job listing RSS feeds from Scout.co.kr into speech with the help of Google's Text-to-Speech API powered by a WaveNet model.

**Why Google Text-to-Speech?**

The Text-to-Speech API creates raw audio data of natural, human speech. That is, it creates audio that sounds like a person talking. When you send a synthesis request to the Text-to-Speech API, you must specify a voice that 'speaks' the words.

**Why WaveNet?**

A WaveNet generates speech that sounds more natural than other text-to-speech systems. It synthesizes speech with more human-like emphasis and inflection on syllables, phonemes, and words. On average, a WaveNet produces speech audio that people prefer over other text-to-speech technologies.

Unlike most other text-to-speech systems, a WaveNet model creates raw audio waveforms from scratch. The model uses a neural network that has been trained using a large volume of speech samples. During training, the network extracts the underlying structure of the speech, such as which tones follow each other and what a realistic speech waveform looks like. When given a text input, the trained WaveNet model can generate the corresponding speech waveforms from scratch, one sample at a time, with up to 24,000 samples per second and seamless transitions between the individual sounds.

## How I built it
* Google Cloud API
* Python 3.7 (and a whole bunch of libraries)
* Google Colaboratory. 

## Challenges I ran into
* Working in a language that I can't speak (Korean)

## Accomplishments that I'm proud of
* Helping build a tool that will one day help blind people find work.

## What I learned
* Data wrangling
* Google Cloud API

## What's next for DoReMi?
* Web App
* Automatic playback
* Speech to text, to parse user's intent (i.e. 'apply job', 'search busan'), completely remove the reliance on typing/reading
