import importlib.util
import io
import sys
import inspect
from textwrap import dedent

def load_module(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_test_case(module, test_input):
    # Redirect stdout to capture the print output
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    
    try:
        sys.stdin = io.StringIO(test_input)
        module.solve()
        output = new_stdout.getvalue().strip()
    finally:
        sys.stdout = old_stdout
        sys.stdin = sys.__stdin__
    
    return output

def save_solution_code(module, problem_number):
    # solve 함수의 소스 코드 추출
    solve_function = module.solve
    source_lines = inspect.getsourcelines(solve_function)[0]
    
    # 함수 정의와 마지막 줄 제거하여 함수 내부 코드만 추출
    function_body = "".join(source_lines[1:])
    
    # 함수 내부 코드의 들여쓰기 제거
    dedented_body = dedent(function_body)
    
    with open(f'baekjoon_{problem_number}.py', 'w', encoding='utf-8') as file:
        file.write(dedented_body)

def check_solution(problem_number):
    # 문제 정보 파일 로드
    with open(f"problem_{problem_number}.txt", 'r', encoding='utf-8') as file:
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
    
    # prob_solve.py 모듈 로드
    module = load_module("prob_solve", "prob_solve.py")
    
    # 각 샘플 케이스에 대해 테스트 실행
    passed_count = 0
    for i, sample_input in enumerate(sample_inputs):
        expected_output = sample_outputs[i].strip()
        actual_output = run_test_case(module, sample_input).strip()
        
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
        # solve 함수 내부 코드만 baekjoon_{problem_number}.py로 저장
        save_solution_code(module, problem_number)
    else:
        print("테스트 케이스 중 일부가 실패했습니다.")

if __name__ == "__main__":
    problem_number = input("Enter the problem number to check: ")
    check_solution(problem_number)
