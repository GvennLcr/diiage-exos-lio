# Owasp Top 10

This work is to improve my skills in Python, while educating students about misconfigurations, outdated components and bad practice patterns on web environement. **Feel free to give me advices to improve the code, or if you want to PR a better version of it.**
All of this is based on the Owasp Top 10 project. https://owasp.org/Top10/
Each containers contains a specific vulnerability and a description of the way to resolve it.

**DO NOT USE IN A PRODUCTION ENVIRONEMENT !!!!!**

Build the images :
```docker build --pull --rm -f "/path/to/your/Dockerfile" -t docker:latest "docker"```

Run containers :
```docker run -d -p unusedport:80 -t "docker"```