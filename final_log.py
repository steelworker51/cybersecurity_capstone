import csv  # Give the robot a pen 

# 1. SETUP
log_file_name = "auth.log"  # Tell the robot which file to look at 
ip_counts = {}              # Empty mailboxes for counting 
boss_mode_attempts = []     # List for 'sudo' or 'root' users 
total_lines = 0             # Tally for total lines scanned 

print("--- Robot Guard is generating the Final Report! ---") 

# 2. READING THE LOGS
try:
    with open(log_file_name, "r") as notebook: 
        for line in notebook: 
            total_lines += 1 
            
            # Clean the line for processing
            clean_line = line.strip() 

            # CHECK 1: Failed password attempts
            if "Failed" in clean_line: 
                # Finds the IP at the end of the line 
                ip_address = clean_line.split()[-1]
                
                # Update the mailbox/dictionary 
                ip_counts[ip_address] = ip_counts.get(ip_address, 0) + 1
            
            # CHECK 2: Boss Mode (Sudo or Root) 
            if "sudo" in clean_line or "root" in clean_line: 
                boss_mode_attempts.append(clean_line) 

    # 3. PRINTING THE SUMMARY REPORT
    print("\n" + "=" * 30) 
    print("SECURITY SUMMARY REPORT") 
    print("-" * 30) 
    print(f"Total lines scanned: {total_lines}") 
    print(f"Unique IPs Flagged: {len(ip_counts)}") 
    print(f"Boss Mode Threats Detected: {len(boss_mode_attempts)}") 
    print("-" * 30)

    # Show top offenders if any exist
    if ip_counts: 
        print("TOP OFFENDERS:") 
        for ip, count in ip_counts.items(): 
            print(f"- {ip}: {count} failed attempts") 

    # 4. SECURITY ACTION (THE TIME-OUT RULE)
    print("\nSECURITY ACTION TAKEN:") 
    for ip, count in ip_counts.items(): 
        if count >= 3: # If someone fails 3 or more times 
            print(f" BLOCKING IP: {ip} (Too many fails: {count})") 

    # 5. EXPORTING TO CSV 
    try:
        with open('security_report.csv', 'w', newline='') as spreadsheet: 
            writer = csv.writer(spreadsheet)
            # Write the "Header" 
            writer.writerow(["IP Address", "Number of Fails"])
            # Write the data 
            for ip, count in ip_counts.items(): 
                writer.writerow([ip, count]) 
        print("\nSpreadsheet 'security_report.csv' has been created!") 
    except Exception as e:
        print(f"Error creating CSV: {e}")

except FileNotFoundError: 
    print("Oops! I can't find the 'auth.log' file. Did you make it yet?") 
except Exception as e: 
    print(f"The robot had a boo-boo: {e}") 

print("\n--- Hunt finished! ---") 
