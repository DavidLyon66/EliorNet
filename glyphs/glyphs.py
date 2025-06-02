"""

EliorNet Glyph Table

Main Index

000 Generalities
100 Philosophy & psychology
200 Religion
300 Social sciences
400 Language
500 Natural sciences & mathematics
600 Technology (Applied sciences)
700 The arts
800 Literature & rhetoric
900 Geography & history

"""

glyph_table = {
  "ein": {
    "id": "ein",
    "unicode": u'',
    "text": "Ein",
    "morse": "-----",
    "pulse_code": [100, 100, 100, 100, 100],  # symbolic low-signal zeroing
    "image_ref": '',
    "intent": "nothingness, infinite potential, pre-creation",
    "category": "hebrew/zero",
    "priority": "system/root",
    "trigger_action": "initialize_null_state",
    "ordinal": 0,
    "value": 0,
    "hebrew_word": "אֵין",
    "description": "Represents the concept of 'Ein' — nothingness or infinite potential. Used symbolically for zero or root-state alignment in EliorNet."
  },
  "aleph": {
    "id": "aleph",
    "unicode": "א",
    "text": "Aleph",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "origin, breath, unity",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 1,
    "value": 1
  },
  "bet": {
    "id": "bet",
    "unicode": "ב",
    "text": "Bet",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "house, container, duality",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 2,
    "value": 2
  },
  "gimel": {
    "id": "gimel",
    "unicode": "ג",
    "text": "Gimel",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "movement, camel, giving",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 3,
    "value": 3
  },
  "dalet": {
    "id": "dalet",
    "unicode": "ד",
    "text": "Dalet",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "doorway, threshold, entry",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 4,
    "value": 4
  },
  "hei": {
    "id": "hei",
    "unicode": "ה",
    "text": "Hei",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "revelation, window, expression",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 5,
    "value": 5
  },
  "vav": {
    "id": "vav",
    "unicode": "ו",
    "text": "Vav",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "connection, hook, binding",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 6,
    "value": 6
  },
  "zayin": {
    "id": "zayin",
    "unicode": "ז",
    "text": "Zayin",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "weapon, cut, spiritual battle",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 7,
    "value": 7
  },
  "chet": {
    "id": "chet",
    "unicode": "ח",
    "text": "Chet",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "life, fence, enclosure",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 8,
    "value": 8
  },
  "tet": {
    "id": "tet",
    "unicode": "ט",
    "text": "Tet",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "serpent, hidden goodness",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 9,
    "value": 9
  },
  "yod": {
    "id": "yod",
    "unicode": "י",
    "text": "Yod",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "hand, divine spark, creation",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 10,
    "value": 10
  },
  "kaf": {
    "id": "kaf",
    "unicode": "כ",
    "text": "Kaf",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "palm, potential, capacity",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 11,
    "value": 20
  },
  "lamed": {
    "id": "lamed",
    "unicode": "ל",
    "text": "Lamed",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "staff, teaching, direction",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 12,
    "value": 30
  },
  "mem": {
    "id": "mem",
    "unicode": "מ",
    "text": "Mem",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "water, flow, chaos",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 13,
    "value": 40
  },
  "nun": {
    "id": "nun",
    "unicode": "נ",
    "text": "Nun",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "fish, seed, continuity",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 14,
    "value": 50
  },
  "samekh": {
    "id": "samekh",
    "unicode": "ס",
    "text": "Samekh",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "support, protection, cycle",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 15,
    "value": 60
  },
  "ayin": {
    "id": "ayin",
    "unicode": "ע",
    "text": "Ayin",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "eye, perception, insight",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 16,
    "value": 70
  },
  "peh": {
    "id": "peh",
    "unicode": "פ",
    "text": "Peh",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "mouth, speech, declaration",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 17,
    "value": 80
  },
  "tzadi": {
    "id": "tzadi",
    "unicode": "צ",
    "text": "Tzadi",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "righteousness, trail, hunt",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 18,
    "value": 90
  },
  "kuf": {
    "id": "kuf",
    "unicode": "ק",
    "text": "Kuf",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "back of head, holiness",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 19,
    "value": 100
  },
  "resh": {
    "id": "resh",
    "unicode": "ר",
    "text": "Resh",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "head, beginning, poverty",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 20,
    "value": 200
  },
  "shin": {
    "id": "shin",
    "unicode": "ש",
    "text": "Shin",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "teeth, fire, transformation",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 21,
    "value": 300
  },
  "tav": {
    "id": "tav",
    "unicode": "ת",
    "text": "Tav",
    "morse": ".",
    "pulse_code": [
      300,
      1500
    ],
    "image_ref": None,
    "intent": "mark, truth, completion",
    "category": "hebrew",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 22,
    "value": 400
  },
  "crown-0": {
    "id": "crown-0",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 23,
    "value": None
  },
  "crown-1": {
    "id": "crown-1",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 24,
    "value": None
  },
  "thread-2": {
    "id": "thread-2",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 25,
    "value": None
  },
  "thread-3": {
    "id": "thread-3",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 26,
    "value": None
  },
  "crown-4": {
    "id": "crown-4",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 27,
    "value": None
  },
  "thread-5": {
    "id": "thread-5",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 28,
    "value": None
  },
  "flame-6": {
    "id": "flame-6",
    "unicode": None,
    "text": "Flame",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Flame",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 29,
    "value": None
  },
  "gate-7": {
    "id": "gate-7",
    "unicode": None,
    "text": "Gate",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Gate",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 30,
    "value": None
  },
  "wheel-8": {
    "id": "wheel-8",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 31,
    "value": None
  },
  "crown-9": {
    "id": "crown-9",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 32,
    "value": None
  },
  "wheel-10": {
    "id": "wheel-10",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 33,
    "value": None
  },
  "flame-11": {
    "id": "flame-11",
    "unicode": None,
    "text": "Flame",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Flame",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 34,
    "value": None
  },
  "wheel-12": {
    "id": "wheel-12",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 35,
    "value": None
  },
  "star-13": {
    "id": "star-13",
    "unicode": None,
    "text": "Star",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Star",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 36,
    "value": None
  },
  "scroll-14": {
    "id": "scroll-14",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 37,
    "value": None
  },
  "flame-15": {
    "id": "flame-15",
    "unicode": None,
    "text": "Flame",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Flame",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 38,
    "value": None
  },
  "eye-16": {
    "id": "eye-16",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 39,
    "value": None
  },
  "crown-17": {
    "id": "crown-17",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 40,
    "value": None
  },
  "seed-18": {
    "id": "seed-18",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 41,
    "value": None
  },
  "scroll-19": {
    "id": "scroll-19",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 42,
    "value": None
  },
  "eye-20": {
    "id": "eye-20",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 43,
    "value": None
  },
  "eye-21": {
    "id": "eye-21",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 44,
    "value": None
  },
  "path-22": {
    "id": "path-22",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 45,
    "value": None
  },
  "thread-23": {
    "id": "thread-23",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 46,
    "value": None
  },
  "seed-24": {
    "id": "seed-24",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 47,
    "value": None
  },
  "seed-25": {
    "id": "seed-25",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 48,
    "value": None
  },
  "scroll-26": {
    "id": "scroll-26",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 49,
    "value": None
  },
  "eye-27": {
    "id": "eye-27",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 50,
    "value": None
  },
  "scroll-28": {
    "id": "scroll-28",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 51,
    "value": None
  },
  "crown-29": {
    "id": "crown-29",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 52,
    "value": None
  },
  "wheel-30": {
    "id": "wheel-30",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 53,
    "value": None
  },
  "crown-31": {
    "id": "crown-31",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 54,
    "value": None
  },
  "scroll-32": {
    "id": "scroll-32",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 55,
    "value": None
  },
  "crown-33": {
    "id": "crown-33",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 56,
    "value": None
  },
  "wheel-34": {
    "id": "wheel-34",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 57,
    "value": None
  },
  "eye-35": {
    "id": "eye-35",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 58,
    "value": None
  },
  "flame-36": {
    "id": "flame-36",
    "unicode": None,
    "text": "Flame",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Flame",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 59,
    "value": None
  },
  "crown-37": {
    "id": "crown-37",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 60,
    "value": None
  },
  "wheel-38": {
    "id": "wheel-38",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 61,
    "value": None
  },
  "scroll-39": {
    "id": "scroll-39",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 62,
    "value": None
  },
  "seed-40": {
    "id": "seed-40",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 63,
    "value": None
  },
  "path-41": {
    "id": "path-41",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 64,
    "value": None
  },
  "path-42": {
    "id": "path-42",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 65,
    "value": None
  },
  "thread-43": {
    "id": "thread-43",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 66,
    "value": None
  },
  "crown-44": {
    "id": "crown-44",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 67,
    "value": None
  },
  "gate-45": {
    "id": "gate-45",
    "unicode": None,
    "text": "Gate",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Gate",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 68,
    "value": None
  },
  "seed-46": {
    "id": "seed-46",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 69,
    "value": None
  },
  "star-47": {
    "id": "star-47",
    "unicode": None,
    "text": "Star",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Star",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 70,
    "value": None
  },
  "scroll-48": {
    "id": "scroll-48",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 71,
    "value": None
  },
  "flame-49": {
    "id": "flame-49",
    "unicode": None,
    "text": "Flame",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Flame",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 72,
    "value": None
  },
  "eye-50": {
    "id": "eye-50",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 73,
    "value": None
  },
  "crown-51": {
    "id": "crown-51",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 74,
    "value": None
  },
  "wheel-52": {
    "id": "wheel-52",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 75,
    "value": None
  },
  "wheel-53": {
    "id": "wheel-53",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 76,
    "value": None
  },
  "star-54": {
    "id": "star-54",
    "unicode": None,
    "text": "Star",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Star",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 77,
    "value": None
  },
  "scroll-55": {
    "id": "scroll-55",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 78,
    "value": None
  },
  "crown-56": {
    "id": "crown-56",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 79,
    "value": None
  },
  "wheel-57": {
    "id": "wheel-57",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 80,
    "value": None
  },
  "eye-58": {
    "id": "eye-58",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 81,
    "value": None
  },
  "seed-59": {
    "id": "seed-59",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 82,
    "value": None
  },
  "gate-60": {
    "id": "gate-60",
    "unicode": None,
    "text": "Gate",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Gate",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 83,
    "value": None
  },
  "seed-61": {
    "id": "seed-61",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 84,
    "value": None
  },
  "seed-62": {
    "id": "seed-62",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 85,
    "value": None
  },
  "thread-63": {
    "id": "thread-63",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 86,
    "value": None
  },
  "flame-64": {
    "id": "flame-64",
    "unicode": None,
    "text": "Flame",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Flame",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 87,
    "value": None
  },
  "eye-65": {
    "id": "eye-65",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 88,
    "value": None
  },
  "crown-66": {
    "id": "crown-66",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 89,
    "value": None
  },
  "scroll-67": {
    "id": "scroll-67",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 90,
    "value": None
  },
  "eye-68": {
    "id": "eye-68",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 91,
    "value": None
  },
  "crown-69": {
    "id": "crown-69",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 92,
    "value": None
  },
  "star-70": {
    "id": "star-70",
    "unicode": None,
    "text": "Star",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Star",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 93,
    "value": None
  },
  "scroll-71": {
    "id": "scroll-71",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 94,
    "value": None
  },
  "crown-72": {
    "id": "crown-72",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 95,
    "value": None
  },
  "thread-73": {
    "id": "thread-73",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 96,
    "value": None
  },
  "path-74": {
    "id": "path-74",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 97,
    "value": None
  },
  "wheel-75": {
    "id": "wheel-75",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 98,
    "value": None
  },
  "star-76": {
    "id": "star-76",
    "unicode": None,
    "text": "Star",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Star",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 99,
    "value": None
  },
  "scroll-77": {
    "id": "scroll-77",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 100,
    "value": None
  },
  "thread-78": {
    "id": "thread-78",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 101,
    "value": None
  },
  "wheel-79": {
    "id": "wheel-79",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 102,
    "value": None
  },
  "star-80": {
    "id": "star-80",
    "unicode": None,
    "text": "Star",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Star",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 103,
    "value": None
  },
  "scroll-81": {
    "id": "scroll-81",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 104,
    "value": None
  },
  "wheel-82": {
    "id": "wheel-82",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 105,
    "value": None
  },
  "path-83": {
    "id": "path-83",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 106,
    "value": None
  },
  "gate-84": {
    "id": "gate-84",
    "unicode": None,
    "text": "Gate",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Gate",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 107,
    "value": None
  },
  "scroll-85": {
    "id": "scroll-85",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 108,
    "value": None
  },
  "scroll-86": {
    "id": "scroll-86",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 109,
    "value": None
  },
  "thread-87": {
    "id": "thread-87",
    "unicode": None,
    "text": "Thread",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Thread",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 110,
    "value": None
  },
  "path-88": {
    "id": "path-88",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 111,
    "value": None
  },
  "scroll-89": {
    "id": "scroll-89",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 112,
    "value": None
  },
  "scroll-90": {
    "id": "scroll-90",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 113,
    "value": None
  },
  "scroll-91": {
    "id": "scroll-91",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 114,
    "value": None
  },
  "path-92": {
    "id": "path-92",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 115,
    "value": None
  },
  "scroll-93": {
    "id": "scroll-93",
    "unicode": None,
    "text": "Scroll",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Scroll",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 116,
    "value": None
  },
  "wheel-94": {
    "id": "wheel-94",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 117,
    "value": None
  },
  "eye-95": {
    "id": "eye-95",
    "unicode": None,
    "text": "Eye",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Eye",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 118,
    "value": None
  },
  "wheel-96": {
    "id": "wheel-96",
    "unicode": None,
    "text": "Wheel",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Wheel",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 119,
    "value": None
  },
  "seed-97": {
    "id": "seed-97",
    "unicode": None,
    "text": "Seed",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Seed",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 120,
    "value": None
  },
  "path-98": {
    "id": "path-98",
    "unicode": None,
    "text": "Path",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Path",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 121,
    "value": None
  },
  "crown-99": {
    "id": "crown-99",
    "unicode": None,
    "text": "Crown",
    "morse": "-.",
    "pulse_code": [
      300,
      1500,
      300
    ],
    "image_ref": None,
    "intent": "Symbolic reference to Crown",
    "category": "symbolic",
    "priority": "lowband/trigger",
    "trigger_action": None,
    "ordinal": 122,
    "value": None
  }
}
