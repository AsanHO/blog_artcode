장고 프로젝트의 뼈대 담당 폴더

1.  장고 설치
    cd 폴더명
    virtualenv venv
    가상환경 구성
    source venv/bin/activate
    가상환경 진입
    pip freeze > requirements.txt
    레시피 저장

2.  장고 프로젝트
    장고 폴더 정리
    setting.py 정리
    -DB 관련 문서-
    # https://ssungkang.tistory.com/entry/Django-Django-22-mysql-8-%EB%B2%84%EC%A0%84-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0
    # https://velog.io/@yoon1ee/django-mysql-%EC%97%B0%EB%8F%99
    $ mysql.server start
    migrate
    서버 테스트 하기

3.  모델
    앱 만들기
    세팅에 앱 설치
    모델 코드 작성
    m&m

4.  어드민
    *만약 db를 예전에 쓰던걸 쓰고 있다면 슈퍼유저계정도 저장되있음

5. 라우팅, 테스트뷰
    뷰 코드 작성
    테스트html설정
    테스트 -> 뷰 -> urls -> urls 순

6. 뷰
7. 폼
8. 배포 (psycopg2-binary도 설치)
9. 보안 강화(dotenv-.env) -배포전 체크리스트 만들기-