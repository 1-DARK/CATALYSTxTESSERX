from rest_framework import serializers
from base.models import Img, Text, Audio, Video, Pdf

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = "__all__"
        
class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = "__all__"
        
class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class PdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = "__all__"
        
