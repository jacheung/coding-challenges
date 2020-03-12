test = "Product Tag : men, Product Type : Suit" \
"- How tall are you? : 5 ft 11 in" \
"- Whats your weight? : 198" \
"- What is your normal blazer size?-Blazer size : 42" \
"- What is your normal blazer size?-Blazer length : Regular" \
"- What best describes your typical dress shirt size?-Neck size : Not Sure" \
"- What best describes your typical dress shirt size?-Sleeve length : Not Sure" \
"- Which best describes your build? : Rectangle" \
"- Which best describes your midsection? : Pretty fit" \
"- Look at yourself in the mirror and relax your shoulders. Which best describes your shoulder? : Rolled back" \
"- How much shirt cuff do you like to show? : Modern: 0.25 inch of cuff" \
"- Which best describes your shoulder slope? : Moderate" \
"- What blazer length do you prefer? : Classic: Traditional suit length" \
"- What size pant do you normally wear?-Waist size : 36" \
"- What size pant do you normally wear?-Inseam length : 30" \
"- Lets talk about your tush. Which best describes your butt shape? : Normal Seat" \
"- What kind of rise do you prefer? : Normal-rise" \
"- What kind of pant break do you prefer? : Zero Break: Barely touching shoe on the front" \
"- How tapered would you like your pants? : Tailored but comfortable"

tmp = test.split(',')
tmp.split('-')


clean = {}
for b in range(len(tmp)):
    extract = tmp[b].split('?')
    clean[str(extract[0]).replace(" ", "")] = str(extract[-1]).replace(" ", "")
