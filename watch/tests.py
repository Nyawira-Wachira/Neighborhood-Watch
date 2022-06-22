from django.test import TestCase
from .models import Profile,  Neighborhood,Post,Business,HealthCentre,PoliceAuthority

# Create your tests here.
class ProfileTestClass(TestCase):

        # Set up method
    def setUp(self):
        self.abigail= Profile(profile_picture='default.png', contact_info='0712345678')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abigail,Profile))



        # Testing Save Method
    def test_save_method(self):
       self.abigail.save()
       all_objects = Profile.objects.all()
       self.assertTrue(len(all_objects)>0)

class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.drawing= Post( caption ='drawing', posted ='2022-June-20 3:00pm', picture='default.png')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.drawing,Post))

    def test_save_method(self):
       self.drawing.save()
       all_objects = Post.objects.all()
       self.assertTrue(len(all_objects)>0)

class NeighborhoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.RidgeWood= Neighborhood( neighborhood_id ='1', name ='RidgeWood', picture='default.png', location ='Woods',occupants_count = '300')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.RidgeWood,Neighborhood))

    def test_save_method(self):
       self.RidgeWood.save()
       all_objects = Neighborhood.objects.all()
       self.assertTrue(len(all_objects)>0)

class BusinessTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.ToyStore= Business( name ='ToyStore',picture='default.png',email='toystore@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ToyStore,Business))

        # Testing Save Method
    def test_save_method(self):
       self.ToyStore.save()
       all_objects = Business.objects.all()
       self.assertTrue(len(all_objects)>0)

# class HealthCentre(TestCase):

#     # Set up method
    def setUp(self):
        self.Hospital= HealthCentre(name='Hospital',picture='default.png',contact_info='0712345678',email='hospital@gmail.com')

#     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Hospital,HealthCentre))

        # Testing Save Method
    def test_save_method(self):
       self.Hospital.save()
       all_objects = HealthCentre.objects.all()
       self.assertTrue(len(all_objects)>0)


class PoliceAuthorityTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Police= PoliceAuthority(name ='Police', picture='default.png',contact_info='0712345678',email='police@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Police,PoliceAuthority))

        # Testing Save Method
    def test_save_method(self):
       self.Police.save()
       all_objects = PoliceAuthority.objects.all()
       self.assertTrue(len(all_objects)>0)