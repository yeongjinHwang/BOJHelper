## 백준 사이트없이 vs code에서 백준을 풀어보자
-----
1. 개발자는 vscode를 주로 사용한다.
2. 백준을 풀기위해서 백준 사이트를 접속해야된다.
3. vscode로 문제를 푼 후 다시 백준에 붙여넣기로 정답인지 확인한다.

+ 나는 다음의 방법에서 vscode만으로 해결을 하고자 이 프로그램을 개발했다.
-----
1. $ python prob_generate.py 실행 후 문제번호 적기
--> 해당 문제에 대한 정보를 problem_{number}.txt로 저장해줌
2. prob_solve.py에서 def solve(): 내부에 문제풀이 코드를 적기
3. $ python answer_check.py를 통해 테스트케이스와 비교하기
--> 모든 테스트 케이스와 정답이 일치한다면 baekjoon_{number}.py 형태로 정답파일을 만들어줌
-----
ex)1025
prob_generate
![prob](https://github.com/yeongjinHwang/BOJHelper/assets/83944553/a42840c2-f538-43a9-95b9-87849ce4a49f)

answer_check
![image](https://github.com/yeongjinHwang/BOJHelper/assets/83944553/25d625a2-a289-4f7a-8180-b9d8999803a3)
