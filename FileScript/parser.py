# parser.py (PWD 명령어 추가)
import commands
import shlex  # 띄어쓰기 포함된 문자열을 하나로 인식
import re  # 정규 표현식을 사용하기 위한 모듈

def is_quote_balanced(command):
    """입력된 문자열에 따옴표가 올바르게 닫혀 있는지 확인"""
    double_quote_count = command.count('"')
    single_quote_count = command.count("'")

    if double_quote_count % 2 == 1 or single_quote_count % 2 == 1:
        if double_quote_count < 3 or single_quote_count < 3 :
            return False  # 따옴표 개수가 홀수면 오류 발생
    
    return True

def is_more_three(command):
    """입력된 문자의 따옴표가 3개 이상인지 확인"""
    double_quote_count = command.count('"')
    single_quote_count = command.count("'")

    if double_quote_count % 2 == 1 or single_quote_count % 2 == 1:
        if double_quote_count >= 3 or single_quote_count >= 3 :
            return False  # 따옴표 개수가 홀수면 오류 발생
    
    return True

def is_exist_backsl(command):
    bs = command.count('\\')

    if bs > 0 :
        print()
        return False
    
    return True

def preprocess_command(command):
    """백슬래시(\\)가 마지막에 올 경우 자동으로 수정"""
    if command.endswith("\\"):
        print("⚠️ 오류: 경로의 마지막에 백슬래시('\\')가 포함될 수 없습니다! (예: PWD \"C:\\Users\\Jeonghwa KIM\\Desktop\")")
        return None  # 오류 발생 시 실행하지 않음
    
    return command.replace("\\", "/")  # 백슬래시를 슬래시로 변환




def handle_command(command):
    """사용자 명령을 분석하고 실행"""
    try:
        command = command.strip()

        if not command:
            return  
        
        if command is None:
            return  # 오류 발생 시 실행하지 않음


        
        if command.startswith('"') or command.startswith("'") :
            print("SyntaxError: 처음에 \'나 \"가 존재할 수 없습니다. !can't exist \' or \" \n\n올바른 형식이 아닙니다.")
            return
        
        if not is_exist_backsl(command):
            print("경고: \\는 허용되지 않습니다. 경로를 사용할 경우 /를 사용하세요. \n\n형식이 올바르지 않습니다. 허용되지 않는 형식입니다.")
            return
                
        
        if not is_quote_balanced(command):
            print("SyntaxError: 따옴표가 올바르게 닫히지 않았습니다. !\' or \' expected \n\n도움말 >> \'나 \"가 올바르게 닫혔는지 확인하십시오. 문장이 올바른지 확인하십시오. \n\n또는 형식이 올바르거나 중복되지 않았는지 확인하십시오.")
            return
        
        if not is_more_three(command):
            print("SyntaxError: 3개 이상의 홀수 따옴표가 감지되었습니다. !\' or \' is expected \n\n도움말 >> \'나 \"가 올바르게 닫혔는지 확인하십시오. 문장이 올바른지 확인하십시오. \n\n또는 형식이 올바르거나 중복되지 않았는지 확인하십시오.")
            return
        
        try:
            parts = shlex.split(command)  # 띄어쓰기 포함된 문자열을 하나의 인자로 변환
        except ValueError:
            evr = ValueError
            print(f"Error?: 따옴표가 올바르게 닫히지 않아 명령어를 처리할 수 없습니다.\n{evr}")


        # for part in parts:
        #    if part.count('"') % 2 == 1 or part.count("'") % 2 == 1:  # 따옴표 개수가 홀수이면 오류
        #        print(f"⚠️ 오류: '{part}' 따옴표가 올바르게 닫히지 않았습니다! (예: LOAD \"file name.txt\")")
        #        return

        
        if parts[0].upper() == "PWD":
            if len(parts) == 2:
                commands.print_working_directory(parts[1])  # 경로 변경
            elif len(parts) >= 3 :
                errPartPWD = parts[2]
                print(f"ValueError : [{errPartPWD}.. ] PWD 경로를 하나만 지정할 수 있습니다. !can't designate more than 1 path\n\n도움말 >> pwd 명령어는 이동할 경로를 받습니다. 만약 띄어쓰기가 있다면, \"\"로 감싸여 출력하세요.")
            else:
                commands.print_working_directory()  # 현재 경로 출력
        elif len(parts) == 2 and parts[0].upper() == "LOAD":
            commands.load_file(parts[1])  
        elif len(parts) == 1 and parts[0].upper() == "LOAD" :
            print("ValueError : 항후 값이 예상되었지만 누락되었습니다. !expected value \n\n도움말 >> load 명령어는 파일 이름이 필요합니다. 값이 올바른지 확인하십시오. 값이 입력되었는지 확인하십시오.\n형식 : load 파일이름.확장자")
        elif len(parts) >= 3 and parts[0].upper() == "LOAD" :
            errPart = parts[2]
            print(f"ValueError : [{errPart}.. ] load는 값을 1개 까지만 받을 수 있습니다. !can't input more than 1 value\n\n도움말 >> load 명령어는 불러올 파일의 값을 받습니다. 만약 띄어쓰기가 있다면, \"\"로 감싸여 출력하세요.\n형식 : load 파일이름.확장자")
        elif parts[0].upper() == "SET" and len(parts) == 3 and parts[1].upper() == "MP":
            commands.set_master_path(parts[2])  # MP 변경
        elif parts[0].upper() == "SET" and len(parts) == 3 and parts[1].upper() != "MP":
            setErOne = parts[1]
            print(f"ValueError : [{setErOne}.. ] 예상되지 않은 값이 입력되었습니다. !unexpected value\n\n지원되지 않는 형식의 값입니다. mp, master path 만 지원됩니다.")
        elif parts[0].upper() == "SET" and len(parts) <= 2 :
            print("ValueError : 항후 값이 예상되었지만 누락되었습니다. !expected value \n\n도움말 >> set 명령어는 형식 및 형식값 필요합니다. 값이 올바른지 확인하십시오. 값이 입력되었는지 확인하십시오.\n지원형식 : set mp 경로")
        elif parts[0].upper() == "SET" and len(parts) > 3 : 
            errMoreSet = parts[3]
            print(f"ValueError : [{errMoreSet}.. ] 예상되지 않은 값이 입력되었습니다. !unexpected values\n\n도움말 >> set 명령어는 2개의 값을 받습니다. 만약 띄어쓰기가 있다면, \"\"로 감싸여 출력하세요.")
        elif parts[0].upper() == "SHOW" and len(parts) == 2 and parts[1].upper() == "MP":
            commands.show_master_path()  # MP 출력
        elif parts[0].upper() == "SHOW" and len(parts) == 2 and parts[1].upper() != "MP":
            showErOne = parts[1]
            print(f"ValueError : [{setErOne}.. ] 예상되지 않은 값이 입력되었습니다. !unexpected value\n\n지원되지 않는 형식의 값입니다. mp 만 지원됩니다.")
        elif parts[0].upper() == "SHOW" and len(parts) <= 1 :
            print("ValueError : 항후 값이 예상되었지만 누락되었습니다. !expected value \n\n도움말 >> show 명령어는 형식이 필요합니다. 값이 올바른지 확인하십시오. 값이 입력되었는지 확인하십시오.\n지원형식 : show mp")
        elif parts[0].upper() == "SHOW" and len(parts) > 2 :
            errMoreSet = parts[2]
            print(f"ValueError : [{errMoreSet}.. ] 예상되지 않은 값이 입력되었습니다. !unexpected values\n\n도움말 >> show 명령어는 1개의 값을 받습니다. 필요없는 값이 입력되지 않았는지 확인하십시오.")
        elif parts[0].upper() == "SAVE" and len(parts) == 3:
            commands.save_file(parts[1], parts[2])  # MP 기준으로 파일 저장
        elif parts[0].upper() == "SAVE" and len(parts) <= 2:
            print("ValueError : 항후 값이 예상되었지만 누락되었습니다. !expected value \n\n도움말 >> save 명령어는 파일이름 및 내용이 필요합니다. 값이 올바른지 확인하십시오. 값이 입력되었는지 확인하십시오.\n지원형식 : save 파일이름(.확장자) 내용")
        elif parts[0].upper() == "SAVE" and len(parts) > 3:
            errSaveOne = parts[3]
            print(f"ValueError : [{errSaveOne}.. ] 예상되지 않은 값이 입력되었습니다. !unexpected values\n\n도움말 >> save 명령어는 2개의 값을 받습니다. 필요없는 값이 입력되지 않았는지 확인하십시오.")
        elif parts[0].upper() == "NEW" and len(parts) == 2:
            commands.create_new_file(parts[1])  # MP 기준으로 새 파일 생성
        elif parts[0].upper() == "NEW" and len(parts) > 2:
            errNew = parts[2]
            print(f"ValueError : [{errNew}.. ] 예상되지 않은 값이 입력되었습니다. !unexpected values\n\n도움말 >> new 명령어는 1개의 값을 받습니다. 필요없는 값이 입력되지 않았는지 확인하십시오.\n만약 띄어쓰기를 사용한다면 \"\"로 감싸 사용하세요.")
        elif parts[0].upper() == "NEW" and len(parts) <= 1:
            print("ValueError : 항후 값이 예상되었지만 누락되었습니다. !expected value \n\n도움말 >> new 명령어는 파일이름이 필요합니다. 값이 올바른지 확인하십시오. 값이 입력되었는지 확인하십시오.\n지원형식 : new 파일이름(.확장자)")
        elif parts[0].upper() == "HELP" and len(parts) == 1:
            commands.help()
        elif parts[0].upper() == "HELP" and len(parts) == 2:
            com = parts[1]
            commands.help(com)
        else:
            print("NameError : 올바른 명령어를 입력하세요. !not found command : %s ..\n" % parts[0] )

    except Exception as e:
        print(f"error? : 예상치 못한 오류가 발생했습니다 ?unexpected error {e}\n")
