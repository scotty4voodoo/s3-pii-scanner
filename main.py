from getobj import download_s3_objects
from scan import write_scan_results_to_file
from clean import cleanup_local_files
from reporter import send_results_via_sns

def print_banner():
    print("""
 _______  ______     _______ __________________     _______  _______  _______  _        _        _______  _______ 
(  ____ \/ ___  \   (  ____ )\__   __/\__   __/    (  ____ \(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ )
| (    \/\/   \  \  | (    )|   ) (      ) (       | (    \/| (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    )|
| (_____    ___) /  | (____)|   | |      | | _____ | (_____ | |      | (___) ||   \ | ||   \ | || (__    | (____)|
(_____  )  (___ (   |  _____)   | |      | |(_____)(_____  )| |      |  ___  || (\ \) || (\ \) ||  __)   |     __)
      ) |      ) \  | (         | |      | |             ) || |      | (   ) || | \   || | \   || (      | (\ (   
/\____) |/\___/  /  | )      ___) (______) (___    /\____) || (____/\| )   ( || )  \  || )  \  || (____/\| ) \ \__
\_______)\______/   |/       \_______/\_______/    \_______)(_______/|/     \||/    )_)|/    )_)(_______/|/   \__/
""")

if __name__ == "__main__":
    print_banner()
    download_s3_objects()
    output_file = write_scan_results_to_file()
    send_results_via_sns("SNS ARN 입력",output_file)
    cleanup_local_files()