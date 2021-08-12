# 홍익대학교 빅데이터 과정 django 4번째 미니 프로젝트.

## * 주제 : 흑임자에 관한 모든 것.
## * 구현 내용
- Dessert
    - name
    - photo
- Cafe
    - dessert[F - Dessert]
    - name
    - scenery(img)
    - address
- Video
    - cafe[F - Dessert]
    - title
    - youtube_link
- Recipe
    - author(F - User)
    - name(F - Dessert)
    - desc
