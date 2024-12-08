import os
import shutil

def cleanup_local_files():

    """
    Delete all downloaded files and directories under temp_scan_files
    """

    try:
        if os.path.exists('temp_scan_files'):
            shutil.rmtree('temp_scan_files')
            print("Successfully deleted all downloaded files")
    except Exception as e:
        print(f"Error deleting files: {str(e)}")