import os
import subprocess


def video_audio_merge(video_files_path, audio_files_path, sep=''):
    result_dir = os.path.join(video_files_path, 'result')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        for f in os.listdir(video_files_path):
            if not f.endswith('.mkv'):
                continue
            result_file = f.split(sep)[1].strip()
            print(result_file)
            audio_file = os.path.join(audio_files_path, result_file.replace('.mkv', '.mka'))
            origin_file = os.path.join(video_files_path, f)
            mkvmerge = subprocess.Popen(['mkvmerge',
                                         '-o', '%s' % os.path.join(result_dir,
                                                                   result_file),
                                         '-A', '-S', '%s' % origin_file,
                                         '%s' % audio_file])
            mkvmerge.communicate()

