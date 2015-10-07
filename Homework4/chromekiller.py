import subprocess
process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
results = process.stdout.read().decode('ascii').strip().split('\n')
for result in results:
    if "chrome" in result.lower():
        if "python" in result.lower():
            continue
        for i in range(0,100):
            result = result.replace("  "," ")
        print(result.split(" ")[1])
        killer = subprocess.Popen(["kill","-9",result.split(" ")[1]])