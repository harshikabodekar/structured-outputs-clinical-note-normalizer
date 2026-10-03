NOTES = [
    # clear
    ("clear", "Resident complained of mild headache since morning. BP 128/82. Took lisinopril 10mg at 8am."),
    ("clear", "Patient reports nausea after breakfast. BP measured at 118/76. Metformin taken with meal."),
    ("clear", "Dizziness when standing up, lasted 2 minutes. BP 135/88. Took amlodipine 5mg this morning."),
    ("clear", "Patient had chest tightness at 3pm, resolved with rest. BP 142/90. Took aspirin 75mg."),
    ("clear", "Complains of joint pain in knees. BP 122/80. Paracetamol 500mg given at noon."),
    # missing info
    ("missing", "Patient felt tired all day. No BP taken. Medication not recorded."),
    ("missing", "Resident had a headache this evening. Took something for it."),
    ("missing", "Patient dizzy after walking. BP not checked."),
    ("missing", "Patient refused lunch, seemed low energy. Nothing else noted."),
    ("missing", "Cough since last night, no fever mentioned. BP and meds not noted."),
    # conflicting
    ("conflicting", "Patient reports dizziness. BP 130/85 first reading, 160/100 on recheck. Took amlodipine."),
    ("conflicting", "Daughter says mother took her tablets, patient says she did not. Mild headache."),
    ("conflicting", "BP written as 120/80 in the log but nurse says it felt higher. Patient has blurry vision."),
    ("conflicting", "Patient says headache started yesterday, caregiver says it began today. BP 138/90."),
    ("conflicting", "Took metformin in morning per patient, but pill box still full. Complains of weakness."),
    # vague / messy
    ("vague", "pt dizzy after lunch, bp maybe high?? took meds, not sure which"),
    ("vague", "feeling off since morning, bp 14/9 ish, took the usual white pill"),
    ("vague", "head hurting bad, BP high-ish, took 2 tabs of the BP one i think"),
    ("vague", "pt c/o dizzy, bp 150/9? (smudged), meds as per chart"),
    ("vague", "shaky and sweaty before dinner, BP around 110 over 70, had her sugar tablet"),
    ("vague", "Patient says she feels weird and not herself. Took morning medicines. BP normal."),
]