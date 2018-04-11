from prac_07.guitar import Guitar

thunderbird = Guitar("thunderbird", 1902, 1520.00)

print(thunderbird.is_vintage())
print("expected True")

print(thunderbird.get_age())
print("expected 116")