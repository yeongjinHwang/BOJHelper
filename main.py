import requests
from bs4 import BeautifulSoup

def fetch_problem_details(problem_number):
    url = f"https://www.acmicpc.net/problem/{problem_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch problem details: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 제목과 설명
    title = soup.find('title').text.strip()
    problem_description = soup.find('div', {'id': 'problem_description'}).text.strip()
    problem_input = soup.find('div', {'id': 'problem_input'}).text.strip()
    problem_output = soup.find('div', {'id': 'problem_output'}).text.strip()

    # 입력 및 출력 예시
    sample_inputs = []
    sample_outputs = []
    example_pairs = soup.find_all('pre', {'class': 'sampledata'})

    for i in range(0, len(example_pairs), 2):
        sample_inputs.append(example_pairs[i].text.strip())
        if i + 1 < len(example_pairs):
            sample_outputs.append(example_pairs[i + 1].text.strip())

    # 추가 정보
    info_table = soup.find('table', {'id': 'problem-info'})
    info_labels = ["time_limit", "memory_limit", "submissions", "correct", "user_correct", "accuracy"]
    info = {label: info_table.find_all('td')[i].text.strip() for i, label in enumerate(info_labels)}

    # 파일로 저장
    with open(f"problem_{problem_number}.txt", 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n\n")
        file.write("Additional Information:\n")
        for key, value in info.items():
            file.write(f"{key.replace('_', ' ').capitalize()}: {value}\n")
        file.write("\n")

        file.write("Problem Description:\n")
        file.write(problem_description + "\n\n")
        file.write("Input Description:\n")
        file.write(problem_input + "\n\n")
        file.write("Output Description:\n")
        file.write(problem_output + "\n\n")

        # 예시 입력 및 출력 번갈아 기록
        for i in range(len(sample_inputs)):
            file.write(f"Sample Input {i+1}:\n{sample_inputs[i]}\n\n")
            if i < len(sample_outputs):
                file.write(f"Sample Output {i+1}:\n{sample_outputs[i]}\n\n")

    print(f"Problem details saved to problem_{problem_number}.txt")

if __name__ == "__main__":
    problem_number = input("Enter the problem number: ")
    fetch_problem_details(problem_number)
