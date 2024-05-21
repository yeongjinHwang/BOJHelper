## 백준 사이트없이 vs code에서 백준을 풀어보자
-----
### 개발 이유
1. 개발자는 vscode를 주로 사용한다.
2. 백준을 풀기위해서 백준 사이트를 접속해야된다.
3. vscode로 문제를 푼 후 다시 백준에 붙여넣기로 정답인지 확인한다.

+ 나는 다음의 방법에서 vscode만으로 해결을 하고자 이 프로그램을 개발했다.
+ 추가적으로 정답검증을 직접 하는 것도 귀찮아!! 이것도 해결하고자 개발했다.
-----
### 사용 방법
1. $ python prob_generate.py 실행 후 문제번호 적기
2. prob_solve.py에 문제풀이 코드를 적기
3. $ python answer_check.py를 통해 테스트케이스와 비교하기
-----
### 기능
1. prob_generate.py를 통해 문제번호를 입력하면, 해당 문제에 대한 모든 정보를 txt형태로 저장(problem/problem_{number}.txt)
2. answer_check.py를 통해 해당 문제에 대한 입출력 예시에 대한 검증
3. 모든 테스트케이스 검증에서 passed된다면 정답코드 저장 (problem/problem_{number}.py)
4. To do ... 모든 테스트케이스에 통과될 경우 baekjoon으로 보내기 (가능...?)
5. To do ... baekjoon에 보내고 완벽한 정답일 때 github에 자동 업로드
6. 문제 번호 없이 문제 난이도 기준으로 뽑아올 수 있게 하기
-----

# Example 1025

## prob_generate
![prob](https://github.com/yeongjinHwang/BOJHelper/assets/83944553/a42840c2-f538-43a9-95b9-87849ce4a49f)

## answer_check
![answer_check](https://github.com/yeongjinHwang/BOJHelper/assets/83944553/25d625a2-a289-4f7a-8180-b9d8999803a3)
