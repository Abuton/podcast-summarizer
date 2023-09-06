## Summarize & highlight podcast episodes for busy listeners

 The focus of this project is to build an LLM app that summarizes a podcast episode, identifies podcast guests, and identifies key highlights.

 ### The problem
 There are many interesting podcast that release good content once or twice per week. I'd lke to listen to all of them to gain experience and be more knownledgeble but I'm occupied with other tasks. How can I get the gist of what a particular podcast discuss in a session without spending so much time listening to the entire podcast.

 ### The solution
 Use OpenAI API to interact with Chatgpt, get a summary of what's discussed and highlight key notes

 #### Steps (keeping it simple)
 - Podcast Transcription and Information Extraction
    - Retrive the audio file, I will obtain the RSS from listennotes
    - Download the mp3 with wget
    - Transcribe the mp3 using whisper library (STT) (This may take more time).
    - Create a summary of the podcast