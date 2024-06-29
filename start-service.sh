echo 'Starting backend'
# Avvia il primo programma in background
echo 'cd vci && python start_server.py &'
cd vci && python start_server.py &
echo '...'
echo 'Done'
echo 'Starting frontend'
#Avvia il secondo programma in background
cd webapp && npm start &
echo '...'
echo 'Done'
#Opzionalmente, aspetta che tutti i processi in background finiscano
wait