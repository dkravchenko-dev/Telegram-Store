pkill -9 -f 'python3 main.py'
source .venv/bin/activate
nohup python3 main.py > output.log 2>&1 &
