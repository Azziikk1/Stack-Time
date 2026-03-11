import re
path = 'android/app/build.gradle'
with open(path, 'r') as f:
    content = f.read()
def bump(m):
    return 'versionCode ' + str(int(m.group(1)) + 1)
content = re.sub(r'versionCode\s+(\d+)', bump, content)
with open(path, 'w') as f:
    f.write(content)
print("versionCode incremented")
