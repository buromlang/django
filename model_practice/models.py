from django.db import models

# Create your models here.
import datetime


class Test(models.Model):
    interval_time = datetime.timedelta(days=1, seconds=1.0)
    duration_field_test = models.DurationField(default=interval_time)
    # email_test = models.EmailField(default="not provided")
    # file_upload = models.FileField(upload_to="./testfields/templates/images/test_%y")
    decimal_field = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    float_field = models.FloatField()
    generic_ip_address = models.GenericIPAddressField(null=True, protocol='ipv6', blank=True)
    generic_ip_address_both = models.GenericIPAddressField(protocol='both', null=True, blank=True)
    #input for the below is ::ffff:192.0.2.1
    generic_ip_address_unpack_ipv4 = models.GenericIPAddressField(null=True, protocol='both', unpack_ipv4=True, blank=True)




    def upload_path(self, filenames):
        return f"./model_practice/static/model_practice/path_{self}/{filenames}"

    upload_file = models.FileField(default="not provided", upload_to=upload_path, null=True)
    # file_path = models.FilePathField(default="./model_practice/static/images/", null=True)
    file_path = models.FilePathField(path='./model_practice/static/path_test1', match=None, recursive=True, allow_files=True, allow_folders=True, max_length=100, null=True)
    # field_test = models.FieldFile(upload_file)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)

    image_file = models.ImageField(default="./model_practice/static/model_practice/images/Image_created_with_a_mobile_phone.png",
                                   upload_to='./model_practice/static/model_practice/images', height_field="height", width_field="width")

    def __str__(self):

        return f"test{self.duration_field_test.seconds}"


# instance_ref = Test(upload_file="./model_practice/templates/static/images")
# field_file = instance_ref.upload_file
# file_url = field_file.url
# file_path = field_file.path
# print(file_url)
# print(file_path)
