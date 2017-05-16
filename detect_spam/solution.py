spam_words = ["free", "claim", ".com", "ringtone", "join", "urgent"]

input_file = "smsspamcollection/SMSSpamCollection"
spam_sms = []
nonspam_sms = []

with open(input_file) as f:
    input_lines = f.readlines()

for line in input_lines:
    if line.startswith("spam"):
        spam_sms.append(line)
    else:
        nonspam_sms.append(line)

spam_mislabel = 0
for line in spam_sms:
    if not any(word in line for word in spam_words):
        spam_mislabel += 1

nonspam_mislabel = 0
for line in nonspam_sms:
    if any(word in line for word in spam_words):
        nonspam_mislabel += 1

print("mislabeled: {} spam ({:.2f} success), {} non-spam ({:.2f} success)".format(spam_mislabel, 1 - (spam_mislabel / len(spam_sms)),
                                                                                nonspam_mislabel, 1 - (nonspam_mislabel / len(nonspam_sms))))

