# commands.py (파일 처리 모듈)
import os

# Master Path 저장 변수
MASTER_PATH = os.getcwd()  # 기본값: 현재 작업 디렉토리

def set_master_path(path):
    """Master Path 설정"""
    global MASTER_PATH
    if os.path.isdir(path):  # 경로가 실제로 존재하는지 확인
        MASTER_PATH = os.path.abspath(path)  # 절대 경로로 저장
        print(f"✅ MP 변경 완료: {MASTER_PATH}")
    else:
        print(f"⚠️ 오류: '{path}'는 존재하지 않는 폴더입니다! 올바른 경로를 입력하세요.")

def show_master_path():
    """현재 Master Path 출력"""
    print(f"📂 현재 MP: {MASTER_PATH}")




def load_file(filename):
    """파일을 불러와서 내용을 출력하는 함수"""
    if os.path.exists(filename):  # 파일 존재 여부 확인
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"\n실행> [파일 내용: {filename}]\n{content}\n")
    else:
        print(f"오류 : '{filename}' 파일을 찾을 수 없습니다. !not found file\n\n도움말 >> pwd를 이용해 현재 경로가 맞는지 확인하십시오. 파일이 존재하며, 확장자와 이름이 올바른지 확인하십시오.")

def print_working_directory(path=None):
    """현재 경로를 출력하거나 변경"""
    if path:
        try:
            os.chdir(path)  # 경로 변경
            print(f"실행> 경로 변경됨: {os.getcwd()}")
        except FileNotFoundError:
            print(f"오류 : '{path}' 경로를 찾을 수 없습니다. !can't find path\n\n도움말 >> pwd를 이용해 현재 경로를 확인하십시오. 경로가 존재하며, 현재 경로안에 있는지 확인하십시오.")
    else:
        print(f"실행> 현재 경로: {os.getcwd()}")

def save_file(filename, content):
    """MP 기준으로 파일을 저장하면서 #을 "로 변환"""
    content = content.replace("#", "\"")  # #을 "로 변경
    filepath = os.path.join(MASTER_PATH, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"실햄> 파일 저장 완료: {filepath}")

def create_new_file(filename):
    """MP 기준으로 새 파일을 생성"""
    filepath = os.path.join(MASTER_PATH, filename)
    if os.path.exists(filepath):
        print(f"FileError: '{filename}' 파일이 이미 존재합니다. !{filename} is already exist")
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("")  # 빈 파일 생성
        print(f"실행> 새 파일 생성 완료: {filepath}")

def help(cmd=None):
    """명령어 도움말 출력"""
    commands = {
        "exit": "File Script를 종료합니다.",
        "load": "파일 내용을 불러옵니다.",
        "save": "파일을 저장합니다.",
        "new": "새 파일을 생성합니다.",
        "pwd": "현재 작업 경로를 출력합니다.",
        "set mp": "파일 작업을 수행할 Master Path를 설정합니다.",
        "show mp": "현재 설정된 Master Path를 출력합니다."
    }

    imcmds = {
        "exit"  : "File Script를 종료합니다. cmd는 종료되지 않지만 시스템은 종료됩니다.",
        "load"  : "선택경로에서 파일 내용을 불러옵니다. pwd를 사용해 현재 작업 경로를 수정하거나 확인합니다.\n형식 : load 파일이름(.확장자)",
        "save"  : "파일을 입력한 파일이름 및 내용으로 저장합니다. Master Path 에 저장됩니다.\n형식 : save 파일이름(.확장자) 내용 \n내용에 \"를 입력할때에는 \" 대신 #를 입력합니다",
        "new"   : "새 파일을 입력한 이름으로 생성합니다. Master Path 에 저장됩니다.\n형식 : new 파일이름(.확장자)",
        "pwd"   : "현재 작업 경로를 출력합니다. pwd 경로 형식으로 경로를 변경합니다",
        "set "  : "파일 작업을 수행할 Master Path를 설정합니다.",
        "show"  : "현재 설정된 Master Path를 출력합니다."
    }

    if cmd is None:
        print(">>>>> 다음은 사용 가능한 명령어입니다")
        for command, description in commands.items():
            print(f"-- {command} : {description}")
    elif cmd.lower() in imcmds:
        print(f"-- 명령어 {cmd.lower()}\n\n>> {commands[cmd.lower()]}\n<<")
    else:
        print(f"NameError: '{cmd}'는 지원되지 않거나 올바르지 않은 명령어입니다 !{cmd} is not cmd\n")