# Week 1.2, Session 2: Task 6

try:
    machine_temp = int(input("Enter the temperature of the machine in Celsius: "))
    machine_psi = int(input("Enter the internal pressure of the machine in PSI: "))
    machine_operating = int(input("Enter the machine's operational status (1 = operating, 0 = stopped): "))
except:
    print("Invalid inputs.")
    exit()

if machine_operating == False:
    print("Machine is stopped. No action needed.")
    exit()

if machine_temp > 80:
    print("Dangerously high temperature detected.")
elif 50 <= machine_temp <= 80:
    print("Temperature is currently within safe limits.")
else:
    print("Temperature is low.")

if machine_psi > 100:
    print("Dangerously high pressure detected.")
elif 70 <= machine_psi <= 100:
    print("Pressure is currently stable.")
else:
    print("Pressure is low, systems running normally.")

if machine_temp > 80 or machine_psi > 100:
    print("Please shut down immediately.")
else:
    print("No further action needed.")