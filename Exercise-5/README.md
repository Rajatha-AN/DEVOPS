# Exercise 5 - AppArmor Security for Docker Flask Application

## Objective

To secure a Flask application running inside a Docker container using an AppArmor security profile.

## Files

- `app.py` - Flask application
- `Dockerfile` - Docker image configuration
- `my-apparmor-profile` - Custom AppArmor security profile

## Procedure

### 1. Build the Docker Image

```bash
docker build -t flask-apparmor .
2. Load the AppArmor Profile
sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
3. Verify the Profile
sudo aa-status | grep my-apparmor-profile

The profile was successfully loaded and attached to the Python process.

4. Run the Container with AppArmor
sudo docker run -d --name flask-apparmor \
  --security-opt apparmor=my-apparmor-profile \
  -p 5000:5000 flask-apparmor
5. Verify the Flask Application

The application was accessed through:

http://localhost:5000

Output:

Hello, this is a secure Flask application running inside a Docker container!
6. Test AppArmor Restriction

An attempt was made to read /etc/shadow from inside the container:

sudo docker exec flask-apparmor python -c "open('/etc/shadow').read()"

The operation was denied:

PermissionError: [Errno 13] Permission denied: '/etc/shadow'

This confirms that the AppArmor profile successfully restricted access to sensitive system files.

Result

The Flask application was successfully executed inside a Docker container with a custom AppArmor security profile. Network access was permitted while access to sensitive system files was restricted.
