# PetAdoption
A system with classes for pets, shelters, and adopters, facilitating pet searches, adoption processes, and shelter management.

# Functional Requirements

- User Account Management: Users can create and manage their accounts;
- Pet Profile Management: Managing profiles for pets available for adoption;
- Shelter and Rescue Organization Profiles: Profiles for shelters and rescue organizations;
- Event Listing and Management: Listing events like adoption drives and fundraisers;
- Educational Resources: Providing resources on pet care and adoption;
- Success Stories and Testimonials: Sharing success stories and testimonials from adopters;
- Community Forum: A forum for adopters and pet lovers to share experiences and advice.
- Search and Filter Options: Enabling users to search and filter pets based on various criteria;
- Adoption Application Processing: Handling and processing adoption applications;
- Donation Processing: Facilitating donations to shelters and rescue organizations;

# Software Project (Classes)

## Date
A class for storing dates.

- has:
    - day (int)
    - month (int)
    - year (int)

- can:
    - format: returns a pretty formatted date
    - age: returns how many years have passed since date

## Address
Class for storing a structured address

- has:
    - street (str)
    - district (str)
    - number (str): can be "10", "11A", etc.
    - postal_code (int)

- can:
    - format: returns a pretty formatted address

## Profile
General informations for users and pets

- has:
    - name (str)
    - birth/open date (Date)
    - address (Adress)
    - description (str)

- can:
    - update_profile: change any attribute
    - format: returns all the profile's info in a pretty formatted way

## Donation
A money donation to a shelter

- has:
    - donor (Adopter)
    - receiver (Shelter)
    - ammount (float)
    - date (Date)

- can:
    - format: returns the donation's info in a pretty formatted way

## Question

- has:
    - name (str)
    - option (list[str])
    - preferred_answer (str): the best/right answer
    - user_answer (str)
    - is_preferred (bool): indicates if the given answer is equal to the preferred answer

- can:
    - answer: choose a option as answer
    - compute_compatibily: update 'is_preferred'

## Application
An Adopter's application to adopt a pet

- has:
    - applicant (Adopter)
    - pet (Pet)
    - form (list[Question])
    - status (str)
    - score (str): calculate the compatibility between the applicant's answers and the expected answers
    - feedback (str)

- can:
    - deny: deny the application, provides feedback
    - approve: approve the application and makes applicant the pet's tutor.
    - format: returns the questions, answers, score and status in a pretty formatted way

## Event
Shelter organized events (fundraisers, pet fairs, etc.)

- has:
    - location (Address)
    - date (Date)
    - status (str): indicates if event has happened, has been cancelled or is in stand-by or in planning

- can:
    - update: change any info
    - cancel: change status to 'cancelled'
    - end: chage status to 'done'

## User

- has:
    - username (str)
    - profile (Profile)
    - allowed_post_types (list[str])
    - posts (list[Post])

- can:
    - post: create a social post (Success Story, Forum or Educational, based on 'allowed_post_types')
    - list_posts: access all posts by all users
    - list_shelters: view all registered shelters
    - list_events: view all registered events
    - list_pets: view and interact with all available pets
    - query_pets: search pet based on various criteria

## Adopter (User)
Inherits User's attributes and methods

- has:
    - donations (list[Donation])
    - applications (list[Aplication])

- can:
    - donate: donate to a shelter

## Shelter (User)
Inherits User's attributes and methods.

Organizations that rescue pets and facilitate adoptions.

- has:
    - received_donations (list[Donation])
    - pets (list[Pet])
    - events (list[Event])
    - allowed_pet_types (list[str])

- can:
    - CRUD Pet: create, read, update and delete pets
    - CRUD Event: create, read, update and delete events
    - CRUD pet_type: create, read, update and delete allowed pet types
    - list_donations: view all received donations

## Accounts
Class for storing and managing all users

- has:
    - adopters (dict[str, Adopter])
    - shelters (dict[str, Shelter])

- can:
    - create_user: add a new User, return object
    - login: returns the User object based on the username

## Pet
Rescued animals

- has:
    - profile (Profile)
    - pet_type (str)
    - breed (str)
    - fur_color (str)
    - applications (list[Applications])
    - status (str): rescued, in_treatment, available_for_adoption, adopted
    - application_template (list[Question]): questions for application form
    - tutor (Adopter)

- can:
    - treat: change status to 'in_treatment'
    - make_available: change status to 'available_for_adoption'
    - add_template_question: add a question to application_template
    - apply_to_adopt: fill the pet's form to apply for adoption

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

## Post
A social post

- has:
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

## Feed
Feed with all registered posts

- has:
    - posts (list[Post])

- can:
    - list_posts: show all registered posts
    - create_post: add new post
    - delete_post: remove post from feed
