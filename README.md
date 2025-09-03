# PetAdoption
A system with classes for pets, shelters, and adopters, facilitating pet searches, adoption processes, and shelter management.

# Functional Requirements

- [OK] User Account Management: Users can create and manage their accounts;
- [OK] Pet Profile Management: Managing profiles for pets available for adoption;
- [OK] Shelter and Rescue Organization Profiles: Profiles for shelters and rescue organizations;
- [OK] Event Listing and Management: Listing events like adoption drives and fundraisers;
- [OK] Educational Resources: Providing resources on pet care and adoption;
- [OK] Success Stories and Testimonials: Sharing success stories and testimonials from adopters;
- [OK] Community Forum: A forum for adopters and pet lovers to share experiences and advice.
- [OK] Search and Filter Options: Enabling users to search and filter pets based on various criteria;
- [OK] Adoption Application Processing: Handling and processing adoption applications;
- [OK] Donation Processing: Facilitating donations to shelters and rescue organizations.

# Software Project (Classes)

## Event [OK]
Shelter organized events (fundraisers, pet fairs, etc.)

- has:
    - location (Address)
    - date (Date)
    - status (str)
        - indicates if event has happened, has been cancelled or is in stand-by or in planning

- can:
    - update: change any info
    - cancel: change status to 'cancelled'
    - end: chage status to 'done'

## Donation [OK]
A money donation to a shelter

- has:
    - donor (Adopter)
    - receiver (Shelter)
    - ammount (float)
    - date (Date)

- can:
    - format: returns the donation's info in a pretty formatted way

---

## Question [OK]

- has:
    - name (str)
    - option (list[str])
    - preferred_answer (str): the best/right answer

- can:
    - formatted_list: formats the question and options in a list of strings

## Form [OK]
Template for aplication (list of questions)

- has:
    - questions (list[question])

- can:
    - add_question
    - formatted_list: formats all questions

## Answer [OK]

- has:
    - question (Question)
    - user_option (str)
    - is_preferred (bool)

- can
    - format: returns the donation's info in a pretty formatted way

## Application [OK]
An Adopter's application to adopt a pet

- has:
    - applicant (Adopter)
    - pet (Pet)
    - answers (list[Answer])
    - score (str)
        - indicates the compatibility between the applicant's answers and the expected answers
    - status (str)
    - feedback (str)

- can:
    - format: returns the questions, answers, score and status in a pretty formatted way

---

## Address [OK]
Class for storing a structured address

- has:
    - street (str)
    - district (str)
    - number (str): can be "10", "11A", etc.
    - postal_code (int)

- can:
    - format: returns a pretty formatted address

## Profile [OK]
General informations for users and pets

- has:
    - name (str)
    - birth/open date (Date)
    - address (Adress)
    - description (str)

- can:
    - update_profile: change any attribute
    - format: returns all the profile's info in a pretty formatted way


---

## User [OK]

- has:
    - username (str)
    - profile (Profile)
    - allowed_post_types (list[str])
    - posts (list[Post])

<!-- >  TODO: review methods -->
- can:
    - login: returns User object
    - format: returns brief User description

## Adopter (User) [OK]
Inherits User's attributes and methods

- has:
    - donations (list[Donation])
    - applications (list[Aplication])

- can:
    - donate: donate to a shelter
    - apply: fill out form to adopt pet

## Shelter (User) [OK]
Inherits User's attributes and methods.

Organizations that rescue pets and facilitate adoptions.

- has:
    - allowed_pet_types (list[str])
    - pets (list[Pet])
    - events (list[Event])

- can:
    - add_allowed_pet_type: add a new species to shelter's list
    - is_allowed(pet_type): indicates if Shelter accepts pet_type
    - [WIP] approve_application: approve an application to adopt a pet, deny and provide feedback for all others and make applicant the pet's tutor
    - [WIP] deny_application: deny an application and provide feedback

---

## Pet [OK]
Rescued animals

- has:
    - profile (Profile)
    - pet_type (str)
    - breed (str)
    - fur_color (str)
    - status (str)
        - rescued, in_treatment, available_for_adoption, adopted
    - form (Form)
        - questions for adoption application form
    - tutor (Adopter)

- can:
    - treat: change status to 'in_treatment'
    - make_available: change status to 'available_for_adoption'
    - add_template_question: add a question to application_template
    - apply_to_adopt: fill the pet's form to apply for adoption

---

## Post [OK]
A social post

- has:
    - author (User)
    - post_type (str)
    - title (str)
    - content (str)
    - comments (list[Post])
    - likes (list[User])

- can:
    - update: change post's info
    - comment: add a comment to post
    - like: like the post
    - format: returns posts info in a pretty formatted way


---

## Query
A class for searching and filtering objects (pets, events, shelters, posts)

- has:
    - options: all available instances
    - criteria: all available criteria for filtering
    - filters: user selected filters
    - result: instances that  fit selected filters

- can:
    - search: find one specific object
    - filter: filter all objects based on various criteria
