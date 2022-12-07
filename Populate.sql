INSERT INTO PERSON
VALUES 	(123456788,"tina", "w", "24 School Drive", "password", 4034034033, "t.w@ucalgary.ca"), 
        (133456789,"ramneet", "h", "23 School Drive", "password", 4034034034, "r.h@ucalgary.ca"), 
        (123456798,"isaac", "d", "22 School Drive", "password", 4034034043, "i.d@ucalgary.ca"), 
        (466709091, "member1", "stark", "87 Member street", "password", 4039925656, "member1@ucalgary.ca"),
        (466707071, "member2", "mcdonald", "91 Member street", "password", 4038855858, "member2@ucalgary.ca"),
        (466606061, "member3", "smith",  "3 Member street", "password", 4039919911, "member3@ucalgary.ca"), 
        (123333335,"manager", "f", "24 Manager Lane", "password", 4035445454, "manager@ucalgary.ca"), 
        (123366775, "owner", "j","24 Owner Lane", "password",  4035690012, "owner@ucalgary.ca");

INSERT INTO RESTRICTED_USER
VALUES  (123456788, 1, "t.w@ucalgary.ca", "tina", "w", "24 School Drive", "password", 4034034033), 
        (133456789, 2, "r.h@ucalgary.ca", "ramneet", "h", "23 School Drive", "password", 4034034034), 
        (123456798, 3, "i.d@ucalgary.ca", "isaac", "d", "22 School Drive", "password", 4034034043);

INSERT INTO EMPLOYEE
VALUES  (123456788, 1, "t.w@ucalgary.ca", "tina", "w", "24 School Drive", 4034034033, "password", 1), 
        (133456789, 2, "r.h@ucalgary.ca", "ramneet", "h", "23 School Drive", 4034034034, "password", 1), 
        (123456798, 3, "i.d@ucalgary.ca", "isaac", "d", "22 School Drive", 4034034043, "password", 1);

INSERT INTO ASSOCIATE
VALUES  (123456788, 1, "t.w@ucalgary.ca", "tina", "w", "24 School Drive", 4034034033, "password", 1), 
        (133456789, 2, "r.h@ucalgary.ca", "ramneet", "h", "23 School Drive", 4034034034, "password", 1);

INSERT INTO TRAINER
VALUES (123456798, 3, "i.d@ucalgary.ca", "isaac", "d", "22 School Drive", 4034034043, "password", 1);

INSERT INTO ADMIN
VALUES (123333335, 1, "manager@ucalgary.ca", "manager", "f", "24 Manager Lane", "password", 4035445454), 
		(123366775, 2, "owner@ucalgary.ca", "owner", "j","24 Owner Lane", "password",  4035690012);

INSERT INTO MANAGER
VALUES (123333335, 1, "manager@ucalgary.ca", 1, "manager", "f", "24 Manager Lane", "password", 4035445454);

INSERT INTO OWNER
VALUES (123366775, 2, "owner@ucalgary.ca", 1, "owner", "j", "password","24 Owner Lane", 4035690012);


INSERT INTO CLIENT
VALUES (466709091, 1, "member1@ucalgary.ca", "member1", "stark", "password", "87 Member street", 4039925656),
        (466707071, 2, "member2@ucalgary.ca", "member2", "mcdonald", "password", "91 Member street", 4038855858),
        (466606061, 3, "member3@ucalgary.ca", "member3", "smith", "password", "3 Member street", 4039919911);

INSERT INTO MEMBER
VALUES (466709091, 1, 1, "member1@ucalgary.ca", True, "member1", "stark", "87 Member street", "password", 4039925656), 
        (466707071, 2, 2, "member2@ucalgary.ca", FALSE, "member2", "mcdonald", "91 Member street", "password", 4038855858), 
        (466606061, 3, 3, "member3@ucalgary.ca", True, "member3", "smith", "3 Member street", "password", 4039919911);
        
INSERT INTO CLASS
VALUES (1, "Monday", "1:00", 1, 3, "i.d@ucalgary.ca", 123456798), 
        (2, "Tuesday", "10:00", 1, 3, "i.d@ucalgary.ca", 123456798), 
        (3, "Friday", "8:00", 1, 3, "i.d@ucalgary.ca", 123456798);
        
INSERT INTO ROOMS
VALUES (1, "Monday" , "1:00"),
        (1, "Tuesday", "1:00"), 
        (2, "Monday", "1:00");
        
INSERT INTO GYM 
VALUES (1, "59 Gym Lane", 123366775, 123333335);

INSERT INTO EQUIPMENT
VALUES (1, "Working", 20, 1, "Bench"), 
        (2, "Broken", 125, 1, "Barbell"), 
        (3, "Working", 152, 1, "Dumbell"), 
        (4, "Working", 1, 1, "Squat Rack"), 
        (5, "Broken", 9, 1, "Leg Press"), 
        (6, "Working", 10, 1, "Kettle Bell"), 
        (7, "Working", 44, 1, "Medicine Ball");
        
INSERT INTO SUPPLIES
VALUES ("Cloth", 1, 400, 1), 
        ("Water Bottle", 2, 20, 1), 
        ("Barbell Pad", 3, 125, 1), 
        ("Foam Roller", 4, 20, 1), 
        ("Hand Sanitizer", 5, 400, 1), 
        ("Mirror", 6, 15, 1);
        
INSERT INTO SUBSCRIPTION
VALUES ("gym_spotify", "spotify", 1), 
        ("gym_netflix", "netflix", 1), 
        ("gym_hulu", "hulu", 1), 
        ("gym_apple", "apple Music", 1);
        

INSERT INTO WEEKLY_SCHEDULE
VALUES ("t.w@ucalgary.ca", 1, '6-10', 'Sunday'),
        ("r.h@ucalgary.ca", 1, '10-2', 'Sunday'),
        ("r.h@ucalgary.ca", 1, '2-6', 'Sunday'),
        ("i.d@ucalgary.ca", 1, '6-12', 'Sunday'),
        ("r.h@ucalgary.ca", 1, '6-10', 'Monday'),
        ("t.w@ucalgary.ca", 1, '10-2', 'Monday'),
        ("r.h@ucalgary.ca", 1, '2-6', 'Monday'),
        ("i.d@ucalgary.ca", 1, '6-12', 'Monday'),
        ("i.d@ucalgary.ca", 1, '6-10', 'Tuesday'),
        ("i.d@ucalgary.ca", 1, '10-2', 'Tuesday'),
        ("r.h@ucalgary.ca", 1, '2-6', 'Tuesday'),
        ("i.d@ucalgary.ca", 1, '6-12', 'Tuesday'),
        ("i.d@ucalgary.ca", 1, '6-10', 'Wednesday'),
        ("t.w@ucalgary.ca", 1, '10-2', 'Wednesday'),
        ("t.w@ucalgary.ca", 1, '2-6', 'Wednesday'),
        ("i.d@ucalgary.ca", 1, '6-12', 'Wednesday'),
        ("t.w@ucalgary.ca", 1, '6-10', 'Thursday'),
        ("r.h@ucalgary.ca", 1, '10-2', 'Thursday'),
        ("r.h@ucalgary.ca", 1, '2-6', 'Thursday'),
        ("i.d@ucalgary.ca", 1, '6-12', 'Thursday'),
        ("t.w@ucalgary.ca", 1, '6-10', 'Friday'),
        ("r.h@ucalgary.ca", 1, '10-2', 'Friday'),
        ("t.w@ucalgary.ca", 1, '2-6', 'Friday'),
        ("i.d@ucalgary.ca", 1, '6-12', 'Friday'),
        ("t.w@ucalgary.ca", 1, '6-10', 'Saturday'),
        ("i.d@ucalgary.ca", 1, '10-2', 'Saturday'),
        ("r.h@ucalgary.ca", 1, '2-6', 'Saturday'),
        ("t.w@ucalgary.ca", 1, '6-12', 'Saturday');
