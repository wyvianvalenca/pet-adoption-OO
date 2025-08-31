from datetime import date
from src.adopter import Adopter
from src.donation import Donation
from src.pet import Pet
from src.post import Post
from src.shelter import Shelter


def create_data():
    a1 = Adopter("wgcv", "Wyvian Valenca")
    a2 = Adopter("ybss", "Ycaro Sales")

    s1 = Shelter("csf", "Casa Sao Franscisco")
    s2 = Shelter("rh", "Reptile House")

    s1.add_allowed_pet_type("dog")
    s2.add_allowed_pet_type("turtle")

    p1 = Pet("shiro", s1.username, "dog")
    p2 = Pet("becky", s1.username, "dog")
    p3 = Pet("jack", s2.username, "turtle")

    p1.apply_adoption(a1.username, ["Yes"])
    p1.apply_adoption(a2.username, ["Yes"])
    p2.apply_adoption(a1.username, ["Yes"])
    p3.apply_adoption(a1.username, ["Yes"])

    post1 = Post(s1, "educational",
                 "The Decompression Period: Giving Your New Pet Time to Adjust", """
Bringing a new pet home is an exciting time, but it's crucial to remember the **"3-3-3 Rule"** for rescue animals. This guideline helps you set realistic expectations for their adjustment period.

### The 3-3-3 Rule:
- **First 3 Days:** Your new pet will likely feel overwhelmed and scared.
    - They are not yet comfortable enough to be themselves. Don't be surprised if they hide or don't eat much.
- **First 3 Weeks:** Your pet is starting to settle in and learn your routine.
    - Their personality will begin to emerge as they realize they are in a safe and stable environment.
- **First 3 Months:** Your pet now feels at home and has built trust with your family.
    - This is when you'll see their true personality, and a real bond has been established.

***
*Patience during this time is the key to building a strong, lifelong foundation of trust.* """)

    post2 = Post(s2, "forum", "Volunteers Needed for Our Upcoming 'Clear the Kennel' Adoption Drive!", """
Hello, pet-loving community! Sunny Paws Shelter is hosting our annual **"Clear the Kennels"** adoption event in two weeks, and we're looking for enthusiastic volunteers to help make the day a success.

We need help with tasks like:
- Walking dogs and supervising play areas
- Managing the kitten playpen
- Talking to potential adopters about our amazing animals
- Assisting with the information and sign-up desk

If you're available to lend a hand and want to help our residents find their forever homes, please let us know in the comments! """)

    d1 = Donation(a1.username, s1.username, 100.00, date.today())
    d2 = Donation(a1.username, s2.username, 120.00, date.today())
