print("=== Power Calculator ===")

base = int(input("What is the base number?: "))
power = int(input("What is the power?: "))

result = 1

for i in range(1, power + 1):
  result = base * result
  print(f"Step {i}: result is {result}")

print(f"Final Result: {result}")
