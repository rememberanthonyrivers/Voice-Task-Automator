Notes:

The important distinction

There are actually two separate jobs:

Job 1 — Hear you
Microphone
     ↓
Sounddevice
     ↓
Audio recording
Job 2 — Understand you
Audio recording
     ↓
Whisper
     ↓
Text

Then we'll eventually add:

Job 3 — Do something
Text
 ↓
Command understanding
 ↓
Automation
 ↓
Computer performs action

So the complete system will eventually be:

        YOU
         │
         │ "Create a file called test"
         ▼
    🎤 MICROPHONE
         │
         ▼
    SOUNDDEVICE
         │
         │ audio
         ▼
      WHISPER
         │
         │ text
         ▼
  COMMAND PROCESSOR
         │
         │ "create_file"
         ▼
     PYTHON ACTION
         │
         ▼
   test.txt CREATED

Now:

You now have this:

          YOU
           │
           │
           ▼
      🎤 MICROPHONE
           │
           ▼
      SOUNDEVICE
           │
           │ audio
           ▼
     recording.wav
           │
           ▼
        WHISPER
           │
           │ text
           ▼
   "Create a file called test"