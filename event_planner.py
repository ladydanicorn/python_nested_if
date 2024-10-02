#Task 1

attendees = float(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2

attendees = float(input("Enter number of attendees: "))
venue = "large hall," if attendees > 100 else "conference room," 

if attendees > 100:
    additions = "live band, and open bar"
else:
    additions = "audio system, and projector"
print(venue, additions)

#Task 3

attendees = float(input("Enter number of attendees: "))
venue = "large hall," if attendees > 100 else "conference room,"
meal = input("Enter meal choice: vegetarian or meat? ")
if attendees > 100:
    if meal == "vegetarian":
        additions = "live band, and open bar with meals from Veggie Delight Caterers"
    elif meal == "meat":
        additions = "live band, and open bar with meals from Gourmet Meals Caterers"
else:
    if meal == "vegetarian":
        additions = "audio system, and projector with meals from Veggie Delight Caterers"
    elif meal == "meat":
        additions = "audio system, and projector with meals from Gourmet Meals Caterers"

print(venue, additions)