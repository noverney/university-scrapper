from fake_student.driver import Driver
from utils.scrapper import get_text 
from utils.process_text import get_rent

browser = Driver()
url = "https://markt.unibas.ch/category/wohnen-angebot"
listings = browser.get_all_listings(url)
browser.close()


price_to_apartment = []
not_included = []
for i,apartment in enumerate(listings):
    text = str(get_text(apartment))
    rent = get_rent(text)
    if not rent:
        not_included.append(apartment)
    else:
        price_to_apartment.append((rent, apartment))
    print("Done", i, "/", len(listings))

for x in not_included:
    print(x)
print(len(not_included))

# write the results we have to look them up
prices = sorted(price_to_apartment, key=lambda x: x[0])
with open("result.csv", "w") as f:
    for price in prices:
        if price[0] >= 300:
            f.write(str(price[0]) + "," + price[1]+"\n")
    for unknown in not_included:
        f.write("UNKOWN,"+unknown+"\n")