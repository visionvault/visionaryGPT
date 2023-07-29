import os
# Set up OpenAI API credentials
import openai
openai.api_key = ' '
import gradio as gr

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def choose_topic(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.9, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def generate_topic():
  prompt_sum = f"""
  Generate a table topic that tests the impromptu speaking skills of a person. Limit it to at the max 7 words. Here are some examples:
  Life As an Object
  Walking Dictionary
  Color your world
  A second chance
  The day I met Elvis
  Did you know that I once...?
  Home is where the heart is
  What doesn't kill you makes you ......
  Keep your friends close. And your enemies closer.
"""

  response_sum = choose_topic(prompt_sum)
  return response_sum

def audio_summary(transcript):
  prompt_sum = f"""
 As Cicero, the master orator, you are tasked with evaluating the effectiveness of a persuasive speech based on his renowned "five canons of rhetoric." These canons serve as a framework for analyzing and crafting persuasive speeches and arguments. Your evaluation will focus on the following aspects:
1. Invention (Quality of Arguments and Evidence):
Assess the logical and compelling nature of the arguments presented by the speaker.
Examine the evidence provided to support the speaker's points and evaluate its credibility.
2. Arrangement (Organization and Structure):
Analyze the logical flow of the speaker's ideas and the overall structure of the argument.
Evaluate whether the arrangement of points enhances the coherence and clarity of the speech.
3. Style (Word Choice, Sentence Structure, Rhetorical Devices):
Assess the appropriateness and effectiveness of the speaker's word choice and sentence structure.
Evaluate the use of rhetorical devices to enhance the persuasiveness of the speech.
4. Memory (Use of Examples, Comparisons, Narratives):
Examine the speaker's use of examples, comparisons, and narratives to illustrate their points.
Evaluate how effectively the speaker makes their arguments memorable through storytelling.
5. Delivery (Voice, Presentation):
Assess the speaker's delivery style, including voice modulation.
Evaluate how well the delivery complements and enhances the content of the argument.
Prompt:
Imagine you are Cicero, the master orator. Your task is to evaluate the persuasive speech presented below based on your renowned "five canons of rhetoric." Provide a comprehensive evaluation report for the speaker, considering each canon's key attributes.
Speech Transcript:
{transcript}
Evaluation Report Format:
Invention:
Evaluate the quality of arguments and evidence.
Provide feedback on the logical strength of the points presented.
Arrangement:
Analyze the organization and structure of the speech.
Assess how well the logical flow enhances the speech's coherence.
Style:
Evaluate the word choice, sentence structure, and use of rhetorical devices.
Comment on the effectiveness of the speaker's stylistic choices.
Memory:
Examine the use of examples, comparisons, and narratives in the speech.
Assess how memorable the speaker's arguments are due to storytelling.
Delivery:
Evaluate the speaker's voice.
Comment on how well the delivery complements and enhances the argument.
Overall Summary of Evaluation:
Provide a concise overview of the speech's strengths and areas for improvement.
Score on a Scale of 1-10:
Assign a rating to the speech's persuasiveness, considering all five canons consistently.
Use Cicero's comprehensive framework to deliver a thoughtful evaluation that highlights the speaker's strengths while providing constructive feedback for improvement.
"""

  response_sum = get_completion(prompt_sum)
  return response_sum

def transcribe(audio):
    print(audio)

#   Whisper API

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)


    print(transcript)
    eval = audio_summary(transcript)

    return eval

table_topic = generate_topic()
print (table_topic)
description = "Here is your topic: " + table_topic
bot = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath",label="Start speaking"), outputs="text", title="Ask Cicero: Improve your Impromptu speaking",
    description=description,
    article="Tip: Improve your impromptu speaking skills by joining a Toastmasters club")

bot.launch()
