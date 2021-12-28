import pychromecast
import subprocess
import sys

# This is called when the FastAPI endpoint is triggered so that a subprocess can execute the athan playing
def execute_athan(audio_id, speaker_name):
    # might update this to execute directly here rather than calling bash file
    resp = subprocess.run(['python', 'bilal_server/play_athan.py', audio_id, speaker_name], capture_output=True, text=True)
    return resp.stdout.rstrip("\n")

# This is run when the play_athan.sh script is exectued and will play the athan on the speaker
def play_athan(audio_id, speaker_name):
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[speaker_name])
    cast = chromecasts[0]
    cast.wait()
    mc = cast.media_controller
    mc.play_media(f'https://drive.google.com/uc?export=download&id={audio_id}', 'audio/mp3')
    return f"Sound is playing on {speaker_name}"

# the play_athan.sh script runs this as main
if __name__ == '__main__':
    resp = play_athan(sys.argv[1], sys.argv[2]) # find a better way to pass the arugments
    print(resp) # pass stdout to FastAPI