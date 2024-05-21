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
        actual_output = run_test_case(problem_number, sample_input).strip()
        
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
    else:
        print("테스트 케이스 중 일부가 실패했습니다.")

if __name__ == "__main__":
    problem_number = input("Enter the problem number to check: ")
    check_solution(problem_number)
    os.remove("input.txt")