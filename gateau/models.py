from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.urls import reverse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 주연배우
class Dessert(TimestampedModel):
    name = models.CharField(max_length=50, db_index=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "black sesame dessert"
        verbose_name_plural = "black sesame desserts"


class Cafe(TimestampedModel):
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, verbose_name="대표 메뉴")
    name = models.CharField(max_length=100)
    scenery = models.ImageField(verbose_name="카페 사진")
    address = models.TextField(verbose_name="주소")

    def __str__(self) -> str:
        return self.name

    # 뭘 기대하냐면
    # movie 인스턴스에 대한 detail URL 문자열을 리턴하기를 기대.
    def get_absolute_url(self) -> str:
        # url = f"/movie/movies/{self.pk}/" # 하드코딩
        url = reverse("cafe_detail", args=[self.pk])
        # url = reverse("movie_detail", kwargs={"pk": self.pk})
        return url


class Video(TimestampedModel):
    name = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    youtube_link = models.URLField()

    # 인자없는 멤버함수는 속성처럼 사용하고 싶습니다.
    @property
    def youtube_id(self):
        # https://www.youtube.com/watch?v=xyfozmk1SxQ
        if "v=" in self.youtube_url:
            return self.youtube_url.split("v=")[1]
        return None

    @property
    def youtube_embed_html(self):
        if self.youtube_id:
            return render_to_string(
                "gateau/_youtube_embed.html",
                {
                    "youtube_id": self.youtube_id,
                },
            )
        return None


class Recipe(TimestampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Dessert, on_delete=models.CASCADE)
    desc = models.TextField()
