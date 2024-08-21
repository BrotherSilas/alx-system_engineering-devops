# Web Stack Debugging 4

## Project Overview
This project is part of the ALX System Engineering and DevOps track.

Tasks
0. Sky is the limit, let's bring that limit higher
 The goal is to debug and optimize an Nginx web server under high load conditions using Puppet. The problem identified was that the server failed to handle a significant number of requests when tested with ApacheBench, leading to over 943 failed requests out of 2000.

The Puppet manifest,0-the_sky_is_the_limit_not.pp`, automates the necessary adjustments to the Nginx configuration, ensuring the server can handle high concurrency with zero failed requests.

1. Increase the number of Nginx worker processes to match the number of available CPU cores.
2. Increase the maximum number of open files per worker process.
3. Ensure the Nginx service is running and enabled to start at system boot.

## Requirements
- **Operating System:** Ubuntu 14.04 LTS
- **Puppet Version:** 3.4
- **Nginx Version:** 1.4.6
- **ApacheBench Version:** 2.3

## Files
- **0-the_sky_is_the_limit_not.pp**: Puppet manifest file that contains the configuration changes to optimize Nginx.

## Usage
1. **Install Puppet** (if not already installed):
   ```bash
   sudo apt-get update
   sudo apt-get install puppet -y
2. **Apply the Puppet Manifest** :
   Run the following command to apply the manifest and optimize Nginx:
   ```bash
   sudo puppet apply 0-the_sky_is_the_limit_not.pp
3. Benchmark the Server:
   Use ApacheBench to test the server's performance after applying the Puppet manifest:
   ```bash
   ab -c 100 -n 2000 http://localhost/
4. Ensure the benchmark results show zero failed requests.
