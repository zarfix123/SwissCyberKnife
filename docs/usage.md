# Cyber Swiss Army Tool Usage Guide

## Port Scanner Commands and Options

### Command Structure

```bash
swissknife port-scanner --target/-t <target> [OPTIONS]
```

### Options

   - ```--target``` / ```-t```: Required. Target IP address or domain.
   - ```--start-port``` / ```-sp```: Starting port number for the scan range. Default is 1.
   - ```--end-port``` / ```-ep```: Ending port number for the scan range. Default is 1024.
   - ```--all``` / ```-a```: Scan all ports from 1 to 65535. Overrides --start-port and --end-port.
   - ```--common```/ ```-c```: Scan only the most common ports. 
   - ```--tcp```: Perform a TCP scan (default if neither --tcp nor --udp specified). 
   - ```--udp```: Perform a UDP scan. 
   - ```--banner``` / ```-b```: Enable banner grabbing for open ports to retrieve service information.  
   - ```--output``` / ```-o```: Specify output file to save results (if used, requires --format).
   - ```--format``` / ```-f```: Format for output file. Choices are txt, json, csv.
   - ```--threads``` / ```-th```: Number of threads to use for parallel scanning. Default is 1. 
   - ```--timeout``` / ```-to```: Timeout (in seconds) for each connection attempt. Default is 0.5.
   - ```--retries``` / ```-r```: Number of retries for each port if scan fails initially. Default is 1.
   - ```--verbose``` / ```-v```: Show detailed scan progress in the console.

### Example Usage

- **Basic TCP Scan on localhost**
 ```bash
 swissknife port-scanner -t localhost -sp 20 -ep 25 --tco
 ```
- **Full TCP Port Scan with Banner Grabbing**
 ```bash
 swissknife port-scanner -t 192.168.1.1 -a -b
 ```
- **Common Ports Only, Multi-Threaded Scan**
 ```bash
 swissknife port-scanner -t example.com -c -th 5
 ```
- **UDP Scan with Retries and Custom Timeout**
 ```bash
 swissknife port-scanner -t 192.168.1.1 --udp -sp 53 -ep 53 -to 1 -r 3
 ```
- **Save Results to File in JSON Format**
 ```bash
 swissknife port-scanner -t 192.168.1.1 -sp 80 -ep 80 -o results.json -f json
 ```

### Notes
- Use ```sudo``` if permissions are needed for specific ports.


## Password Strength Commands and Options:

### Command Structure
```bash
swissknife pass-strength [OPTIONS] <password>
```

### Options
   - ```<password>```: **Required**. The password or hash to analyze.
   - ```--hash-check``` / ```-hc```: Check if the input is a known hash type (e.g, MD5, SHA-1) and if it hash known collision vulns
   - ```--entropy```/```-en```: Calculate and display the entropy of the password in bits
   - ```--rockyou-check```/```-ry```: Check if the password contains common dictionary words in rock you (src/extra/rockyou.txt)
   - ```--wordlist```/```-wl```: Check if the password contains words from the provided path to wordlist

### Example Usage
- **Basic Password Strength Check**
 ```bash
 swissknife pass-strength "StrongPassword!123"
 ```
- **Hash Check**
 ```bash
 swissknife pass-strength -hc "d41d8cd98f00b204e9800998ecf8427e"
 ```
- **Password Check with Entropy Calculation**
 ```bash
 swissknife pass-strength -en "StrongPassword!123"
 ```
- **Dictionary Check with Rockyou**
 ```bash
 swissknife pass-strength -ry "StrongPassword!123"
 ```
- **Dictionary Check with Custom wordlist**
 ```bash
 swissknife pass-strength -wl /path/to/wordlist.txt "StrongPassword!123"
 ```

### Notes:
- Enclosing the password in single quotes is recommended as with some terminals double quotes can cause errors due to  shell history expansion.
- Use ```sudo``` if your custom wordlist is in a root directory. 
- If you want to change the preset version of rockyou, it is in src/extra/rockyou.txt
- Entropy formula: length * log2(pool_size)
 

## Password Generator Commands and Options:

### Command Structure
```bash
swissknife pass-gen [OPTIONS]
```
### Options
   - ```--length```/```-l```: Specify password length to generate (default is 15)
   - ```--no-upper```/```-nu```: Uppercase letters will not be included in password generation 
   - ```-no-lower```/```-nl```: Lowercase letters will not be included in password generation
   - ```--no-num```/```-nn```: Numbers will not be included in password generation
   - ```--no-special```/```-ns```: Special characters will not be included in password generation
   - ```--exclude```/```-ex```: Takes a string of characters to exclude from password generation
   - ```--alphanumeric```/```-an```: Generates using only alphanumeric characters
   - ```--hex```: Generates a hex password with the amount of characters provided in length
   - ```--base64```/```-b64```: Generates a base64 password with the amount of chars provided in length
   - ```--hash```: Prompts the user for a string and hash algorithm. Hashes string via algorithm. 
   - ```--memorable```/```-mem```: Generates memorable password using entries in ```rockyou.txt```
   - ```--count```: Takes an integer for the amount of passwords/hashes you want to generate.
   - ```--seperator```/```-sep```: Used in coherence with ```--hash```. Takes a string to use as a seperator between entries. 

### Example Usage
**Basic Password Generation**
- **Generate a 12-character password with uppercase, lowercase, numbers, and special characters**
 ```bash
 swissknife pass-gen --length 12
 ```
- **Generate a 20-character alphanumeric password**
 ```bash
 swissknife pass-gen --length 20 --alphanumeric
 ```
- **Generate a 16-character password with no special characters**
 ```bash
 swissknife pass-gen --length 16 --no-special
 ```
**Generate Multiple Passwords**
- **Generate 5 random passwords of 15 characters each**
 ```bash
 swissknife pass-gen --length 15 --count 5
 ```
**Hexadecimal and Base64 Passwords**
- **Generate a 32-character hexadecimal password**
 ```bash
 swissknife pass-gen --hex --length 32
 ```
- **Generate a 24-character base64 password**
 ```bash
 swissknife pass-gen -b64 --length 24
 ```
**Excluding Specific Characters**
- **Generate a 10-character password excluding ```A```, ```B```, and ```C```**
 ```bash
 swissknife pass-gen --length 10 --exclude "ABC"
 ```
**Memorable Password Generation**
- **Generate a memorable password of 20 characters using words from ```rockyou.txt```**
 ```bash
 swissknife pass-gen --memorable --length 20
 ```
- **Generate a memorable password of 24 characters with hyphens as separators**
 ```bash
 swissknife pass-gen --memorable --length 24 --separator "-"
 ```
**Hashing a String**
- **Hash a custom string with an algorithm prompt**
 ```bash
 swissknife pass-gen --hash
 ```
   - Program Output:
      ```plaintext
      Enter the string you want to hash: mysecretpassword
      Available algorithms: md5, sha1, sha256, sha512, ...
      Enter the hashing algorithm to use (e.g., md5, sha1): sha256
      SHA256('mysecretpassword') = <hashed_value>
      ```







