장고 프로젝트의 뼈대 담당 폴더

1.  cd 폴더명
    virtualenv venv
    가상환경 구성
    source venv/bin/activate
    가상환경 진입
    pip freeze > requirements.txt
    레시피 저장
2.  장고 폴더 정리
    setting.py 정리
    -DB 관련 문서-
    # https://ssungkang.tistory.com/entry/Django-Django-22-mysql-8-%EB%B2%84%EC%A0%84-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0
    # https://velog.io/@yoon1ee/django-mysql-%EC%97%B0%EB%8F%99
    $ mysql.server start
    migrate
