import subprocess
import io
import sys
import os

def run_test_case(test_input):
    # Save the test input to a file
    with open("input.txt", "w", encoding='utf-8') as file:
        file.write(test_input)
    
    # Run the prob_solve.py script with the test input
    result = subprocess.run(["python", "prob_solve.py"], input=test_input, text=True, capture_output=True)
    return result.stdout.strip()

def check_solution(problem_number):
    # 문제 정보 파일 로드
    with open(f"problem/problem_{problem_number}.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 샘플 입력과 출력 파싱
    sample_inputs = []
    sample_outputs = []
    is_input = False
    is_output = False
    current_input = []
    current_output = []

    for line in content.split('\n'):
        if line.startswith("Sample Input"):
            if current_input:
                sample_inputs.append('\n'.join(current_input))
                current_input = []
            is_input = True
            is_output = False
        elif line.startswith("Sample Output"):
            if current_output:
                sample_outputs.append('\n'.join(current_output))
                current_output = []
            is_input = False
            is_output = True
        elif is_input:
            current_input.append(line.strip())
        elif is_output:
            current_output.append(line.strip())
    
    if current_input:
        sample_inputs.append('\n'.join(current_input))
    if current_output:
        sample_outputs.append('\n'.join(current_output))
    
    # 각 샘플 케이스에 대해 테스트 실행
    passed_count = 0
    for i, sample_input in enumerate(sample_inputs):
        expected_output = sample_outputs[i].strip()
        actual_output = run_test_case(sample_input).strip()
        
        expected_lines = expected_output.split('\n')
        actual_lines = actual_output.split('\n')

        if expected_lines == actual_lines:
            print(f"Test Case {i+1}: Passed")
            passed_count += 1
        else:
            print(f"Test Case {i+1}: Failed")
        print(f"Expected Output:\n{expected_output}")
        print(f"Actual Output:\n{actual_output}")
        print()

    if passed_count == len(sample_inputs):
        print("모든 테스트 케이스 통과")
        # prob_solve.py 파일을 problem_{problem_number}.py로 저장
        with open("prob_solve.py", 'r', encoding='utf-8') as file:
            code = file.read()
        with open(f'problem/problem_{problem_number}.py', 'w', encoding='utf-8') as file:
            file.write(code)
        
        # GitHub에 파일 업로드
        upload_to_github(problem_number)
        
    else:
        print("테스트 케이스 중 일부가 실패했습니다.")

def upload_to_github(problem_number):
    # user_info.txt 파일에서 GitHub URL, 사용자 ID, 비밀번호 읽기
    with open('user_info.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        url = lines[0].strip().split('=')[1]
        username = lines[1].strip().split('=')[1]
        password = lines[2].strip().split('=')[1]
    
    # GitHub 리포지토리에 push
    commands = [
        ['git', 'add', f'problem/problem_{problem_number}.py', f'problem/problem_{problem_number}.txt'],
        ['git', 'commit', '-m', f"Add problem {problem_number} files"],
        ['git', 'push', url, f'--repo={username}:{password}@{url}']
    ]
    
    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {' '.join(command)} failed with message:\n{result.stderr}")
            return False
    print(f"Problem {problem_number} files successfully uploaded to GitHub.")
    return True

if __name__ == "__main__":
    problem_number = input("Enter the problem number to check: ")
    check_solution(problem_number)
    os.remove("input.txt")
