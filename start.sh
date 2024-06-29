#!/bin/sh

# Avvia il container Docker
docker run -d -p 5200:5200 -p 8000:8000 -it --name voice-synthesizer-container voice-synthesizer