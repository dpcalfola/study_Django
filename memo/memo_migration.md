<h2> python manage.py migrate </h2>


-> INSTALL_APPS 설정을 탐색하여 필요한 DB table 생성


<h2> python manage.py makemigrations polls </h2>

-> Django 에게 모델을 변경시킨 사실과 변경사항을 migration 으로 저장시키고 싶다는 것을 알림

-> polls.migrations.0001_initial.py 파일이 생성됨

<h2>python manage.py sqlmigrate polls 0001</h2>

-> 0001_initial.py 가 생성하는 sql 구문 출력

-> 실행이 아닌 sql 구문만을 출력하는 것



<h2> python manage.py migrate </h2>



(
-> INSTALL_APPS 설정을 탐색하면서 DB table 생성하는 명령어

- 첫 명령어와 같음.
  )

-> polls 에 모델을 작성하고 make migrations 를 실행했으므로 
migrate 명령은 INSTALL_APPS 설정을 탐색해면서
변경사항을 수집하고 
그 결과를 sqlite3 에 테이블 생성