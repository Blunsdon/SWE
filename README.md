# SWE-Opgave
A simple docker-compose file That has a simple web service thats works on a Windows machine with Docker toolbox.


### Docker-compose
The *docker-compose.yml* file handles:
- Coordination of construction, startup, shutdown and destruction of the services (running in containers).
- Creation of networking bridges between running services (between containers). 
- Mapping of ports between containers and the host OS.
- Specification of storage volumes and mapping to local folders.

**Starting and stopping _without_ rebuilding:**
- Services that are already built can be started and stopped without re-building, using:
  - `docker-compose start`
  - `docker-compose stop`.

**Starting and stopping _with_ rebuilding:**
- The calls `docker-compose up -d --build` and `docker-compose down` ensure a re-build and destruction of containers at each run.

This is good during development, ensuring that any changes to build specs are captured in the services. But it is slow.

### Creating volumes
To make data persistent outside the Docker container, we use volumes. This is essentially just attached storage. 
To make the needed volumes:
- For the database, run `docker volume create data-volume`.

### Building the Webinterface image
The first build of the Webinterface image takes a while, as many different libraries must be fetched and installed.
- Build all the images for all services, without starting them, run: `docker-compose build`, or
- Build and _start_ all services: `docker-compose up -d --build`.
  
## Running on Windows with Docker Toolbox

To run on Windows, you must:
- Ensure LF line endings via Git.
- Share local folders via VirtualBox.
- Find your docker-machine IP address.

**LF line endings:** Before cloning the directory, ensure that your Git doesn't automatically modify files. Otherwise, Git will automatically convert to Windows style CRLF endings. It must be set up to keep Unix-style LF line endings. Run the command `git config --global core.autocrlf false`.

You can read more about it here: [Configuring Git to handle line endings](https://help.github.com/en/github/using-git/configuring-git-to-handle-line-endings).

If you forget to do this, you will get an error when the webinterface container tries to run the entrypoint script.

**Share local folders:** To share local files with the container (config files, etc.), you must set up a shared folder in VirtualBox:
  - The name of the shared folder _must_ be `c/docker`.


**IP address:** You can find the local IP address using `docker-machine ip Default`, and then access the services in your browser with the correct IP and port number, e.g. 192.168.99.100:80.

