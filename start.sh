!/bin/sh

# Avvia il container Docker
docker run -d -p 5000:5000 -p 3000:3000 --network host -it --name voice-synthesizer-container voice-synthesizer /bin/sh -c "/start-service.sh"