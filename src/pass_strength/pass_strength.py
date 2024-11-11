import re
import math
import os

DEFUALT_DICTIONARY="src/extra/rockyou.txt"
def main(args):
    if args.hash_check:
        hash_type, is_vulnerable = analyze_hash(args.password)
        print(f"Hash Type: {hash_type}")
        if is_vulnerable:
            print("This hash is vulnerable to collisions")
        else:
            print("This hash type is considered secure against known collision attacks")
    else:
        score, strength, feedback = analyze_password(args.password)  
        print(f"Password score: {score}, Strength: {strength}")
        for word in feedback:
            print(f" -{word}")
        
        if args.entropy:
            entropy=calculate_entropy(args.password)
            print(f"Entropy: {entropy:.2f} bits")
            if entropy < 28:
                print("Entropy Interpretation: Very Weak")
            elif 28 <= entropy < 36:
                print("Entropy Interpretation: Weak")
            elif 36 <= entropy < 60:
                print("Entropy Interpretation: Moderate")
            elif 60 <= entropy < 128:
                print("Entropy Interpretation: Strong")
            else:
                print("Entropy Interpretation: Very Strong")
        
        if args.rockyou_check:
            dictionary_feedback= dictionary_check(args.password, DEFUALT_DICTIONARY)
            print("Dictionary Check: ", dictionary_feedback)
            
        if args.wordlist:
            word_path = args.wordlist
            dictionary_feedback= dictionary_check(args.password, word_path)
            print("Custom Wordlist Check: ", dictionary_feedback)
            
        
def analyze_hash(password):
    if re.match(r"^[a-fA-F0-9]{32}$", password):
        return "MD5 or NTLM", True
    elif re.match(r"^[a-fA-F0-9]{40}$", password):
        return "SHA-1", True
    elif re.match(r"[a-fA-F0-9]{64}$", password):
        return "SHA-256", True
    elif re.match(r"[a-fA-F0-9]{128}$", password):
        return "SHA-512", True
    else:
        return "Hash Type not Recognized", False
    



def analyze_password(password):
    score = 0
    feedback = []
    
    # Check Length
    if len(password) < 8:
        feedback.append("✗ Password is too short, Use at least 8 characters (recommended 12)")
    elif len(password) > 11:
        feedback.append("✓ Great password length!")
        score +=2
    else:
        feedback.append("✓ Decent password length, consider adding a few more characters")
        score +=1
    
    if re.search(r"[A-Z]", password):
        score +=1
        feedback.append("✓ Good Uppercase letter usage.")
    else:
        feedback.append("✗ Consider adding uppercase letters for more security")
    
    if re.search(r"[a-z]", password):
        score +=1
        feedback.append("✓ Good lowercase letter usage.")
    else:
        feedback.append("✗ Consider adding lowercase letters for more security")
    
    if re.search(r"\d", password):
        score +=1 
        feedback.append("✓ Good usage of numbers")
    else:
        feedback.append("✗ Consider adding numbers for more security")
    
    if re.search(r"[\W_]", password):
        score +=1
        feedback.append("✓ Good special character usage")
    else:
        feedback.append("✗ Consider adding special characters for further security (!, @, $, #)")
    
    if re.search(r"(12|pass|qwerty|abc|32)", password, re.IGNORECASE):
        feedback.append("✗ Avoid using common password patterns for higher security")
    else:
        score+=1
        feedback.append("✓ No usage of common password phrases")
    
    if re.search(r"(.)\1{2,}", password):
        feedback.append("✗ Avoid repeated sequences/characters such as aaa, 111 for better security")
    else:
        feedback.append("✓ No usage of repeated characters")
        
    if score == 7:
        return score, "Perfect", feedback
    elif 4<=score<= 6:
        return score, "Strong", feedback
    elif 2<=score<=3:
        return score, "Moderate", feedback
    else:
        return score, "Weak", feedback

def calculate_entropy(password):
    pool_size = 0
    if re.search(r"[a-z]", password):
        pool_size += 26
    if re.search(r"[A-Z]", password):
        pool_size += 26
    if re.search(r"\d", password):
        pool_size += 10
    if re.search(r"\W", password):
        pool_size += 32 
    
    
    if pool_size > 0:
        entropy = len(password) * math.log2(pool_size)
    else:
        entropy = 0
    return entropy

def dictionary_check(password, wordlist):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for word in file:
                word = word.strip().lower()
                if word and word in password.lower():
                    return f"Contains common word '{word}', consider changing it."
                
    except FileNotFoundError:
        return f"Dictionary not found at '{wordlist}'."
    
    return None

    
    
    
