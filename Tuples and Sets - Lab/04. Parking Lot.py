num = int(input())

cars_in_parking = set()

for _ in range(num):
    command, plate_number = input().split(', ')
    if command == 'IN':
        cars_in_parking.add(plate_number)
    elif command == 'OUT':
        cars_in_parking.remove(plate_number)

if cars_in_parking:
    [print(plate_number) for plate_number in cars_in_parking]
else:
    print("Parking Lot is Empty")
