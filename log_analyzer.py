import csv

log_file_name = "auth.log"
ip_counts = {}

print("--- Robot Guard is starting the hunt! ---")

try:
    # --- STEP 1: READ THE BOOK ---
    with open(log_file_name, "r") as notebook:
        for line in notebook:
            if "Failed" in line:
                ip_address = line.split()[-1]
                ip_counts[ip_address] = ip_counts.get(ip_address, 0) + 1

    # --- STEP 2: (THE TIME-OUT RULE) ---
    print("\n🛡️ SECURITY ACTION TAKEN:")
    for ip, count in ip_counts.items():
        if count >= 3: 
            print(f"🚫 BLOCKING IP: {ip} (Too many fails: {count})")

    # --- STEP 3: WRITE THE SPREADSHEET ---
    with open('security_report.csv', 'w', newline='') as spreadsheet:
        writer = csv.writer(spreadsheet)
        writer.writerow(["IP Address", "Number of Fails"])
        for ip, count in ip_counts.items():
            writer.writerow([ip, count])
            
    print("\n✅ Everything worked perfectly! CSV created.")

# --- STEP 4: THE SAFETY GEAR () ---
except FileNotFoundError:
    print(f"❌ ERROR: I can't find '{log_file_name}'.")
except Exception as e:
    print(f"❌ A strange error happened: {e}")

print("--- Hunt Finished ---")