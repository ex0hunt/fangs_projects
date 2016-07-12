import os
import subprocess

def volume_increaser(files_path, sep=''):
    result_dir = os.path.join(files_path, 'result')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        for f in os.listdir(files_path):
            if not f.endswith('.mka'):
                continue
            full_path = os.path.join(files_path, f)
            result_filename = f.split(sep)[1].strip()
            print(result_filename)
            ffmpeg = subprocess.Popen(['ffmpeg', '-i', '%s' % full_path, '-vcodec', 'copy', '-af','volume=20dB', '%s' %os.path.join(result_dir, result_filename)])
            ffmpeg.communicate()
