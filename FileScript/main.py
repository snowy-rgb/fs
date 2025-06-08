# main.py (프로그램의 진입점)
import parser  # 명령어 분석 모듈

def main():
    """파일 스크립트 실행 환경"""
    print(">>> File Script 실행 중... (help 명령어로 살펴보세요)\n")
    
    while True:
        command = input("FileScript> ")  # 사용자 입력
        if command.lower() == "exit":
            print("파일 스크립트를 종료합니다.")
            break
        parser.handle_command(command)  # 명령어 처리

if __name__ == "__main__":
    main()