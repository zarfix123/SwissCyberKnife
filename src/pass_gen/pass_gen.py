import random
import hashlib
import base64
import os

def main(args):
    if args.hash:
        to_hash = input("Enter the string you want hashed: ")
        print("Available algorithms:", ', '.join(sorted(hashlib.algorithms_guaranteed)))
        algorithm = input("Enter the hashing algorithm to use to use (e.g., md5, sha1, sha256, sha512): ").lower()
        if algorithm in hashlib.algorithms_available:
            gen_hash(to_hash, algorithm)
        else:
            print(f"Error: Unsupported Hash Algorithm {algorithm}.")
    elif args.hex:
        gen_hex(args.length, args.count)
    elif args.base64:
        gen_base64(args.length, args.count)
    else:
        gen_pass(args)
        
def gen_pass(args):
    pool = ""
    length = args.length

    if not args.no_upper:
        pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not args.no_lower:
        pool += "abcdefghijklmnopqrstuvwxyz"
    if not args.no_num:
        pool += "0123456789"
    if not args.no_special:
        pool += "!@#$%^&*()_+-=[]{}|;:,.<>/?"
    
    if args.alphanumeric:
        pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        
            
    if args.exclude:
        pool = ''.join(c for c in pool if c not in args.exclude)
    
    if not pool:
        print("Error: Character Pool for password generation is empty. Cannot generate password")
    
        return
    
    passwords = []
    for i in range(args.count or 1):  
        if args.memorable:
            password = gen_memorable(args)
        else:
            password = ''.join(random.choice(pool) for i in range(args.length)) 
        passwords.append(password)
    
    for p in passwords:
        print(p)

def gen_hex(length, count):
    for i in range(count or 1):
        password = ''.join(random.choices("0123456789abcdef", k=length))
        print(password)

def gen_base64(length, count):
    for i in range(count or 1):
        num_bytes = (length * 3) // 4 + 1
        byte_data = os.urandom(num_bytes)
        encoded = base64.b64encode(byte_data).decode('utf-8')[:length]
        print(encoded)
    

def gen_hash(inp, alg):
    hash_obj = hashlib.new(alg)
    hash_obj.update(inp.encode())
    print(f"{alg.upper()}('{inp}') = {hash_obj.hexdigest()}")

def gen_memorable(args):
    wordlist_path = "src/extra/rockyou.txt"
    try:
        with open(wordlist_path, "r", encoding='utf-8',errors='ignore') as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: Rockyou wordlist not found at src/extra/rockyou.txt. Please install wordlist and place into that path")
        return ""
    
    seperator = args.seperator if args.seperator else ""
    num_words = max(1, args.length // 6)
    password_words = random.choices(words, k=num_words)
    password = seperator.join(password_words)
    
    if len(password) > args.length:
        password = password[:args.length]
    elif len(password) < args.length:
        padding = ''.join(random.choices("0123456789", k=args.length - len(password)))
        password += padding
    
    return password