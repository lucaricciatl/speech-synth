
docker run -it voice-synthesizer

echo "Starting backend"
# Start program 1 in the background
echo "cd vci && python start_server.py &"
cd vci && python start_server.py &
echo "..."
echo "Done"
echo "Starting frontend"
# Start program 2 in the background
cd webapp && npm start &
echo "..."
echo "Done"

# Optionally, wait for all background processes to finish
wait